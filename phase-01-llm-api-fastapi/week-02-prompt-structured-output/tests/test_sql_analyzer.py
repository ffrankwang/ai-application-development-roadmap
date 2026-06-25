import sys
import os
from unittest.mock import MagicMock

# 将 src 目录加入 sys.path，以便导入源码模块
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

# 在导入 sql_analyzer 之前 mock 外部依赖
mock_dotenv = MagicMock()
mock_openai = MagicMock()
mock_prompt_templates = MagicMock()
mock_prompt_templates.SYSTEM_PROMPT = {"sql_analyzer": "mock prompt"}

sys.modules["dotenv"] = mock_dotenv
sys.modules["openai"] = mock_openai
sys.modules["prompt_templates"] = mock_prompt_templates

import unittest
from sql_analyzer import parse_json_response


class TestParseJsonResponse(unittest.TestCase):

    def test_valid_json_object(self):
        """解析正常的 JSON 对象"""
        response = '{"summary": "查询用户", "risk_level": "低", "problems": "无", "suggestions": "添加索引"}'
        result = parse_json_response(response)
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["summary"], "查询用户")
        self.assertEqual(result["data"]["risk_level"], "低")
        self.assertEqual(result["data"]["problems"], "无")
        self.assertEqual(result["data"]["suggestions"], "添加索引")

    def test_valid_json_with_nested_structure(self):
        """解析嵌套结构的 JSON"""
        response = '{"summary": "复杂查询", "details": {"table": "users", "columns": ["id", "name"]}}'
        result = parse_json_response(response)
        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["details"]["table"], "users")
        self.assertEqual(result["data"]["details"]["columns"], ["id", "name"])

    def test_valid_json_array(self):
        """解析 JSON 数组"""
        response = '[{"id": 1}, {"id": 2}]'
        result = parse_json_response(response)
        self.assertTrue(result["success"])
        self.assertEqual(len(result["data"]), 2)
        self.assertEqual(result["data"][0]["id"], 1)

    def test_valid_json_primitive_string(self):
        """解析原始 JSON 字符串值"""
        response = '"hello world"'
        result = parse_json_response(response)
        self.assertTrue(result["success"])
        self.assertEqual(result["data"], "hello world")

    def test_valid_json_number(self):
        """解析 JSON 数字"""
        response = "42"
        result = parse_json_response(response)
        self.assertTrue(result["success"])
        self.assertEqual(result["data"], 42)

    def test_valid_json_boolean(self):
        """解析 JSON 布尔值"""
        response = "true"
        result = parse_json_response(response)
        self.assertTrue(result["success"])
        self.assertEqual(result["data"], True)

    def test_valid_json_null(self):
        """解析 JSON null"""
        response = "null"
        result = parse_json_response(response)
        self.assertTrue(result["success"])
        self.assertIsNone(result["data"])

    # ---- 非正常 JSON 格式 ----

    def test_invalid_json_missing_brace(self):
        """缺少闭合大括号"""
        response = '{"summary": "查询用户", "risk_level": "低"'
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])

    def test_invalid_json_trailing_comma(self):
        """JSON 末尾多余逗号"""
        response = '{"summary": "查询用户",}'
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])

    def test_invalid_json_single_quotes(self):
        """使用单引号（非标准 JSON）"""
        response = "{'summary': '查询用户'}"
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])

    def test_invalid_json_unquoted_key(self):
        """键名未用双引号"""
        response = '{summary: "查询用户"}'
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])

    def test_invalid_json_garbled_text(self):
        """完全不是 JSON 的乱码文本"""
        response = "这是SQL分析结果：查询效率较低，建议优化。"
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])

    def test_invalid_json_with_markdown_wrapper(self):
        """LLM 常见错误：带有 Markdown 代码块标记的 JSON"""
        response = '```json\n{"summary": "查询用户", "risk_level": "低"}\n```'
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])

    def test_invalid_json_empty_string(self):
        """空字符串"""
        response = ""
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])

    def test_invalid_json_whitespace_only(self):
        """只有空白字符"""
        response = "   \t\n  "
        result = parse_json_response(response)
        self.assertFalse(result["success"])
        self.assertIsNone(result["data"])


if __name__ == "__main__":
    unittest.main()

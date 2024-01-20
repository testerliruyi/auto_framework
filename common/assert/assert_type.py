"""
func: assert 方法
"""

from common.common_test_api import logger

builtin_str = str
integer_type = (int,)


# 判断是否相等
def equals(check_value, expect_value):
    try:
        assert check_value == expect_value
        logger.info(f"【断言结果】is True,【实际结果】：{check_value}，【预期结果】：{expect_value}")
    except Exception as e:
        logger.error(f"【断言结果】is False,【实际结果】：{check_value}，【预期结果】：{expect_value}")
        raise AssertionError("断言结果为失败")


# 判断实际结果小于预期结果
def less_than(check_value, expect_value):
    try:
        assert check_value < expect_value
        logger.info(f"【断言结果】is True,【实际结果】：{check_value}，【预期结果】：{expect_value}")
    except Exception as e:
        logger.error(f"【断言结果】 is False，【实际结果】：{check_value}，【预期结果】：{expect_value}")
        raise AssertionError("断言结果为失败")


def less_than_or_equals(check_value, expect_value):
    try:
        assert check_value <= expect_value
        logger.info(f"【断言结果】is True,【实际结果】：{check_value}，【预期结果】：{expect_value}")
    except Exception as e:
        logger.error(f"【断言结果】 is False,【实际结果】：{check_value}，【预期结果】：{expect_value}")


# 判断实际结果大于预期结果
def greater_than(check_value, expect_value):
    try:
        assert check_value > expect_value
        logger.info(f"【断言结果】is True,【实际结果】：{check_value}，【预期结果】：{expect_value}")
    except Exception as e:
        logger.error(f"【断言结果】 is False，【实际结果】：{check_value}，【预期结果】：{expect_value}")
        raise AssertionError("断言结果为失败")

# 判断实际结果大于等于预期结果
def greater_than_or_equals(check_value, expect_value):
    try:
        assert check_value >= expect_value
        logger.info(f"【断言结果】is True,【实际结果】：{check_value}，【预期结果】：{expect_value}")
    except Exception as e:
        logger.error(f"【断言结果】 is False,【实际结果】：{check_value}，【预期结果】：{expect_value}")


# 判断实际结果不相等
def not_equals(check_value, expect_value):
    try:
        assert check_value != expect_value
        logger.info(f"【断言结果】is True,【实际结果】：{check_value}，【预期结果】：{expect_value}")
    except Exception as e:
        logger.error(f"【断言结果】 is False,【实际结果】：{check_value}，【预期结果】：{expect_value}")


# 判断实际结果包含在预期结果里
def contains(check_value, expect_value):
    try:
        assert check_value in expect_value
        logger.info(f"【断言结果】is True,【实际结果】：{check_value}，【预期结果】：{expect_value}")
    except Exception as e:
        logger.error(f"【断言结果】 is False,【实际结果】：{check_value}，【预期结果】：{expect_value}")



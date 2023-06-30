import functools
import json

from funkagent.parser import func_to_json


def func_with_no_params():
    """
    This function has no parameters
    :return:
    """
    return 1


def func_with_mandatory_params_single_space_doc(a: str, b: str):
    """
    This function has mandatory parameters
    :param a:
    :param b:
    :return:
    """
    return 1


def func_with_optional_params_single_space_doc(a: str, b: str = "b"):
    """
    This function has optional parameters
    :param a:
    :param b:
    :return:
    """
    return 1


def func_with_mandatory_params_double_space_doc(a: str, b: str):
    """
    This function has mandatory parameters

    :param a:
    :param b:
    :return:
    """
    return 1


def func_with_optional_params_double_space_doc(a: str, b: str = "b"):
    """
    This function has optional parameters

    :param a:
    :param b:
    :return:
    """
    return 1


def test_func_to_json_func_with_no_params():
    """
    This function tests func_to_json with a function that has no parameters
    :return:
    """
    _json_fun = func_to_json(func_with_no_params)
    assert _json_fun["name"] == "func_with_no_params"
    assert _json_fun["description"] == "This function has no parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {}
    assert _json_fun["required"] == []


def test_func_to_json_func_with_mandatory_params_single_space_doc():
    """
    This function tests func_to_json with a function that has mandatory parameters and single space doc
    :return:
    """
    _json_fun = func_to_json(func_with_mandatory_params_single_space_doc)
    assert _json_fun["name"] == "func_with_mandatory_params_single_space_doc"
    assert _json_fun["description"] == "This function has mandatory parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "a": {
            "description": "",
            "type": "string"
        },
        "b": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == ["a", "b"]


def test_func_to_json_partial_func_with_mandatory_params_single_space_doc():
    """
    This function tests func_to_json with a function that has mandatory parameters and single space doc
    :return:
    """
    _json_fun = func_to_json(functools.partial(func_with_mandatory_params_single_space_doc, a="a"))
    assert _json_fun["name"] == "func_with_mandatory_params_single_space_doc"
    assert _json_fun["description"] == "This function has mandatory parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "b": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == ["b"]


def test_func_to_json_partialmethod_func_with_mandatory_params_single_space_doc():
    """
    This function tests func_to_json with a function that has mandatory parameters and single space doc
    :return:
    """
    _json_fun = func_to_json(functools.partialmethod(func_with_mandatory_params_single_space_doc, b="b"))
    assert _json_fun["name"] == "func_with_mandatory_params_single_space_doc"
    assert _json_fun["description"] == "This function has mandatory parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "a": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == ["a"]


def test_func_to_json_func_with_optional_params_single_space_doc():
    """
    This function tests func_to_json with a function that has optional parameters and single space doc
    :return:
    """
    _json_fun = func_to_json(func_with_optional_params_single_space_doc)
    assert _json_fun["name"] == "func_with_optional_params_single_space_doc"
    assert _json_fun["description"] == "This function has optional parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "a": {
            "description": "",
            "type": "string"
        },
        "b": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == ["a"]


def test_func_to_json_partial_func_with_optional_params_single_space_doc():
    """
    This function tests func_to_json with a function that has optional parameters and single space doc
    :return:
    """
    _json_fun = func_to_json(functools.partial(func_with_optional_params_single_space_doc, a="a"))
    print(_json_fun)
    assert _json_fun["name"] == "func_with_optional_params_single_space_doc"
    assert _json_fun["description"] == "This function has optional parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "b": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == []


def test_func_to_json_partial_func_with_optional_params_single_space_doc_positional():
    """
    This function tests func_to_json with a function that has optional parameters and single space doc
    :return:
    """
    _json_fun = func_to_json(functools.partial(func_with_optional_params_single_space_doc, "a"))
    print(_json_fun)
    assert _json_fun["name"] == "func_with_optional_params_single_space_doc"
    assert _json_fun["description"] == "This function has optional parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "b": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == []


def test_func_to_json_partialmethod_func_with_optional_params_single_space_doc():
    """
    This function tests func_to_json with a function that has optional parameters and single space doc
    :return:
    """
    _json_fun = func_to_json(functools.partialmethod(func_with_optional_params_single_space_doc, b="b"))
    assert _json_fun["name"] == "func_with_optional_params_single_space_doc"
    assert _json_fun["description"] == "This function has optional parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "a": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == ['a']


def test_func_to_json_func_with_mandatory_params_double_space_doc():
    """
    This function tests func_to_json with a function that has mandatory parameters and double space doc
    :return:
    """
    _json_fun = func_to_json(func_with_mandatory_params_double_space_doc)
    assert _json_fun["name"] == "func_with_mandatory_params_double_space_doc"
    assert _json_fun["description"] == "This function has mandatory parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "a": {
            "description": "",
            "type": "string"
        },
        "b": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == ["a", "b"]


def test_func_to_json_func_with_optional_params_double_space_doc():
    """
    This function tests func_to_json with a function that has optional parameters and double space doc
    :return:
    """
    _json_fun = func_to_json(func_with_optional_params_double_space_doc)
    assert _json_fun["name"] == "func_with_optional_params_double_space_doc"
    assert _json_fun["description"] == "This function has optional parameters"
    assert 'properties' in _json_fun["parameters"]
    assert 'type' in _json_fun["parameters"]
    assert _json_fun["parameters"]["type"] == "object"
    assert _json_fun["parameters"]["properties"] == {
        "a": {
            "description": "",
            "type": "string"
        },
        "b": {
            "description": "",
            "type": "string"
        }
    }
    assert _json_fun["required"] == ["a"]

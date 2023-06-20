import inspect
import re


def type_mapping(dtype):
    if dtype == float:
        return "number"
    elif dtype == int:
        return "integer"
    elif dtype == str:
        return "string"
    else:
        return "string"

def extract_params(doc_str: str):
    # parse the docstring to get the descriptions for each parameter in dict format
    params_str = doc_str.split("\n\n")[1].split("\n")
    params = {}
    for line in params_str:
        param_match = re.findall(r'(?<=:param )\w+(?=:)', line)
        if param_match != []:
            param_name = param_match[0]
            desc_match = line.replace(f":param {param_name}:", "").strip()
            params[param_name] = desc_match
    return params

def func_to_json(func):
    # first we get function name
    func_name = func.__name__
    # then we get the function annotations
    argspec = inspect.getfullargspec(func)
    # get the function docstring
    func_doc = inspect.getdoc(func)
    # parse the docstring to get the description
    func_description = func_doc.split("\n\n")[0]
    # get params
    params = argspec.annotations
    if 'return' in params.keys():
        del params['return']
    # parse the docstring to get the descriptions for each parameter in dict format
    param_details = extract_params(func_doc)
    # attach parameter types to params
    for param_name in argspec.args:
        params[param_name] = {
            "description": param_details.get(param_name) or "",
            "type": type_mapping(argspec.annotations[param_name])
        }
    # get parameters for function including default values (that are optional)
    len_optional_params = len(inspect.getfullargspec(func).defaults)
    # then return everything in dict
    return {
        "name": func_name,
        "description": func_description,
        "parameters": {
            "type": "object",
            "properties": params
        },
        "required": argspec.args[:len_optional_params]
    }
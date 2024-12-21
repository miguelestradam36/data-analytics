import pytest

def test_modules():
    """
    Python pytest
    ---
    Params: No arguments/parameters
    Objetive: Test modules into system or environment.
    """
    assert __import__('yaml')
    import yaml
    import os
    # Repeated values
    filepath = "../config/info.yaml"
    fullpath = os.path.join(os.path.dirname(__file__), filepath)

    with open(fullpath, 'r') as file:
        global yaml_config
        yaml_config = yaml.safe_load(file)
    
    for module in yaml_config["python"]["global"]["modules"]:
        assert __import__(module)
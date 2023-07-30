import os

# function to set environment variable in python
def set_environment_variable(name, value):
    os.environ[name] = value

def check_if_variable_exists(name):
    print(os.environ[name])
    if name in os.environ:
        print('Variable exists: ', name)
    else:
        print('Variable does not exist: ', name)


if __name__ == '__main__':
    check_if_variable_exists('OPENAI_API_KEY')
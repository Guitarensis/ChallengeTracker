import os

try:
    try:
        # Convert main_window.ui to Python code
        ui_file_name = 'main_window.ui'
        py_file_name = 'ui_main_window.py'
        print('convert ui files to py files')
    except Exception:
        raise ValueError(f'Errno: we got a problem no conversion took place')

    try:
        with open(py_file_name, 'w') as f:
            command = f"pyuic5 {ui_file_name} -o {py_file_name} -x"
            os.system(command)
            print('command to convert pushed')
    except Exception:
        raise ValueError(f'Errno: Some shit fucked up when command pushed to convert')

    try:
        # Convert settingsmenu.ui to Python code
        ui_file_name = 'settingsmenu.ui'
        py_file_name = 'ui_settingsmenu.py'
        print('converting settings')
    except Exception:
        raise ValueError(f'Errno: shit aint wanting to convert')

    try:
        with open(py_file_name, 'w') as f:
            command = f"pyuic5 {ui_file_name} -o {py_file_name} -x"
            os.system(command)
            print('converted settings')
    except Exception:
        raise ValueError(f'shit fuck damn nothing converted')

except Exception:
    raise ValueError(f'Welp something fucked up')
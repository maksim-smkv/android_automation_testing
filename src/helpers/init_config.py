from configparser import ConfigParser
from pathlib import Path
import os


class InitConfig:

    path_current_directory = os.path.dirname(__file__)
    proj_root_directory = Path(path_current_directory).parent.parent
    path_config_file = os.path.join(proj_root_directory, '', 'config.ini')
    config = ConfigParser()
    config.read(path_config_file, 'utf-8')

    userName = config.get('auth', 'userName')
    userPass = config.get('auth', 'userPass')
    userPhone = config.get('auth', 'userPhone')
    userSmsPass = config.get('auth', 'userSmsPass')
    officeShK = config.get('auth', 'officeShK')

    deviceName = config.get('capabilities', 'deviceName')
    app = config.get('capabilities', 'app')
    server = config.get('capabilities', 'server')

    fullUserName = config.get('menu', 'fullUserName')
    pvzName = config.get('menu', 'pvzName')

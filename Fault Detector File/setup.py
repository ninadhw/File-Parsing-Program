from cx_Freeze import setup,Executable

setup(name='convertmodule',
      version='0.1',
      description='extract current readings from gateway data',
      executables=[Executable('CurrentAlarmParser.py', icon='icon1.ico')])

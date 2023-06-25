# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
os.environ['TCL_LIBRARY'] = r'C:\Users\HP\AppData\Local\Programs\Python\Python310\tcl\tcl8'
os.environ['TK_LIBRARY'] = r'C:\Users\HP\AppData\Local\Programs\Python\Python310\tcl\tcl8.6'

a = Analysis(['main.py'],
             pathex=[r'E:\Gopal Work\Python Basic To Advance Projects\Library Management System\main.py'],
             binaries=[],
             datas=[('style.qss', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          [],
          name='Library Management System',
          icon=r'E:\Gopal Work\Python Basic To Advance Projects\Library Management System\lms.ico',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          upx_include=[],
          runtime_tmpdir=None,
          console=False )

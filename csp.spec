# -*- mode: python -*-

block_cipher = None


a = Analysis(['Code\\main.py'],
             pathex=['Code\\'],
             binaries=[],
             datas=[],
             hiddenimports=['Code\\Ui\\MainWindow.py', 'tkinter.filedialog'],
             hookspath=['Code\\Ui'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='csp',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False)

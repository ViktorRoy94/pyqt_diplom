# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[''],
             binaries=[],
             datas=[],
             hiddenimports=['MainWindow.py', 'tkinter.filedialog'],
             hookspath=[''],
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

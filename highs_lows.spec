# -*- mode: python -*-

block_cipher = None


a = Analysis(['highs_lows.py'],
             pathex=['C:\\Users\\admin\\AppData\\Local\\Microsoft\\OneDrive\\17.3.7074.1023', 'C:\\Users\\admin\\Documents\\Files\\ITL\\Python\\python_work\\mpl'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          name='highs_lows',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

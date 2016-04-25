# -*- mode: python -*-

block_cipher = None


a = Analysis(['stabilizer'],
             pathex=['/home/samuel/git/nlsam/scripts'],
             binaries=None,
             datas=None,
             hiddenimports=['scipy.special._ufuncs_cxx',
                            'scipy.linalg.cython_blas',
                            'scipy.linalg.cython_lapack',
                            'scipy.integrate',
                            'cython_gsl',
                            'scipy.special',
                            'scipy.integrate.quadrature',
                            'scipy.integrate.odepack',
                            'scipy.integrate._odepack',
                            'scipy.integrate.quadpack',
                            'scipy.integrate._quadpack',
                            'scipy.integrate._ode',
                            'scipy.integrate.vode',
                            'scipy.integrate._dop',
                            'scipy.integrate.lsoda'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.binaries = [x for x in a.binaries if not x[0].startswith("IPython")]
a.binaries = [x for x in a.binaries if not x[0].startswith("zmq")]
a.binaries = [x for x in a.binaries if not x[0].startswith("PIL")]
a.binaries = [x for x in a.binaries if not x[0].startswith("tcl")]
a.binaries = [x for x in a.binaries if not x[0].startswith("tk")]
a.binaries = [x for x in a.binaries if not x[0].startswith("matplotlib")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='stabilizer',
          debug=False,
          strip=False,
          upx=True,
          console=True )

# --------------------------------- [edit] ---------------------------------- #
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf1E\x1d\x9e\x80\xc4\x9b8\x18\xab\xce\xb1\xbaV\xe0\x14'
# --------------------------------------------------------------------------- #
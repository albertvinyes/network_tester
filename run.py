from app import app
from app import config

app.debug = True
app.run(host='0.0.0.0', port=config.PORT)

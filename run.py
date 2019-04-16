# run the web

from app.__init__ import app

if __name__ == '__main__':
	app.debug = True
	app.run()

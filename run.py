from questionario.__init__ import create_app


init_app = create_app()

if __name__ == '__main__':
    init_app.run(debug=True)

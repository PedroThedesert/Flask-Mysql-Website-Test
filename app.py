from flask import Flask

app = Flask(__name__)


@app.route('/<Home>')
def index(Home):
    return '<h1>This is the start of this website auto, folks!</h1>' .format(Home)

@app.route('/<Help>')
def Help (Help):
    return '<h1>Second part {}! </h1>' .format(Help)


@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>Data Processing</h1>
                </br>
                </br>
                <p> Insert your CSV file and then download the Result
          s      <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" class="btn btn-block"/>
                    </br>
                    </br>
                    <button type="submit" class="btn btn-primary btn-block btn-large">Pocess</button>
                </form>
            </body>
        </html>
    """

if __name__ == 'app': # reload auto
    print ("debug mode On")
    app.run(debug=True)
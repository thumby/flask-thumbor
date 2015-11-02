# flask-thumbor
Flask utilities to use thumbor images.

## Installing

Instaling flask-thumbor is as easy as:

    $ pip install flask-thumbor

## Initializing

In order to use flask-thumbor you must ensure that two configuration variables are present in your flask app configuration:

    THUMBOR_SERVER - Must be the URL for the thumbor server your image
                     will come from. i.e.: http://myuser.thm.la/
    THUMBOR_KEY - Security key that libthumbor will use to generate your image URLs

After having configured those two, you must initialize flask-thumbor. When initializing your app:

    from flask_thumbor import FlaskThumbor

    app = Flask(__name__)

    # load configuration from somewhere

    thumbor = FlaskThumbor(app)

Or if you want to initialize later:

    app = Flask(__name__)
    thumbor = FlaskThumbor()

    def main():
        # load configuration from somewhere
        thumbor.init_app(app)

## Usage

Using it in your templates is very simple:

    <img src="{{ thumbor(
            width=300, height=200, smart=True,
            image_url="http://my.com/img.jpg")
        }}" />

Any of the options supported by [libthumbor](https://github.com/thumbor/libthumbor) are available.

## License

This project is MIT licensed.

## Contributing

Fork, commit, pull request. Rinse and repeat.

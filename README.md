# FeedLeap: RSS feeds that leap into Kippt

FeedLeap lets you subscribe to your favorite RSS feeds and store new entries as Clips
in any Kippt List you want.  Clips are stored with a url, title, and a summary.

You try out the official hosted one at [http://feedleap.com](http://feedleap.com).


## About
This is a pretty simple web app that lets Kippt users subscribe to RSS feeds and store
new entries as Clips in the List they choose. When a user subscribes to a feed we listen
to updates from Superfeedr and add them to the List they chose.


## Running locally
    $ git clone git@github.com:jpadilla/feedleap.git
    $ cd feedleap
    $ pip install -r requirements.txt
    $ cp sample.env .env
    $ ./manage.py syncdb
    $ ./manage.py migrate
    $ ./manage.py runserver_plus

You have to set your domain and [Superfeedr](http://superfeedr.com/) credentials in the `.env` file.
To test locally you'll need to setup a reverse shell or have a domain that is accessible from an
external request where Superfeedr will verify your subscription callback before notifying of any
updated feed entries.


### Subscriptions management command
Included is a convenience management command to subscribe to one or more topic URLs.
You can also unsubscribe by passing the `--unsubscribe` option.

    $ ./manage.py subscriptions http://push-pub.appspot.com/feed


## License
Licensed under the MIT License.


## Thanks
Thanks to [@jorde](https://github.com/jorde) and [@ksaa](https://github.com/ksaa) from
[Kippt](http:om) for their awesome feedback, support and simple [API](https://kippt.com/developers/).


## Issues
Please use the [Github issue tracker](https://github.com/jpadilla/feedleap/issues) for any bug reports or feature requests.

## To-do
* OPML importer
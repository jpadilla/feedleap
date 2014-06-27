**Update: I'm officially shutting down the hosted version of FeedLeap for a couple of reasons. It was currently giving too much problems, and with no time to pick this up, all subscriptions on Superfeedr have been deleted. So no new entries will be showing up on Kippt. Also, Kippt won't probably be receiving any attention after they announced their [Next Chapter](http://blog.kippt.com/next-chapter/). I'll turn off the app on July 15th to allow anyone to retrieve their subscriptions manually from their dashboard. Thanks to everyone who helped this project live until now, especially [Jori Lallo](https://github.com/jorilallo), [Karri Saarinen](https://github.com/ksaa) and [Julien Genestoux](https://github.com/julien51).**

# FeedLeap: RSS feeds that leap into Kippt

FeedLeap lets you subscribe to your favorite RSS feeds and store new entries as Clips
in any Kippt List you want.  Clips are stored with a url, title, and a summary.


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
[Kippt](https://kippt.com/) for their awesome feedback, support and simple [API](https://kippt.com/developers/).

Thanks to [Julien Genestoux](https://github.com/julien51) and everyone at Superfeedr for powering our official demo.

![Powered by Superfeedr](https://feedleap.herokuapp.com/static/images/superfeedr-logo.png)


## Issues
Please use the [Github issue tracker](https://github.com/jpadilla/feedleap/issues) for any bug reports or feature requests.

## To-do
* OPML importer

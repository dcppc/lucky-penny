# lucky-penny

Lucky Penny is the Data Commons Twitter bot.
It tweets under the handle [`@nih_dcppc`](https://twitter.com/nih_dcppc).

This repo contains scriptsfor running the Data Commons
Twitter bot using
[rainbow-mind-machine](https://github.com/rainbow-mind-machine/rainbow-mind-machine),
the extensible framework for Twitter bot flocks.

## The Setup

To run a Twitter bot, you first need a Twitter OAuth application at
[apps.twitter.com](https://apps.twitter.com).

See the [rainbow-mind-machine
documentation](https://pages.charlesreid1.com/rainbow-mind-machine)
for details about setting up a Twitter OAuth app.

You will need a Consumer Token and a Consumer Secret Token.
Put these into `apikeys.json` in the form:

**`apikeys.json`**:

```
{
    "consumer_token" : "AAAAA",
    "consumer_token_secret" : "BBBBB"
}
```

## The Script

To run the Lucky Penny Twitter bot, use the provided
`LuckyPenny.py` script.

The script has three methods:

* `setup()` - performs authentication with the Twitter account
    that Lucky Penny will be using. **This step must be run once
    to create a bot key. This step is interactive.**

* `shepherd()` - creates a Shepherd for the Twitter flock
    and a Sheep for the DCPPC Twitter account. **This only creates
    the Shepherd (and the Sheep), it does not do anything with them.**

* `favorite()` - continuously searches for tweets containing a given
    hashtag and favorites them. The user can specify whether the bot should
    follow each user it retweets, how many tweets it looks at in each cycle,
    and how often it should look for new tweets.

    **NOTE:** If a bot has already favorited a tweet or followed a user and it
    tries to do so again, nothing will happen.

## Quick Start

Quick start instructions:

* Create your Twitter OAuth app
* Put your consumer token and consumer secret token in `apikeys.json`
* Run `LuckyPenny.py`, which will create a bot key interactively
* Run `LuckyPenny.py` again, which will run the `favorite()` method forever

You can run this anywhere you want, but you can run it on an ASWS node
(current approach) or as a Heroku app (in progress).

That's all there is to it!



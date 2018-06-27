import os
import rainbowmindmachine as rmm

def main():
    if not os.path.exists('apikeys.json'):
        # Need to create a Twitter app
        err = "\n\n\nERROR: You must add your consumer token and consumer secret token to apikeys.json\n\n"
        raise Exception(err)
    elif not os.path.exists('keys/lucky_penny.json'):
        # Need to set up the bot key
        setup()
    else:
        # We have a bot key, so do the dang thing
        favorite()

def setup():
    k = rmm.TwitterKeymaker()

    # This will look for OAuth app keys in apikeys.json
    # These are OAuth app credentials only, no bots.
    k.set_apikeys_file('apikeys.json')

    # This will create a bot key in lucky_penny.json
    # containing the credentials for the bot.
    k.make_a_key(
            name = 'lucky penny',
            json_target = 'lucky_penny.json',
            keys_out_dir = 'keys'
    )

def shepherd():
    # Create a shepherd using the bot keys 
    # created by the TwitterKeymaker above.
    sh = rmm.TwitterShepherd( 
            json_keys_dir = 'keys/',
            flock_name = 'lucky penny flock',
            sheep_class = rmm.SocialSheep
    )
    return sh

def favorite():
    # Get a flock object
    sh = shepherd()

    # Perform the "favorite" action
    sh.perform_parallel_action(
            'favorite',
            sleep = 60,
            capacity = 20,
            search_term = '#dcppc_test',
            follow = True
    )

if __name__=="__main__":
    main()

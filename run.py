import traceback

from xbot import XBot_SingleTweet


def mainFunction():
    # Single tweet scraper :
    url = "https://x.com/SpaceX/status/1875218268857958468"
    xBot1 = XBot_SingleTweet(url, headlessBool=True)
    xBot1.shutdown()

if __name__ == "__main__":
    try:
        mainFunction()
    except Exception:
        print(traceback.format_exc())
    exit(0)  # Return success code.

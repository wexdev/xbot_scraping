import time
import traceback
import threading

from bot import Bot


class XBot(Bot):
    def __init__(self, headlessBool=True):
        super().__init__(headlessBool)

    # Return the formatted number (nb. of views, likes, reposts...).
    def formatTweetNb(self, stringNb):
        if("K" in stringNb):
            n = float(stringNb.replace("K", ""))
            return str(int(n*1000))
        elif("M" in stringNb):
            n = float(stringNb.replace("M", ""))
            return str(int(n*1000000))
        return str(int(stringNb.replace(",", "").replace(".", "")))

# Scrap single tweets.
class XBot_SingleTweet(XBot):
    def __init__(self, url, headlessBool=True):
        super().__init__(headlessBool)
        self._url = url        
        self.run()

    def getTweetStats(self):
        time.sleep(2)

        nbViews, nbReposts, nbLikes = "", "", ""

        nbViews = self.getFromElement(Bot.TEXT, '//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[4]/div/div[1]/div/div[3]/span/div/span/span/span', 0)
        nbViews = self.formatTweetNb(nbViews)
        
        nbReposts = self.getFromElement(Bot.TEXT, '//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/button/div/div[2]/span/span/span', 0)
        nbReposts = self.formatTweetNb(nbReposts)

        nbLikes = self.getFromElement(Bot.TEXT, '//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[3]/button/div/div[2]/span/span/span', 0)
        nbLikes = self.formatTweetNb(nbLikes)

        print("nbViews     : " + nbViews)        
        print("nbReposts   : " + nbReposts)
        print("nbLikes     : " + nbLikes)

    def getProfileInfo(self):
        self.performOnElement(Bot.CLICK, '//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/div/div[1]/span/span', 2, "")

        nbFollowing = self.getFromElement(Bot.TEXT, '//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span', 0)
        nbFollowing = self.formatTweetNb(nbFollowing)

        nbFollowers = self.getFromElement(Bot.TEXT, '//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span', 0)
        nbFollowers = self.formatTweetNb(nbFollowers)

        print("nbFollowing : " + nbFollowing)
        print("nbFollowers : " + nbFollowers)

    # Scrap a single tweet data.
    def scraperWorker(self):
        print("url : " + self._url)
        self._driver.get(self._url)
        time.sleep(5)
        try:
            self.getTweetStats()
            self.getProfileInfo()
        except Exception:
            print("ERROR :\n", traceback.format_exc())
        time.sleep(5)

    def runScraper(self):
        t1 = threading.Thread(target=self.scraperWorker)
        self._threadsPool.append(t1)
        t1.start()

    def run(self):
        self.runScraper()

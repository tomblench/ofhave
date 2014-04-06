import re
import logging
from errbot import BotPlugin


class ofhave(BotPlugin):
    patt = re.compile("(I|you|they|we|he|she|it)\s+(could|couldn't|should|shouldn't|would|wouldn't|won't|will not|can't|cannot|can not)(\s+have|'ve)\s+([^-.;,]*)", re.I) # noqa

    def callback_message(self, conn, mess):
        reply = self.couldShould(mess.getBody())
        if reply:
            self.send(
                mess.getFrom(),
                reply,
                message_type=mess.getType()
            )

    def couldShould(self, sentence):
        logging.info(sentence)
        pronMap = {"i": "you",
                   "you": "you",
                   "they": "they",
                   "we": "you",
                   "he": "he",
                   "she": "she",
                   "it": "it"}
        # (could should would won't can't)
        m = self.patt.search(sentence)
        logging.info(m)
        if (m):
            return ("%s %s of %s!" % (
                pronMap[m.group(1).lower()],
                m.group(2),
                m.group(4))
            )
        return None

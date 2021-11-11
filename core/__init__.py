from dotenv import load_dotenv
import os

load_dotenv()
env = os.environ

BOT_KEY = env.get('BOT_KEY')

DEBUG = env.get('DEBUG')
GREETING_MESSAGE = 'Hello! My name is LinksKeeper bot. ' \
                   'I\'ve been created to keep your links and associate them with your custom shortcuts. ' \
                   'I promise that all of your links will be protected. Let\'s start working together! '

print(BOT_KEY)

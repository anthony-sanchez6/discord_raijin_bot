import logging
from bot import run_bot

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.NOTSET)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.NOTSET)
    logFormatter = logging.Formatter(fmt=' %(name)s :: %(levelname)s :: %(message)s')
    stream_handler.setFormatter(logFormatter)

    logger.addHandler(stream_handler)
    # run the bot
    logger.info('Bot is running!')
    run_bot()

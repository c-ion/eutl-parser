import traceback
import sys

class Logger:
    @staticmethod
    def LogError(msg):
        print("ERROR: ", msg)

    @staticmethod
    def LogInfo(msg):
        print("INFO: ", msg)

    @staticmethod
    def LogException(msg, ex):
        print("ERROR: {0}: {1}".format(msg, ex))

    @staticmethod
    def LogExceptionTrace(msg, ex):
        print("ERROR: ", msg)
        print('-'*60)
        traceback.print_exc(file=sys.stdout)
        print('-'*60)

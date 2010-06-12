""" Test processing class """
import logging

class test_processor:
    def __init__(self, consumer):
        self.consumer = consumer
    
    def process(self, message):
        
        logging.debug('In test_processor.test: %s' % message.body)
        return True
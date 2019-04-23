import unittest

import sys
sys.path.append("../")

from core.TransE import TransE
from core.TransH import TransH
from core.TransR import TransR
from core.ConvE import ConvE
from core.ProjE_pointwise import ProjE_pointwise
from config.config import ConvEConfig, TransEConfig, TransHConfig, TransHConfig, TransRConfig, ProjE_pointwiseConfig
from utils.dataprep import DataPrep
from utils.trainer import Trainer

import tensorflow as tf

class Pykg2vecTestCase(unittest.TestCase):
    
    def setUp(self):
        print('setup')
        self.data_handler = DataPrep("Freebase15k")

    def test_transE(self):
        
        config = TransEConfig(learning_rate=0.01, batch_size=512, epochs=1, hidden_size=16)

        config.test_step = 1
        config.test_num  = 10
        config.gpu_fraction = 0.4
        config.save_model = False
        config.disp_result= False

        model = TransE(config, self.data_handler)
        
        trainer = Trainer(model=model)
        trainer.build_model()
        trainer.train_model()
    
    def test_transH(self):

        config = TransHConfig(learning_rate=0.01, batch_size=512, epochs=1, hidden_size=16)

        config.test_step = 1
        config.test_num  = 10
        config.gpu_fraction = 0.4
        config.save_model = False
        config.disp_result= False
        config.C = 0.125

        model = TransH(config, self.data_handler)
        
        trainer = Trainer(model=model)
        trainer.build_model()
        trainer.train_model()

    def test_transR(self):

        config = TransRConfig(learning_rate=0.01, batch_size=512, epochs=1, 
                              ent_hidden_size=8, rel_hidden_size=4)

        config.test_step = 1
        config.test_num  = 10
        config.gpu_fraction = 0.4
        config.save_model = False
        config.disp_result= False


        model = TransR(config, self.data_handler)
        
        trainer = Trainer(model=model)
        trainer.build_model()
        trainer.train_model()

    def test_ConvE(self):

        config = ConvEConfig(learning_rate=0.01, batch_size=512, epochs=1)

        config.test_step = 1
        config.test_num  = 10
        config.gpu_fraction = 0.4
        config.save_model = False
        config.disp_result= False


        model = ConvE(config, self.data_handler)
        
        trainer = Trainer(model=model, algo=True, debug=False)
        trainer.build_model()
        trainer.train_model()

    def test_ProjE(self):

        config = ProjE_pointwiseConfig(learning_rate=0.01, batch_size=512, epochs=1)

        config.test_step = 1
        config.test_num  = 10
        config.gpu_fraction = 0.4
        config.save_model = False
        config.disp_result= False


        model = ProjE_pointwise(config, self.data_handler)
        
        trainer = Trainer(model=model, algo=True, debug=False)
        trainer.build_model()
        trainer.train_model()

    def tearDown(self):
        print('teardown')
        tf.reset_default_graph()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Pykg2vecTestCase('test_transE'))
    suite.addTest(Pykg2vecTestCase('test_transH'))
    suite.addTest(Pykg2vecTestCase('test_transR'))
    suite.addTest(Pykg2vecTestCase('test_ConvE'))
    return suite

if __name__ == '__main__':
    """ Execute whole test case as a whole """
    runner = unittest.TextTestRunner()
    runner.run(suite())
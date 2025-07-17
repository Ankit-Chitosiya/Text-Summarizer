from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.Model_training import ModelTrainer
from TextSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        trainer = ModelTrainer(config=model_trainer_config)
        trainer.train()


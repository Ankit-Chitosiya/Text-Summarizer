import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.entity import ModelTrainerConfig
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"


        import gc
        torch.cuda.empty_cache()
        gc.collect()
        

        model_ckpt = self.config.model_ckpt
        tokenizer = AutoTokenizer.from_pretrained(model_ckpt, use_fast=True)
        model_ = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt).to(device)

        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # trainer_args = TrainingArguments(
        #     output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
        #     per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
        #     weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
        #     evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
        #     gradient_accumulation_steps=self.config.gradient_accumulation_steps
        # ) 


        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            eval_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        ) 

        train_dataset = dataset_samsum_pt["train"].select(range(2000))
        eval_dataset = dataset_samsum_pt["validation"].select(range(100))
        
        os.environ["WANDB_MODE"] = "disabled"

        trainer = Trainer(
            model=model_,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset
        )

        
        trainer.train()

        # After training, saving the model and tokenizer in artifacts
        model_path = os.path.join(self.config.root_dir, "model")
        model_.save_pretrained(model_path)
        tokenizer_path = os.path.join(self.config.root_dir, "tokenizer")
        tokenizer.save_pretrained(tokenizer_path)

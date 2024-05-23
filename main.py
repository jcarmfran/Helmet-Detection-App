from src.helmet.pipeline.train_pipeline import TrainPipeline

def main():
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()
    print("success")
    

if __name__=="__main__":
    main()
# Fine-tuning Text Summarizer 

## Workflow

1. Update files under config folder:
   - config.yaml
   - models.py
   - helper.py

2. Update files under textSummarizer folder:
   - helper.py
   - pipeline.py

3. Update params.yaml 
4. Update main.py
5. Update main_fastapi.py


## Steps to get started with the project

1 - Clone the repository in directory of your choice:
```bash
git clone https://github.com/di37/text-summarizer-project.git
```
2 - Create conda environment:
```bash
conda create -n summary python=3.10 -y
```
3 - Activate environment:
```bash
conda activate summary
```
4 - In the `requirements.txt` file, include the required following libraries.

5 - Install the libraries:
```bash
pip install -r requirements.txt
```

6 - To retain the environment:
```bash
conda env export --no-builds > environment.yml
```

Next time, to work with this repo in a different system, we can just run the following command:
```bash
conda env create -f environment.yml
```
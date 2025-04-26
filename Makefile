install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

format:
	black *.py

train:
	python train.py

eval:
	echo "## Model Metrics" > report.md 
	cat Result/metrics.txt >> report.md

	echo '\n## Confusion Matrix Plot' >> report.md
	echo '![Confusion Matrix](Result/model_results.png)' >> report.md

	cml comment create report.md

update-branch:
	git config --global user.name $(USER_NAME)
	git config --global user.email $(USER_EMAIL)
	git commit -am "Update with new results"
	git push --force origin HEAD:update

hf-login:
	git pull origin update
	git switch update
	pip install -U "huggingface_hub[cli]"
	huggingface-cli login --token $(HF)

push-hub:
	huggingface-cli upload Deva2149/Drug-classification2 ./App --repo-type=space --commit-message="Sync App files"
	huggingface-cli upload Deva2149/Drug-classification2 ./Model /Model --repo-type=space --commit-message="Sync Model"
	huggingface-cli upload Deva2149/Drug-classification2 ./Result /Metrics --repo-type=space --commit-message="Sync Metrics"

deploy: hf-login push-hub

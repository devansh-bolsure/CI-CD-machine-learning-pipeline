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
	git stash
	git pull origin main --rebase
	git stash pop
	git config user.name "$(USER_NAME)"
	git config user.email "$(USER_EMAIL)"



install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

format:
	black *.py

train:
	python train.py

eval:
	echo "## Model Metrics" > report.md 
	cat "C:\\Users\\DEVANSH BOLSURE\\Dropbox\\My PC (LAPTOP-9PET8DJR)\\Documents\\anime\\MOVIES\\python_practice\\for_job\\ci_cd_project\\Result\\metrics.txt" >> report.md

	echo '\n## Confusion Matrix Plot' >> report.md
	echo '![Confusion Matrix](C:\\Users\\DEVANSH BOLSURE\\Dropbox\\My PC (LAPTOP-9PET8DJR)\\Documents\\anime\\MOVIES\\python_practice\\for_job\\ci_cd_project\\Result\\model_results.png)' >> report.md 

	cml comment create report.md


git commit -am 'new_changes'
git push origin main
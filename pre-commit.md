
conda install -c conda-forge pre-commit

Create the config.yaml
    pre-commit sample-config > .pre-commit-config.yaml

Run pre-commit install
(precommit) PS C:\Users\bmart\OneDrive\12_Data_Engineering\de-hotel-reviews> pre-commit install
output --> pre-commit installed at .git\hooks\pre-commit


git add .

git commit -m "hooks"

This will initialize the hooks

git status to see the modified files

git diff to see the modifications

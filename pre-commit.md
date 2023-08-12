# Pre-commit hooks

This file is a quick explanation of the pre-commit hooks

## Set up

- Install pre-commit:

    ```bash
    conda install -c conda-forge pre-commit
    ```

- Create the config.yaml and add the desired hooks:

    ```bash
    pre-commit sample-config > .pre-commit-config.yaml
    ```

- To create/install the hook run:

    ```bash
    pre-commit install
    ```

- Run the hooks by committing files that have not yet been commited:

    ```bash
    git add .

    git commit -m "hooks"
    ```

- To rull all files:

    ```bash
    pre-commit run --all-files
    ```
    
<p align="center">
<img align="center" width="970" height="180" src="../images/Pre Commit passed.png"> 
</p>

- Once all tests are passed commit all changes by-passing the hooks:

    ```bash
    git commit -m "All hooks passed" --no-verify
    ```

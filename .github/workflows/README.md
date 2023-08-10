# CI/CD Pipeline

The CI/CD Pipeline is configure for push/pull requests from the cicd branch. Feel free to change it. The following environment varibles must added in the GitHub secrets to make it run.

    ```bash
    GOOGLE_PROJECT_ID: ${{ secrets.GOOGLE_PROJECT_ID }}
    GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GOOGLE_APPLICATION_CREDENTIALS }}
    ```

The pipeline will run in GitHub Actions.

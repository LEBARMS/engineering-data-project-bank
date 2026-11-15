# Football Prediction MLOps & CI/CD

The objective of this project was to build an **end-to-end MLOps and CI/CD pipeline around football prediction models**.

Training a model is only one part of an operational machine-learning system. Data and model versions must remain reproducible, experiments must be traceable, changes in incoming data must be monitored, updated models must be evaluated, and the application must be tested and deployed consistently.

Football prediction provided the modelling use case for this team project; the main engineering work focused on the infrastructure required to manage the complete model lifecycle.

## What the pipeline does

The system connects the main stages of an operational machine-learning workflow:

1. **Version data and model artifacts** so a specific model can be associated with the data and outputs that produced it.
2. **Train and evaluate predictive models** while recording experiment information.
3. **Monitor feature distributions** to detect changes in incoming data.
4. **Conditionally retrain models** when the configured drift threshold is exceeded.
5. **Evaluate candidate models and select the champion** according to the model-selection criteria.
6. **Package the prediction API in Docker** so the same application can run consistently in CI and in the cloud.
7. **Validate the container during CI** before it is published.
8. **Publish the tested container image** to Google Artifact Registry.
9. **Deploy the prediction service** to Google Cloud Run.

![CI/CD and MLOps lifecycle from versioned artifacts through monitoring, retraining and Google Cloud deployment](assets/training-and-serving.png)

## Data and model versioning

**DVC** versions the processed datasets, trained model artifacts, evaluation reports and champion-model configuration.

The DVC remote is backed by **Google Cloud Storage**, allowing the CI/CD workflows to retrieve the model and data artifacts associated with the current repository state.

This separates large analytical artifacts from the Git repository while keeping them reproducible through versioned references.

## Experiment tracking

Training and monitoring code integrates **MLflow** to record experiment information and model metrics.

This provides a traceable history of training runs and supports model comparison independently from the application deployment layer.

## Drift monitoring and conditional retraining

A scheduled monitoring workflow compares current numerical features with reference data using two-sample **Kolmogorov–Smirnov tests**.

If more than the configured share of eligible numerical features is detected as drifting, the retraining logic reproduces the corresponding DVC pipeline stages.

The resulting model evaluation reports are compared to select the champion.

Champion selection prioritizes **macro-F1** and uses **accuracy** as a secondary criterion.

Updated analytical artifacts are then stored through the versioned DVC / Cloud Storage workflow.

## CI/CD and application deployment

The serving layer is implemented as a **FastAPI prediction API packaged in Docker**.

The deployment workflow performs the main CI/CD steps:

### Continuous integration

- retrieve the required versioned artifacts;
- build the Docker image;
- start the image inside the CI environment;
- verify that the FastAPI application successfully serves its `/docs` endpoint.

### Continuous deployment

- authenticate to Google Cloud;
- push the tested Docker image to **Google Artifact Registry**;
- deploy the image to **Google Cloud Run**.

The result is a reproducible path from analytical artifacts to a containerized prediction service running on managed cloud infrastructure.

The monitoring/retraining workflow and application-deployment workflow are implemented separately in GitHub Actions, but together they form the model lifecycle shown above.

A main-branch push or manual dispatch triggers the deployment workflow.

## Prediction service

The API exposes model predictions including goal regression, home/draw/away classification and lineup-based prediction, together with champion-model metadata.

A Streamlit interface was also developed around predictions, metrics and drift information.

The portfolio emphasis, however, is the **MLOps and CI/CD system surrounding the models**, rather than football prediction accuracy itself.

## Technical evidence

- [Feature-level drift detection](code/drift_monitor.py)
- [Conditional retraining and artifact updates](code/conditional_retraining.py)
- [Champion-model selection](code/champion_selection.py)
- [Container validation, image publication and Cloud Run deployment](code/deploy-excerpt.yml)

## Technologies

Python · XGBoost · SciPy · DVC · MLflow · FastAPI · Uvicorn · Docker · GitHub Actions · Google Cloud Storage · Google Artifact Registry · Google Cloud Run · Streamlit

## Sources

[Canonical project repository](https://github.com/TSM-MachLedata/MLOps) · [Technical evidence and provenance](../../docs/evidence-register.md#football-prediction-mlops--cicd)

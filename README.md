# explore-mlflow-model-deploy

Exploring the MLflow paradigm for model deployment.

> At this point I'm pretty experienced with MLflow, but I've never deployed MLflow models as a container.
> That's what we are trying to achieve today.

## Tutorial Links

The following are the links to the tutorials I used for this project:

1. [Deploy MLflow Model as a Local Inference Server](https://mlflow.org/docs/latest/deployment/deploy-model-locally/)
    1. [Getting Started with MLflow](https://mlflow.org/docs/latest/getting-started)
        1. [How to Run Tutorials](https://mlflow.org/docs/latest/getting-started/running-notebooks/) 

## Steps to reproducing this exercise

### Part 1: Model serve on local environment

#### Steps: 

1. Prepare the environment. I used [uv](), so you can simply `uv sync`.
1. Run mlflow with `uv run mlflow ui`, and now the mlflow file is accessible at [http://localhost:5000](http://localhost:5000).
1. Run [train.py](train.py) to materialize the MLflow model:
    ```
    uv run python train.py
    ```
1. You may validate the MLflow model with [validate.py](validate.py) - make sure to replace the run id:
    ```
    uv run python validate.py
    ```
1. Try serving the model (note that the port for this model server is `5001`):
    ```
    uv run mlflow models serve -m runs:/3a42592dd37b43f5ab73d87af8bc5fe1/iris_model --env-manager uv -p 5001
    ```
    Test the endpoint:
    ```
    curl http://127.0.0.1:5001/invocations -H "Content-Type:application/json"  --data '{"inputs": [[1,2,3,4]]}'
    ```

#### Note(s):

1. My main concern has always been about environment management. So this small model's environment is stored at [.mlflow/envs/mlflow-RUN_ID]() and the size of this file is `667M` (check with `du -h .mlflow/envs/mlflow-RUN_ID --max-depth 2`). In a current project I'm working on, we need to update models frequently, so I think going with the docker container approach will make environment management easier. 
1. Next, we will explore that alternative. 

### Part 2: Building a docker container for the model


## Notes

1. From [here](https://mlflow.org/docs/latest/getting-started/intro-quickstart#step-4---log-the-model-and-its-metadata-to-mlflow):
    - _It is best to keep the training execution outside of the run context block to ensure that the loggable content (parameters, metrics, artifacts, and the model) are fully materialized prior to logging._
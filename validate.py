import mlflow
from mlflow.models import Model

mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

model_uri = 'runs:/3a42592dd37b43f5ab73d87af8bc5fe1/iris_model'
# The model is logged with an input example
pyfunc_model = mlflow.pyfunc.load_model(model_uri)
input_data = pyfunc_model.input_example

# Verify the model with the provided input data using the logged dependencies.
# For more details, refer to:
# https://mlflow.org/docs/latest/models.html#validate-models-before-deployment
mlflow.models.predict(
    model_uri=model_uri,
    input_data=input_data,
    env_manager="uv",
)
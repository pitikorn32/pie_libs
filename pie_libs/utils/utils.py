import json
import yaml
import csv
import base64
import logging


def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def save_yaml(file, name):
    with open(name, "w") as f:
        yaml.dump(file, stream=f, default_flow_style=False, sort_keys=False)


def load_yaml(name):
    with open(name) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def base64_to_file(filename, filedata):
    img_recovered = base64.b64decode(str.encode(filedata))  # convert string to bytes & decode base64string
    try:
        with open(filename, "wb") as f:
            f.write(img_recovered)
    except Exception:
        return {"message": "There was an error uploading the file"}


def file_to_base64(filepath):
    try:
        with open(filepath, "rb") as file:
            encoded_string = base64.b64encode(file.read())
            return encoded_string.decode("utf-8")  # Convert bytes to string for easier handling
    except Exception as e:
        return {"message": f"There was an error reading the file: {str(e)}"}


def create_logger(log_filename):

    # Clear previous handlers to avoid duplicate messages
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Set up the logger
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Create handlers for file and console
    file_handler = logging.FileHandler(log_filename)

    # Set formatters for the handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logging.getLogger().addHandler(file_handler)

    # Creating an object
    logger = logging.getLogger()

    return logger


def append_dataframe_to_csv(df, filepath):

    # Convert the DataFrame to a list of lists
    new_rows = df.values.tolist()

    # Open the CSV file in append mode
    with open(filepath, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write new rows to the CSV
        for row in new_rows:
            writer.writerow(row)


def get_variable_from_config(variable_name: str, config_script: dict, config: dict):
    if variable_name in config_script:
        return config_script[variable_name]
    elif variable_name in config:
        return config[variable_name]
    else:
        raise ValueError(f"Variable {variable_name} not found in config")

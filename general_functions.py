
def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)


def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)


# Read Object from File
def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


# Write Object to File
def write_to_pickle_file(filename, an_object):
    with open(filename, 'wb') as file:
        pickle.dump(an_object, file)


def createTimeStampedFolder(path):
    import os
    import subprocess
    from datetime import datetime

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    mydir = os.path.join(path, timestamp)
    os.makedirs(mydir, exist_ok=True)
    subprocess.run(['open', mydir], check=True)


def createShapPlot(model, X_dataset):
    import shap
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_dataset)

    return shap.summary_plot(shap_values,
                             features=X_dataset,
                             feature_names=X_dataset.columns)

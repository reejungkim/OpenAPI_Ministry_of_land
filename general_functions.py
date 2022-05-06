
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


def createTimeStampedFolder(path):
    import os
    import subprocess
    from datetime import datetime

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    mydir = os.path.join(path, timestamp)
    os.makedirs(mydir, exist_ok=True)
    subprocess.run(['open', mydir], check=True)

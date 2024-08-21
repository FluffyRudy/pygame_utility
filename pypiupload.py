import subprocess
import shutil
import os


def upload_package():
    if not prompt_version_reminder():
        return

    try:
        clean_build()
        print("Uploading to pypi....")
        build_code = subprocess.run(
            ["python3", "-m", "setup.py", "sdist", "bdist_wheel"]
        )
        upload_code = subprocess.run(
            ["twine", "upload", "dist/*"], check=True, capture_output=True, text=True
        )
        if upload_code != 0:
            print("Unknown error: failed to upload to pypi")
        print(upload_code)

    except subprocess.TimeoutExpired:
        print("Error: Timeout")
    except subprocess.CalledProcessError:
        print("Error occured while uploading package to pypi")
    except Exception as error:
        print("Unknown error occured")


def clean_build():
    print("cleaning build...\n")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")


def prompt_version_reminder():
    if input("Did you update version?(y/n)") == "y":
        return True
    return False


if __name__ == "__main__":
    upload_package()

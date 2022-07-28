from pathlib import Path


def copy():
    """ This funcion only let you move files on one drive"""

    source_path = Path.joinpath(Path.home(), "AppData", "Local", "Packages",
                                "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy", "LocalState", "Assets")
    target_path = Path().cwd()
    new_suffix = ".jpg"
    for obj in source_path.iterdir():
        if obj.is_file():
            new_name = f"{obj.stem}{new_suffix}"
            print(new_name)
            obj.rename(target_path / new_name)


copy()

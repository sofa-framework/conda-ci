import yaml
import json
import sys

def keys_exists(element, *keys):
  '''
  Check if *keys (nested) exists in `element` (dict).
  '''
  if not isinstance(element, dict):
    raise AttributeError('keys_exists() expects dict as first argument.')
  if len(keys) == 0:
    raise AttributeError('keys_exists() expects at least two arguments, one given.')

  _element = element
  for key in keys:
    try:
      _element = _element[key]
    except KeyError:
      return False
  return True

# Usage: bump_build_number.py <recipe_file.yaml>
if __name__ == "__main__":
  recipe_file = sys.argv[1]

  # read recipe file
  with open(recipe_file, "r") as file:
    recipe = yaml.load(file, Loader=yaml.FullLoader)
    # look for context.build_num key first
    foundBuildNumber = False
    if keys_exists(recipe, "context", "build_num"):
      try:
        old_build_number = int(recipe["context"]["build_num"])
        new_build_number = old_build_number + 1
        print(json.dumps({"old_build_number": old_build_number,
                          "new_build_number": new_build_number,
                          "key": "context-build_num",
                          "status": "ok"}))
        old_str = "build_num: " + str(old_build_number)
        new_str = "build_num: " + str(new_build_number)
        foundBuildNumber = True
      except ValueError:
        print("Recipe ", recipe_file, " has context.build_num key, but value is not a number: ", recipe["context"]["build_num"], file=sys.stderr)
    # otherwise try build.number key
    if foundBuildNumber == False:
      if keys_exists(recipe, "build", "number"):
        try:
          old_build_number = int(recipe["build"]["number"])
          new_build_number = old_build_number + 1
          print(json.dumps({"old_build_number": old_build_number,
                            "new_build_number": new_build_number,
                            "key": "build-number",
                            "status": "ok"}))
          old_str = "number: " + str(old_build_number)
          new_str = "number: " + str(new_build_number)
          foundBuildNumber = True
        except ValueError:
          print("Recipe ", recipe_file, " has build.number key, but value is not a number: ", recipe["build"]["number"], file=sys.stderr)
    if foundBuildNumber == False:
        print("Recipe ", recipe_file, " has no valid build number field", file=sys.stderr)
        sys.exit(1)

  # Safely read the input filename using 'with'
  with open(recipe_file, "r") as file:
    file_str = file.read()
    if old_str not in file_str:
      print("Error: ", old_str, " not found in ", recipe_file, file=sys.stderr)
      sys.exit(1)

  # Safely write the changed content, if found in the file
  with open(recipe_file, "w") as file:
    new_file_str = file_str.replace(old_str, new_str)
    file.write(new_file_str)

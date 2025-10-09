import yaml
import sys

# Usage: filter_config.py <config_to_filter.yaml> <filter_file.yaml>
if __name__ == "__main__":
  config_filename = sys.argv[1]
  filter_file = sys.argv[2]
  print('config_filename = ', config_filename)
  print('filter_file = ', filter_file)

  # read config file to filter
  with open(config_filename, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

  # read filter.yaml
  with open(filter_file, "r") as file:
    filt = yaml.full_load(file)
    print('filt:', filt)

    # print("top-level attributes to be filtered config yaml: ", filt['filtered'])
    for l in filt['filtered']:
      print("filtering ", l, "...")
      config.pop(l, None)

  # output to file
  with open(config_filename, "w") as file:
    yaml.dump(config, file)

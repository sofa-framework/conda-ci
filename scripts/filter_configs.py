import yaml
import sys

# Usage: filter_config.py <filter_file.yaml> [<config_to_filter_1.yaml> ...]
if __name__ == "__main__":
  filter_file = sys.argv[1]
  config_files = sys.argv[2:]
  print('config_files = ', config_files)
  print('filter_file = ', filter_file)

  # read config file to filter
  for config_file in config_files:
    with open(config_file, "r") as file:
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
    with open(config_file, "w") as file:
      yaml.dump(config, file)

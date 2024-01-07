# Format for several templates per asset definition

```yaml
# ~/repo-path/src/asset-path/meta.yml
#
title: "Asset title"
disabled: false  # false by default
# ~/repo-path/src/asset-path/asset-name.hbs
#
template: "asset-name.hbs"

parts:
  - template: "part1-name.hbs"
    data_from: "part1-data.yml" # if omitted, parent's data used
    disabled: true              # perhaps, it should be possible too
  - template: "part2-name.hbs"
    data_from: "part2-data.yml"

# First variant to get data
data_from: "asset-data.yml"
# Second variant for cases when data is too small
data:
  author: "John Doe"
  year: 2024
paths:
  # Path to put build result
  #   inside asset repository root
  #
  build: "build/path/filename.cfg"
  # Path to link from
  #   inside home directory
  link: "link/path/filename.cfg"
```

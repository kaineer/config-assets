# Repository

```yaml
title: "Some repository"
disabled: false
# Repository source url
#
url: git@github.com:kaineer/repository-name.git
paths:
  # Where to clone repository (inside this repository)
  build: "git/repository-name"
  # Where to link repository dir
  link: "${env.home}/git/repository-name"
```

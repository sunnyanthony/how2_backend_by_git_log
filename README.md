![dockerbuild](https://github.com/sunnyanthony/how2_backend_by_git_log/actions/workflows/dev.yml/badge.svg)
# how2_backend_by_git_log
This repository is going to teach you how to build backend service from scratch

# install
- Docker
  * we'll use dockerfile to create container
- [kind](https://kind.sigs.k8s.io)
  * use local k8s to deploy our service
- Python3
  * yous should install python and setup everything

```python
K8s
+-------------------------------------------+
|Pod0                                       |
|+------------------------------------+     |
||+---------------------+  Container0 |     |
|||   Pythonic program  |             |     |
||+---------------------+             |     |
|+------------------------------------+     |
+-------------------------------------------+
```

## example
1. socket
    * [commit](https://github.com/sunnyanthony/how2_backend_by_git_log/commit/18b31bcc82d2706f3438ce75771326b8322322c7)
2. HTTP
    * [commit](https://github.com/sunnyanthony/how2_backend_by_git_log/commit/b7b329fbf690c76db9cfb42bd49311520e8d2af0)

# Framework
In this repo, I decide to use `Django` to be our web framework rather than **flask**. Actually, I never use it before, so I'm going to learn this framework with you.

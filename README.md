# how2_backend_by_git_log
This repository is going to teach you how to build backerend service from scratch

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

# Framework
In this repo, I decide to use `Django` to be our web framework rather than **flask**. Actually, I never use it before, so I'm going to learn this framework with you.

---
layout: page
title: "快速运行脚本"
permalink: /script/
---

* TOC
{:toc}

# NUSHPC
## volta login
- vaspstd
```
export OMP_NUM_THREADS=4
export CONTAINER_PATH=~/hpctmp/container/6.3.0/latest # change the directory to your sif container
export OMPI_MCA_hwloc_base_binding_policy=none

export OMP_STACK_SIZE=4096m
cp CONTCAR POSCAR

nohup singularity exec ${CONTAINER_PATH} mpirun -n 1 vasp_std >> vasp.out &
```
- vaspgam
```
export OMP_NUM_THREADS=4
export CONTAINER_PATH=~/hpctmp/container/6.3.0/latest # change the directory to your sif container
export OMPI_MCA_hwloc_base_binding_policy=none

export OMP_STACK_SIZE=4096m
cp CONTCAR POSCAR

nohup singularity exec ${CONTAINER_PATH} mpirun -n 1 vasp_gam >> vasp.out &
```

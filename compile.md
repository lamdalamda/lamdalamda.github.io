---
layout: page
title: "vasp编译"
permalink: /compile/
---


`#查询AMD编译器受教育程度#`

# vasp compilation

## intel parallel studio 2019:

- fornax
```
OFLAG      = -O3 -xCORE-AVX2 -fma -static
BLAS       =  $(MKLROOT)/lib/intel64/libmkl_scalapack_lp64.a -Wl,--start-group $(MKLROOT)/lib/intel64/libmkl_intel_lp64.a $(MKLROOT)/lib/intel64/libmkl_sequential.a $(MKLROOT)/lib/intel64/libmkl_core.a $(MKLROOT)/lib/intel64/libmkl_blacs_intelmpi_lp64.a -Wl,--end-group -lpthread -lm -ldl
```

## oneapi
Remember to change the path of fftw3xf!
```
OFLAG      = -O3 -xCORE-AVX2 -fma -static
OBJECTS    = fftmpiw.o fftmpi_map.o fft3dlib.o fftw3d.o  /opt/intel/oneAPI/2021.2/mkl/latest/interfaces/fftw3xf/libfftw3xf_intel.a
```

## aocc



# References

## intel mpi
- flags:
    - https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html
    - https://developer.amd.com/wordpress/media/2020/04/Compiler%20Options%20Quick%20Ref%20Guide%20for%20AMD%20EPYC%207xx2%20Series%20Processors.pdf
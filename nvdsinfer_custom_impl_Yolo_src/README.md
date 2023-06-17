## Derived from Marcos Luciano's project - https://github.com/marcoslucianops/DeepStream-Yolo 

### DeepStream 6.2 on x86 platform

`sudo CUDA_VER=11.8 make -C nvdsinfer_custom_impl_Yolo`

### DeepStream 6.1.1 on x86 platform

`sudo CUDA_VER=11.7 make -C nvdsinfer_custom_impl_Yolo`

### DeepStream 6.1 on x86 platform

`sudo CUDA_VER=11.6 make -C nvdsinfer_custom_impl_Yolo`

### DeepStream 6.0.1 / 6.0 on x86 platform

`sudo CUDA_VER=11.4 make -C nvdsinfer_custom_impl_Yolo`

### DeepStream 5.1 on x86 platform

`sudo CUDA_VER=11.1 make -C nvdsinfer_custom_impl_Yolo`

### DeepStream 6.2 / 6.1.1 / 6.1 on Jetson platform

`sudo CUDA_VER=11.4 make -C nvdsinfer_custom_impl_Yolo`

### DeepStream 6.0.1 / 6.0 / 5.1 on Jetson platform
A prebuilt library (.so) is provided for Jetson Nano (nvdsinfer_custom_impl_Yolo_bin/Jetson_Nano) and does not need to be built

`sudo CUDA_VER=10.2 make -C nvdsinfer_custom_impl_Yolo`


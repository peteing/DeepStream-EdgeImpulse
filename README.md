# DeepStream-EdgeImpulse

This guide takes you through the process of using Edge Impulse with DeepStream. You are able to build both object detectors and classifiers using Edge Impulse.

These custom models can be used to implement your own Intelligent Video Analytics pipelines and a typical use case is using the object detector for your primary stage (PGIE) Gst-nvinfer instance 
and the classifier for your second stage (SGIE) instance of Gst-nvinfer

Note that these config files can be used with any of the methods to build and create a DeepStream pipeline including Python and C++. The example shown works with
the prebuilt "deepstream-app" found in the samples provided with DeepStream

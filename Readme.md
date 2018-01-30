Example processing node for [HASTE](http://haste.research.it.uu.se) for use with the [HarmonicIO processing framework](https://github.com/HASTE-project/HarmonicIO)

**Only works inside a HarmonicIO container (see: https://github.com/HASTE-project/HarmonicPE)**

## Features
* Caching of storage clients for the HASTE Storage Platform.
* Auto-configuration of HASTE storage client.


## Build and Publish for use in HIO:
```
docker build -t "benblamey/haste-image-proc:latest" . ; docker push benblamey/haste-image-proc:latest
```

## ...with profiling enabled:
```
__enable_profiling = True
```

```
docker build -t "benblamey/haste-image-proc:latest-profiling" . ; docker push benblamey/haste-image-proc:latest-profiling
```

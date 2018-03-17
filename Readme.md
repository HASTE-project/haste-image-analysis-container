Example processing node for [HASTE](http://haste.research.it.uu.se) for use with the [HarmonicIO processing framework](https://github.com/HASTE-project/HarmonicIO)

**Only works inside a HarmonicIO container (see: https://github.com/HASTE-project/HarmonicPE)**

## Features
* Caching of storage clients for the HASTE Storage Platform.
* Auto-configuration of HASTE storage client.


## Build and Publish for use in HIO:
We use --no-cache because otherwise calls to 'git clone' get cached - rather than pulling latest code!

```
docker build --no-cache=true -t "benblamey/haste-image-proc:latest" . ; docker push benblamey/haste-image-proc:latest
```

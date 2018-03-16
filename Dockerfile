# HIO requires python 3.
FROM python:3.6.3

# Set the working directory to /app
WORKDIR /app

# Checkout and install Harmonic PE (latest):
RUN git clone https://github.com/HASTE-project/HarmonicPE.git;cd /app/HarmonicPE;git checkout master;pip3 install -e .

# Checkout and install the Haste Storage Client (specific version):
RUN git clone https://github.com/HASTE-project/HasteStorageClient.git;cd /app/HasteStorageClient;git checkout v0.8;pip3 install -e .

# Checkout and install the The Windowed Conformal Model (latest):
RUN git clone https://github.com/HASTE-project/windowed-conformal-model.git;cd /app/windowed-conformal-model;git checkout master;pip3 install -e .

# Install packages for image analysis
RUN pip3 install numpy
RUN pip3 install Pillow
RUN pip3 install scikit-image

# TODO investigate installing scikit-sparse here?
#RUN conda install -c conda-forge scikit-sparse

# Make port 80 available (required for the listening daemon)
EXPOSE 80



# Add the example srcipt (change this to your own:)
ADD haste_processing_node /app/haste_processing_node

# TODO: use setup.py for dependencies.

CMD ["python", "-m", "haste_processing_node.function"]

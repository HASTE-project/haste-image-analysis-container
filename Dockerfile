# HIO requires python 3.
FROM python:3.6.3

# Set the working directory to /app
WORKDIR /app

# Checkout and install Harmonic PE:
RUN git clone https://github.com/HASTE-project/HarmonicPE.git;cd /app/HarmonicPE;git checkout master;pip3 install -e .

# Checkout and install the Haste Storage Client:
RUN git clone https://github.com/HASTE-project/HasteStorageClient.git;cd /app/HasteStorageClient;git checkout v0.5;pip3 install -e .

# Install packages for image analysis
RUN pip3 install numpy
RUN pip3 install Pillow
RUN pip3 install scikit-image

# Make port 80 available (required for the listening daemon)
EXPOSE 80


# Add the example script (change this to your own:)
ADD haste_processing_node /app/haste_processing_node

# TODO: use setup.py for dependencies.

CMD ["python", "-m", "haste_processing_node.function"]

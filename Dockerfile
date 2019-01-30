# HIO requires python 3.
FROM python:3.6.3

# Set the working directory to /app
WORKDIR /app

# GOTCHA: git clone gets cached - use --no-cache !!

# Install dependendencies not on PyPI:

# Checkout and install Harmonic PE (latest):
RUN git clone https://github.com/HASTE-project/HarmonicPE.git;cd /app/HarmonicPE;git checkout master;pip3 install .

# Checkout and install the The Windowed Conformal Model (latest):
# This needs to use -e for the .npy files.
RUN git clone https://github.com/HASTE-project/windowed-conformal-model.git;cd /app/windowed-conformal-model;git checkout master;pip3 install -e .

# TODO investigate installing scikit-sparse here?
#RUN conda install -c conda-forge scikit-sparse


COPY haste_processing_node /app/haste_processing_node

# Install dependendencies from setup.py:

COPY setup.py /app/setup.py
RUN pip3 install /app

# Make port 80 available (required for the listening daemon)
EXPOSE 80

CMD ["python", "-m", "haste_processing_node.function"]

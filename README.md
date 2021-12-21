# Email Spam Detector

## Table of Contents

- [Dependencies](#markdown-header-dependencies)
- [How to setup](#markdown-header-how-to-setup)
- [Dataset](#markdown-header-dataset)

## Dependencies

- python 3 or above
- Anaconda (conda)
- Numpy
- Scikit-learn
- Keras (TensorFlow)

### <i>Note: This has not been tested, just an example. Will be further developed.</i>

## How to setup

## 1. Clone the repository

```bash
git clone https://github.com/km2795/spam-detector.git
```

## 2. Get inside the cloned repository

```bash
cd spam-detector
```

## 3. Checkout the master branch.

```bash
git checkout master
```

## 4. Install the project.

```bash
conda env create -f environment.yaml
```

## 5. Download and setup the datasets.

```bash
# Run it ONLY from the top level directory of the project.
sh setup_dataset.sh
```

## 6. Run the project.

```bash
python3 ./spam-detector/spam_detector.py
```

# Dataset

The following datasets have been used for the training and testing of the spam detector.

<https://spamassassin.apache.org/old/publiccorpus/>

DATASET_DIR=./spam-detector/dataset

# Create dataset directory.
mkdir -p $DATASET_DIR

# Download the datasets.
wget -c https://spamassassin.apache.org/old/publiccorpus/20030228_easy_ham.tar.bz2 -P $DATASET_DIR
wget -c https://spamassassin.apache.org/old/publiccorpus/20030228_easy_ham_2.tar.bz2 -P $DATASET_DIR
wget -c https://spamassassin.apache.org/old/publiccorpus/20030228_spam.tar.bz2 -P $DATASET_DIR
wget -c https://spamassassin.apache.org/old/publiccorpus/20050311_spam_2.tar.bz2 -P $DATASET_DIR
wget -c https://spamassassin.apache.org/old/publiccorpus/20030228_hard_ham.tar.bz2 -P $DATASET_DIR

# Extract the datasets.
tar -xf $DATASET_DIR/20030228_easy_ham.tar.bz2 -C $DATASET_DIR
tar -xf $DATASET_DIR/20030228_easy_ham_2.tar.bz2 -C $DATASET_DIR
tar -xf $DATASET_DIR/20030228_spam.tar.bz2 -C $DATASET_DIR
tar -xf $DATASET_DIR/20050311_spam_2.tar.bz2 -C $DATASET_DIR
tar -xf $DATASET_DIR/20030228_hard_ham.tar.bz2 -C $DATASET_DIR

# Remove datasets archives.
rm $DATASET_DIR/*.tar.bz2

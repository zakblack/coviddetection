# COVID-19 detector in X-ray scans using TensorFlow

Using TensorFlow, Keras and Python, I wrote this code for detection of COVID-19 patients.

**Disclaimer** : This code on automatic COVID-19 detection is for educational purposes only. It is _not_ meant to be a reliable, highly accurate COVID-19 diagnosis system, nor has it been professionally or academically vetted.
# Usage

You can start by downloading the dataset from [here](https://github.com/zakblack/coviddataset) then put it in a folder named "dataset" next to training scripts.
You can start the training by typing :

`$ python train.py --dataset dataset`

You can predict on an image using the Test script like the following :
<br>
`$ python test.py --image positif.jpeg --model covid.model` 

## Results

<br>
<a href="https://zakaria.tech/"><img src="https://i.ibb.co/gWdLhnY/stats2.png" alt="stats2" border="0"></a>

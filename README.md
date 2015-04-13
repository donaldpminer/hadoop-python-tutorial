# hadoop-python-tutorial
Exercises and examples developed for the Hadoop with Python tutorial


DESCRIPTION

In this tutorial, students will learn how to use Python with Apache Hadoop to store, process, and analyze incredibly large data sets. Hadoop has become the standard in distributed data processing, but has mostly required Java in the past. Today, there are a numerous open source projects that support Hadoop in Python and this tutorial will show students how to use them.

Working with Hadoop using Python instead of Java is entirely possible with a conglomeration of active open source projects that provide Python APIs to Hadoop components. This tutorial will survey the most important projects and show that not only is Hadoop with Python possible, but that it also has some advantages over Hadoop with Java.

The reasons for using Hadoop with Python instead of Java are not all that different than the classic Java vs. Python arguments. One of the most important differences is not having to compile your code by instead using a scripting language. This makes more interactive development of analytics possible, makes maintaining and fixing applications in production environments simpler in many cases, makes for more succinct and easier to read code, and so much more. Also, by integrating Python with Hadoop, you get access to the world-class data analysis libraries such as numpy, scipy, nltk, and scikit-learn that are best-in-breed both inside of Python and outside.

Students will be surprised at how quickly they can get up and running with Hadoop when using Python. In this tutorial, we will talk about the following libraries and approaches and will guide students through a series of exercises:

* Interacting with files in the Hadoop Distributed File System with the snakebite Python module to store potentially petabytes of data
* Writing MapReduce jobs with the mrjob Python module to analyze large amounts of data over potentially thousands of nodes
* Writing MapReduce jobs with Apache Pig (a higher-level data flow language) in conjunction with Python user-defined functions

In addition to these topics, we'll briefly cover the state of Python support for other Hadoop ecosystem projects, such as HBase, Hive, Spark, Storm, Flume, Accumulo, and a few others.



CONTENTS OF THIS REPO

HadoopWithPython-tutorial.pptx.pdf - These are the slides used for the class. They are also available on slideshare: http://www.slideshare.net/DonaldMiner/hadoop-with-python

ipynb/ directory - These are ipython notebook demonstrations of how to use Snakebite, mrjob, and Pig/Python. To use them, start IPython Notebook in the directory:  $ cd ipynb/ ; ipython notebook

pig_scripts/ directory - A pig script for finding the most highly paid individuals in Baltimore. It uses some Python UDFs.

mrjob_scripts/ directory - A few examples of MapReduce jobs written in mrjob. avg.py, max.py, and seniority_v_pay.py are for the Baltimore data, while wordcount.py is a fancy word count that will work on any type of English text.





DATA

The Baltimore FY2014 employee salary data was used for a lot of the exercises here. You can get it here. Download it as a CSV. 
https://data.baltimorecity.gov/City-Government/Baltimore-City-Employee-Salaries-FY2014/2j28-xzd7


PREREQUISITES

The following Python libraries were used (should be able to pip them down): mrjob, snakebite, nltk

The latest versions of Pig and Hadoop 2.x should work with these exercises.


CONTACT INFORMATION

This tutorial was authored by Donald Miner, who can be reached at donaldpminer@gmail.com


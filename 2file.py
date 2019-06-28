#!/usr/bin/env python
#------------------------------------------------Import Packages----------------------------------------------------------------------------
from textblob.classifiers import NaiveBayesClassifier
import os

#-----------------------------------------------Importing Categories from file-------------------------------------------------------------
working_dir=os.getcwd()
fo=open(working_dir+'/Data/'+'CategoryDescription.txt')
line=fo.readline()
description={} 
while line:
	line=line[::-1]
	category=line.split('   ',1)[0][::-1].replace('\n','')
	disease=line.split('   ',1)[1][::-1]
	description[category]=disease
#	print category+' '+disease
	line=fo.readline()
fo.close()
#-----------------------------------------------Training Data----------------------------------------------------------------------------------
traincount=input('Enter number of files to train(0 to train will whole data) : ')
traindata=[]
for folder in description.keys():
	files=os.listdir(working_dir+'/Data/'+folder)
#	print 'Folder '+folder+' has '+str(len(files))+' files'
	filecount = 1
	for filex in files:
		fo=open(working_dir+'/Data/'+folder+'/'+filex)
		datax=""
		for line in fo:
			datax+=line
		traindata
		fo.close()	
		traindata.append((datax,folder))
		if filecount==traincount:
			break
		filecount+=1

#------------------------------------------------Test Data------------------------------------------------------------------------------------------

testdata1='External fixation for type III open tibial fractures. An analysis of 51 type III open tibial fractures treated by external skeletal fixation is presented. The fractures are subdivided according to the classification of Gustilo, Mendoza and Williams (1984) into types IIIa, IIIb and IIIc. The different prognoses of these fracture subtypes is examined. The use of the Hoffmann and Hughes external fixators in the management of type III open tibial fractures is presented and it is suggested that the prognosis is independent of the type of fixator used.'

testdata2='Possible role of leukotrienes in gastritis associated with Campylobacter pylori. This study was done to evaluate the role of leukotrienes (LTs) in gastritis associated with Campylobacter pylori. Biopsy specimens of gastric mucosa were obtained endoscopically from 18 patients with nonulcer dyspepsia for bacteriological and histological examination and extraction of LTs. There was correlation between the LTB4 level in the mucosa and the degree of gastritis evaluated histologically. The level was higher when infiltration of neutrophils in the gastric mucosa was more extensive. The LTB4 level in mucosa infected with C. pylori was higher than that in noninfected mucosa. These findings suggest that endogenous LTs may be related to the pathogenesis of gastritis associated with C. pylori.'


#---------------------------------------------Classifying Data-------------------------------------------------------------------------------

classifier=NaiveBayesClassifier(traindata)
keyt=classifier.classify(testdata1)
#print 'testdata1 : '+str(keyt)
print ("testdata1 is of "+description[keyt]+" category")
keyt=classifier.classify(testdata2)
#print 'testdata2 : '+str(keyt)
print ("testdata2 is of "+description[keyt]+" category")

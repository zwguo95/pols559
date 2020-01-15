install.packages("quanteda")
install.packages("readtext")
install.packages("devtools")
devtools::install_github("quanteda/quanteda.corpora")
install.packages("spacyr")
install.packages("newsmap")

require(quanteda)
require(readtext)
require(quanteda.corpora)
require(newsmap)

#To learn how to use a command, type ? before the command (e.g ?names)

#How to set a path to your data
getwd() #where are you now?
setwd(C:/Users/John/Documents)  #this is obviously an example path

#R vectors

vec_num <- c(1, 5, 6, 3)
vec_num

vec_char <- c('apple', 'banana', 'mandarin', 'melon')
vec_char #don't have to say 'print'

vec_num[1]
vec_num[1:3]
vec_num[c(1,4)]

vec_num2 <- vec_num * 2  #arithmetic
vec_num2

vec_num3 <- append(vec_num,1:5, after = 4) #add values in a specific location
vec_num3

vec_char2 <- paste(c('red', 'yellow', 'orange', 'green'), vec_char) #concatenate
vec_char2

names(vec_num) <- vec_char  #assign names to numbers
vec_num

vec_gt5 <- vec_num >= 5  #is the value greater than 5?
vec_gt5

vec_textmatch <- vec_char == 'apple'  #does the text match?
vec_textmatch

#dataframes (content can be of different data types)

dat_fruit <- data.frame(name = vec_char, count = vec_num)  #combines two vectors above
dat_fruit
nrow(dat_fruit)
ncol(dat_fruit)

dat_fruit_sub <- subset(dat_fruit, count >= 5)  #select only those cases by value
dat_fruit_sub

dat_fruit_sub2 <- subset(dat_fruit, name == 'apple') #by name
dat_fruit_sub2

#matrices (only one data type)

mat <- matrix(c(1, 3, 6, 8, 3, 5, 2, 7), nrow = 4)
mat 

rownames(mat) <- c('bag1', 'bag2', 'bag3', 'bag4') 
mat

colnames(mat) <- c('yep', 'nope') 
mat

dim(mat)

mat['bag1',1]  #first entry in brackets is row range; second is column

rowSums(mat)
colSums(mat)

#importing data

getwd()
setwd(C:/Users/John/Desktop/POLS559/2019/) #must be forward slashes

dat_inaug <- read.csv(paste0('C:/Users/John/Desktop/POLS559/2019/', "inaugCorpus.csv"), encoding ='utf-8')
dim(dat_inaug)  #Make sure that the document character encoding is utf-8
dat_inaug[ ,1]

#The readtext package can be used to read in multiple documents, scrape twitter json files, convert pdfs, read word docs, to text and much much more. 

#here we read in and combine two files from the txt subdirectory. The asterisk says 'get everything' 
dat_reviews <- readtext(paste0('C:/Users/John/Desktop/POLS559/2019/', "txt/*"), docvarsfrom = "filenames", dvsep = "_")

dim(dat_reviews) #rows x columns                      
dat_reviews #look at everything
dat_reviews[1,2] #look at 2nd column of first row
                                    






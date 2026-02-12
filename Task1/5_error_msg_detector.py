logs=["INFO","ERROR","WARNING","ERROR"]
# used count function to count the tota ERROR words in list
error_count=logs.count("ERROR")
print("Total 'ERROR' entries are: ",error_count)
index_of_ERROR=logs.index('ERROR')
print("The index of 'ERROR' is:",index_of_ERROR)
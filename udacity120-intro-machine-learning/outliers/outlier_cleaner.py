#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
    
    cleaned_data = []
    error_holder = []
    ### your code goes here
    # Calculate the residuals
    for i in range(len(predictions)):
        error = (net_worths[i] - predictions[i])**2
        error_holder.append(error[0])
        
    # Sort the errors and select only lower %90 of data 
    error_holder.sort()
    #print error_holder
    #print "Removed errors:", error_holder[len(error_holder)*9/10:]
    error_holder = error_holder[0:len(error_holder)*9/10]
     
    for i in range(len(predictions)):
        error = (net_worths[i] - predictions[i])**2
        if error in error_holder:
            tpl = (ages[i],net_worths[i],error[0])
            cleaned_data.append(tpl)

    #print "Cleaned_data has", len(cleaned_data), "elements"
    #print "Cleaned data error of 5th element:", cleaned_data[5][2]

    
    return cleaned_data


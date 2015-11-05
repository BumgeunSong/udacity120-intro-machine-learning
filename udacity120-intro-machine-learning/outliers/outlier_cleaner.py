#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range(len(predictions)):
        error = net_worths[i] - predictions[i]
        print 'Error:',error[0]
        tpl = (ages[i],net_worths[i],error)
        cleaned_data.append(tpl)

    print "Cleaned_data has", len(cleaned_data), "elements"
    print "Cleaned data error of 5th element:", cleaned_data[5][2][0]
    
    ## TODO: write a code to clean %10 of the outlies here
    return cleaned_data


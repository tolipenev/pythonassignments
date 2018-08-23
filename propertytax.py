# Property tax
# Calculation of assessment value and property tax
# Anatoli Penev
# 26.11.2017

# Main fucntion
def main():
    # Ask for the property's actual value.
    property_value = float(input("Enter the property's actual value: "))
    prop(property_value)


# Property value calculation
def prop(property_value):
    # Calculate the property's assessment value
    # using the actual value.
    # assessment_value=actual_value*60%
    assessment_value = property_value * 0.6
    print('The assessment value is $%.2f' % assessment_value)
    assessment(assessment_value)


# Assessment value calculation
def assessment(assessment_value):
    # Calculate the property tax.
    # Property_tax=$0.64 for every $100 of assessment_value.
    property_tax = assessment_value * 0.0064
    print('The property tax is $%.2f' % property_tax)


# Call the main function.
main()

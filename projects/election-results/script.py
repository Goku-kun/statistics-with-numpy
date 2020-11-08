import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
responses = np.array(survey_responses)
total_ceballos = np.count_nonzero(responses[responses == 'Ceballos'])
print(total_ceballos)
total = sum([1 for x in survey_responses if x == 'Ceballos'])
survey_length = float(len(survey_responses))
percentage_ceballos = 100 * total_ceballos/len(survey_responses)
print(percentage_ceballos)

possible_surveys = np.random.binomial(survey_length, 0.54, size=10000)/survey_length
print(possible_surveys)
plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()
ceballos_loss_surveys = float(len(possible_surveys[possible_surveys < 0.5]))/ len(possible_surveys) * 100
print(ceballos_loss_surveys)

large_survey = np.random.binomial(7000, 0.54, size = 10000) / float(7000)
ceballos_loss_new = float(len(large_survey[large_survey < 0.5])) / len(large_survey) * 100
print(ceballos_loss_new)
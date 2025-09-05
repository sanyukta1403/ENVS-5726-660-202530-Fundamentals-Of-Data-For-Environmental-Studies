import datetime
import statistics

class PreySample:
    def __init__(self, full_species_name, delta13c_list, tissue_description, sample_date_utc):
        self.full_species_name = full_species_name
        self.delta13c_list = delta13c_list
        self.tissue_description = tissue_description
        self.sample_date_utc = sample_date_utc

    def get_discrimination_factor(self):
        return predator_delta13c - get_average_delta13c
    
sample2 = PreySample(
       full_species_name= 'Pacific pmfret (Brama japonica)',
       delta13c_list= [-16,1, -17.8, -19.6, -19.1, -18.0],
       tissue_description= 'Whole animal',
       sample_date_utc= '2020-11-17T05:00:02Z',
)

print(sample2.get_discrimination_factor(predator_delta13c=-15.5))

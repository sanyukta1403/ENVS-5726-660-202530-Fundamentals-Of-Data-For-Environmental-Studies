import datetime 
import statistics 

class DeerHerd:
    def __init__(self, species, deer_count, grazing_area_acres, date_sighted, deer_weight_kg_list):
        self.species = species
        self.deer_count = deer_count
        self.grazing_area_acres = grazing_area_acres
        self.date_sighted = date_sighted
        self.deer_weight_kg_list = deer_weight_kg_list
    
    def get_genus(self):
        return self.species.split(' ')[0]
    
    def get_formatted_date_sighted(self):
        return self.date_sighted.strftime('%B %d, %Y')
    
    def get_grazing_density_deer_per_acre(self):
        return self.deer_count / self.grazing_area_acres
    
    def get_average_deer_weight_kg(self):
        return statistics.mean(self.deer_weight_kg_list)
    

my_herd = DeerHerd(
    species = '0docoileus virginianus',
    deer_count = 10,
    grazing_area_acres = 120,
    date_sighted = datetime.datetime(year=2019,month=4,day=23),
    deer_weight_kg_list = [20, 14, 30, 47, 65, 43, 73, 65, 55, 60]
)

my_herd_genus = my_herd.get_genus()
my_herd_date_sighted_description = my_herd.get_formatted_date_sighted()
my_herd_grazing_density = my_herd.get_grazing_density_deer_per_acre()
my_herd_avg_weight = my_herd.get_average_deer_weight_kg()
print(f'The genus of the hers is {my_herd_genus}')
print(f'Herd was last sighted on {my_herd_date_sighted_description}')
print(f'The grazing density of the herd is {my_herd_grazing_density} deer per acres')
print(f'The average weight of the herd is {my_herd_avg_weight} kilograms')

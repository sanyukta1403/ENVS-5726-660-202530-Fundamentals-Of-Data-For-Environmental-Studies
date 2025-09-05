sample1 = PreySample(
    full_species_name = 'Harbor Seal (Phoca vitulina)',
    delta13c_list = [-12.4, -11.3, -10.6, -13.5, -15.8],
    tissue_description = 'Bone collagen, Bone collagen, Muscle Skin',
    sample_date_utc = '2020-11-16T04:25:03Z',
)

print(sample1.get_cmmon_name())
print(sample1.get_scientific_name())
print(sample1.get_average_delta13c())
print(sample1.get_tissue_count())
print(sample1.get_sample_date())

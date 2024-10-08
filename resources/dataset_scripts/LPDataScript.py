
# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
df = pd.read_excel('../uploaded-datasets/LP2024Categories.xlsx')

# print(df['notes'])
dataset_md = ""

for index, row in df.iterrows():
	f = open("./output/categories/"+str(row['title'])+".md", "a")
	
	dataset_md = "---\n"
	dataset_md = dataset_md+"schema: default\n"
	dataset_md = dataset_md+"title: "+row['title']+"\n"
	dataset_md = dataset_md+"organization: Unitn\n"
	dataset_md = dataset_md+"notes: "+row['notes']+"\n"

	dataset_md = dataset_md+"resources:\n"

	if (row['technical_report-name'] != ""):
		dataset_md = dataset_md+"  - name: "+str(row['technical_report-name'])+"\n"
		dataset_md = dataset_md+"    url: >-\n"
		dataset_md = dataset_md+"      "+str(row['technical_report-URL'])+"\n"
		dataset_md = dataset_md+"    format: "+str(row['technical_report-format'])+"\n"

	if (str(row['codebook-name']) != "nan"):
		codebook_name_array = str(row['codebook-name']).split(', ')
		codebook_url_array = str(row['codebook-URL']).split(', ')
		for c in range(len(codebook_name_array)):
			dataset_md = dataset_md+"  - name: "+codebook_name_array[c]+"\n"
			dataset_md = dataset_md+"    url: >-\n"
			dataset_md = dataset_md+"      "+codebook_url_array[c]+"\n"
			dataset_md = dataset_md+"    format: "+str(row['codebook-format'])+"\n"

	if (str(row['additional_material-name']) != "nan"):
		material_name_array = str(row['additional_material-name']).split(', ')
		material_url_array = str(row['additional_material-URL']).split(', ')
		for m in range(len(material_name_array)):
			dataset_md = dataset_md+"  - name: "+material_name_array[m]+"\n"
			dataset_md = dataset_md+"    url: >-\n"
			dataset_md = dataset_md+"      "+material_url_array[m]+"\n"
			dataset_md = dataset_md+"    format: "+str(row['additional_material-format'])+"\n"

	dataset_md = dataset_md+"license: >-\n"
	dataset_md = dataset_md+"  "+str(row['license'])+"\n"

	dataset_md = dataset_md+"dataset_name: "+row['dataset_name']+"\n"
	dataset_md = dataset_md+"location: "+row['location']+"\n"
	dataset_md = dataset_md+"latitude_map: "+str(row['latitude'])+"\n"
	dataset_md = dataset_md+"longitude_map: "+str(row['longitude'])+"\n"
	dataset_md = dataset_md+"start_date: "+str(row['start_date'])+"\n"
	dataset_md = dataset_md+"end_date: "+str(row['end_date'])+"\n"
	dataset_md = dataset_md+"dataset_type: "+row['dataset_type']+"\n"
	dataset_md = dataset_md+"sensor_type: "+str(row['sensor_type'])+"\n"
	dataset_md = dataset_md+"size: "+str(row['size'])+"\n"
	dataset_md = dataset_md+"dataset_format: "+row['dataset_format']+"\n"
	dataset_md = dataset_md+"other_format: "+row['other_format']+"\n"
	dataset_md = dataset_md+"number_participants: "+str(row['number_participants'])+"\n"
	dataset_md = dataset_md+"language: "+str(row['language'])+"\n"
	dataset_md = dataset_md+"collection_name: "+row['collection_name']+"\n"
	dataset_md = dataset_md+"project_url: <a href=\""+str(row['project_url'])+"\">"+str(row['project_url'])+"</a>\n"

	dataset_md = dataset_md+"category:\n"
	dataset_md = dataset_md+"  - "+"Dataset"+"\n"  # row['domain']

	dataset_md = dataset_md+"5_stars: "+str(row['5_stars'])+"\n"
	dataset_md = dataset_md+"publication_date: "+row['publication_date']+"\n"
	dataset_md = dataset_md+"identifier: "+row['identifier']+"\n"
	dataset_md = dataset_md+"request_contact: "+row['request_contact']+"\n"
	dataset_md = dataset_md+"---\n"
 
	print(dataset_md)
	f.write(dataset_md)
	f.close()

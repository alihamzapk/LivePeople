
# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
df = pd.read_csv('testLP.csv')

# print(df['notes'][1])
dataset_md = ""

for index, row in df.iterrows():
	f = open("./output/"+str(row['title'])+".md", "a")
	
	dataset_md = "---\n"
	dataset_md = dataset_md+"schema: default\n"
	dataset_md = dataset_md+"title: "+df['title'][1]+"\n"
	dataset_md = dataset_md+"organization: Unitn\n"
	dataset_md = dataset_md+"notes: "+df['notes'][1]+"\n"

	dataset_md = dataset_md+"resources:\n"
	dataset_md = dataset_md+"  - name: "+df['technical_report-name'][1]+"\n"
	dataset_md = dataset_md+"    url: >-\n"
	dataset_md = dataset_md+"      "+df['technical_report-URL'][1]+"\n"
	dataset_md = dataset_md+"    format: "+df['technical_report-format'][1]+"\n"

	codebook_name_array = str(df['codebook-name'][1]).split(';')
	codebook_url_array = str(df['codebook-URL'][1]).split(';')
	for c in range(len(codebook_name_array)):
		dataset_md = dataset_md+"  - name: "+codebook_name_array[c]+"\n"
		dataset_md = dataset_md+"    url: >-\n"
		dataset_md = dataset_md+"      "+codebook_url_array[c]+"\n"
		dataset_md = dataset_md+"    format: "+df['codebook-format'][1]+"\n"

	material_name_array = str(df['additional_material-name'][1]).split(';')
	material_url_array = str(df['additional_material-URL'][1]).split(';')
	for m in range(len(material_name_array)):
		dataset_md = dataset_md+"  - name: "+material_name_array[m]+"\n"
		dataset_md = dataset_md+"    url: >-\n"
		dataset_md = dataset_md+"      "+material_url_array[m]+"\n"
		dataset_md = dataset_md+"    format: "+df['additional_material-format'][1]+"\n"

	dataset_md = dataset_md+"license: >-\n"
	dataset_md = dataset_md+"  "+df['licence-URL'][1]+"\n"

	dataset_md = dataset_md+"dataset_name: "+df['dataset_name'][1]+"\n"
	dataset_md = dataset_md+"location: "+df['location'][1]+"\n"
	dataset_md = dataset_md+"start_date: "+df['start_date'][1]+"\n"
	dataset_md = dataset_md+"end_date: "+df['end_date'][1]+"\n"
	dataset_md = dataset_md+"dataset_type: "+df['dataset_type'][1]+"\n"
	dataset_md = dataset_md+"sensor_type: "+df['sensor_type'][1]+"\n"
	dataset_md = dataset_md+"size: "+df['size'][1]+"\n"
	dataset_md = dataset_md+"dataset_format: "+df['dataset_format'][1]+"\n"
	dataset_md = dataset_md+"other_format: "+df['other_format'][1]+"\n"
	dataset_md = dataset_md+"number_participants: "+str(df['number_participants'][1])+"\n"
	dataset_md = dataset_md+"language: "+df['language'][1]+"\n"
	dataset_md = dataset_md+"collection_name: "+df['collection_name'][1]+"\n"
	dataset_md = dataset_md+"project_url: <a href=\""+df['project_url'][1]+"\">"+df['project_url'][1]+"</a>\n"

	dataset_md = dataset_md+"category:\n"
	dataset_md = dataset_md+"  - "+df['domain'][1]+"\n"

	dataset_md = dataset_md+"5_stars: "+str(df['5_stars'][1])+"\n"
	dataset_md = dataset_md+"publication_date: "+df['publication_date'][1]+"\n"
	dataset_md = dataset_md+"identifier: "+df['identifier'][1]+"\n"
	dataset_md = dataset_md+"request_contact: "+df['request_contact'][1]+"\n"
	dataset_md = dataset_md+"---\n"
 
	print(dataset_md)
	f.write(dataset_md)
	f.close()
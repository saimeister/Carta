Hi,

Please follow the below instructions

1. The file "Parse_Aggregate.py" contains the script for the parsing and aggregation of nginx.log in terms of 
	a. Number of occurrences of each source IP address
	b. number of distinct IP addresses belonging to the below subnets
		○ 108.162.0.0/16
		○ 212.129.32.128/25
		○ 173.245.56.0/23

Run command: python Parse_Aggregate.py
(I also added comments for better understanding of the code)

2. The file "Carta.py" creates a flask webserver that outputs the information obtained from executing "Parse_Aggregate.py"
(Please refer to Carta_description.py for commented version of Carta.py)


3. The Dockerfile contains necessary infromation required to build the docker image, 
	Base: nginx:latest
	Installing flask
	Executing Carta.py

4. Build the docker file using below command: 
	a. docker build -t carta_image .
	(you can use any tag by replacing carta_image) 

5. Running the image as a docker container
	a. docker run -d -p 8080:8080 carta_image
	(use -d to run in detach mode, also replace carta_image with the tag you used in step 4.a)
	
6. Now you can access the data either through your browser: http://localhost:8080 or through terminal using "curl http://localhost:8080"


NOTE:
Please note, I did not convert the IpV6 to IpV4

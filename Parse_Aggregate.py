
#Opening the file 

with open('nginx.log') as f:
    f = f.readlines()


#Defining variable repition of each address
    
ip_counter = {}

#Looping through the lines to accumulate each address

for line in f:
    ip = line.split(' -')[0]
    if ip in ip_counter.keys():
        ip_counter[ip] = ip_counter[ip] + 1
    else:
        ip_counter[ip] = 1

#For lopp to print the repition of each address

for ip in ip_counter.keys():
    print("Address {} was encountered {} times(s)".format(ip,ip_counter[ip]))


print("--------------------------------------------------")


#Defining subnet aggregation dictionary for the given subnets
    
unique_ips = list(ip_counter.keys())
subnet_aggregation = {'108.162.0.0/16':0,
                      '212.129.32.128/25':0,
                      '173.245.56.0/23':0}

#Checking the loop to find out the ips starting with given subnets

for ip in unique_ips:
    if ip.startswith('108.162.'):
        subnet_aggregation['108.162.0.0/16'] += 1
    if ip.startswith('212.129.32.'):
        subnet_aggregation['212.129.32.128/25'] += 1
    if ip.startswith('173.245.56.'):
        subnet_aggregation['173.245.56.0/23'] += 1

#For lopp to print the number of ips in given subnets

for subnet in subnet_aggregation.keys():
	print("The bucket {} contains {} addresses".format(subnet,subnet_aggregation[subnet]))





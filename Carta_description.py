# flask_web/app.py

#import flast library

from flask import Flask
app = Flask(__name__)


#Define main route

@app.route('/')
def Carta():


    #Defining dictinaries
    
    result = {}
    address = {}



    with open('nginx.log') as f:
        f = f.readlines()

    ip_counter = {}

    for line in f:
        ip = line.split(' -')[0]
        if ip in ip_counter.keys():
           ip_counter[ip] = ip_counter[ip] + 1
        else:
            ip_counter[ip] = 1

    #Storing ips and counts as key and values in address dictionary

    for ip in ip_counter.keys():
        print("Address {} was encountered {} times(s)".format(ip,ip_counter[ip]))
        address[ip] = ip_counter[ip]

    print("--------------------------------------------------")

    unique_ips = list(ip_counter.keys())
    subnet_aggregation = {'108.162.0.0/16':0,
                        '212.129.32.128/25':0,
                        '173.245.56.0/23':0}
    for ip in unique_ips:
        if ip.startswith('108.162.'):
            subnet_aggregation['108.162.0.0/16'] += 1
        if ip.startswith('212.129.32.'):
            subnet_aggregation['212.129.32.128/25'] += 1
        if ip.startswith('173.245.56.'):
            subnet_aggregation['173.245.56.0/23'] += 1

    #Storing subnets and aggregation as key and values in result

    for subnet in subnet_aggregation.keys():
            print("The bucket {} contains {} addresses".format(subnet,subnet_aggregation[subnet]))
            result[subnet] = subnet_aggregation[subnet]
    final_result = {}
    final_result['buckets'] = result
    final_result['address'] = address
    return final_result



if __name__ == '__main__':

    #Running on localhost with port 8080

    app.run(debug=False, host='0.0.0.0',port = 80)

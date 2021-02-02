import os
import sys
import logging
import pynetbox
import route53



class NetboxRoute53:
  def __init_(self):

    # Initialize logging
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    self.logging = logging.getLogger()

    # Initialize Netbox
    if "NETBOX_URL" in os.environ:
        self.nb_url = os.getenv("NETBOX_URL")
    else:
        logging.error("Environmnet variable NETBOX_URL must be set")
        sys.exit(1)

    if "NETBOX_TOKEN" in os.environ:
        self.nb_token = os.getenv("NETBOX_TOKEN")
    else:
        logging.error("Environmnet variable NETBOX_TOKEN must be set")
        sys.exit(1)

    self.nb = pynetbox.api(url=self.nb_url, token=self.nb_token)

    # Not sure if I need these yet
    # self.nb_prefixes = self.nb.ipam.prefixes.all()
    # self.nb_ip_addresses = self.nb.ipam.ip_addresses.all()


    # Initialize Route53
    if "ROUTE53_ID" in os.environ:
        self.r53_id = os.getenv("ROUTE53_ID")
    else:
        logging.error("Environment variable ROUTE53_ID must be set")
        sys.exit(1)

    if "ROUTE53_KEY" in os.environ:
        self.r53_key = os.getenv("ROUTE53_KEY")
    else:
        logging.error("Environment variable ROUTE53_KEY must be set")
        sys.exit(1)

    # I dont know if this works
    conn = route53.connect(
        aws_access_key_id=self.r53_id,
        aws_secret_access_key=self.r53_key,
    )

  # Not sure I need these functions
  # Might only need check_ip_addresses & maybe is_discovered

  # Prefix
  def check_prefixes(self, ip_address):
    for prefix in self.nb_prefixes:
        if prefix.status.value == 'active' and (ipaddress.ip_address(ip_address) in ipaddress.ip_network(
                prefix.prefix)):
            return prefix.prefix.split('/')[1]
    return None

  # Ip - address
  def check_ip_addresses(self, ip_address):
    for nb_ip_address in self.nb_ip_addresses:
        if ip_address in nb_ip_address.address:
            return nb_ip_address
    return None

  # discovered tag
  def is_discovered(self, nb_ip_address):
    for tag in nb_ip_address.tags:
        if tag.name == self.discovered_tag:
            return True
    return False

  # Netbox stuff for getting prefixes
pfx_search = nb.ipam.prefixes.all()

for pfx in pfx_search:
      #pfx.prefix, pfx.status, pfx.ip,










#add error catches for the below functions
#route53.exceptions.Route53Error
    #R53 function to update a records by passing in the prefix and ip (check both and update respectively)
  def record_update(ip, prefix)

    #R53 function to create a record by passing in the prefix and ip
  def record_create(ip, prefix):
    record_set.create_a_record(name, values, ttl=60, weight=None, region=None, set_identifier=None, alias_hosted_zone_id=None, alias_dns_name=None)
        #what record am I creating here? a/aaaa/cname/mx/ns/ptr/spf/srv/TXT/
        #Using a function for code simplicity to easily pass in netbox ip and prefix in the for loop later on
        #new_record, change_info = zone.create_a_record(name= prefix,values=ip,)


  # Code for R53 add / update records based on NB
  # Find out what is needed of the 3 functions defined
  # Above, and how they tie into comparing records in R53

  #comparing netbox to r53:
  #iterate through ips using netbox_ip
  #probably will use nb_ip_address (possibly could call the function and pass it in at the same time)
  #check if record_set . name is appropiate or if it should be record_set . ip (also find a way to print both r53 and nb ips and compare them manually first before automating)
  #find out what this code block below prints

netbox_ip = '(insert netbox ip here)'
for record_set in zone.record_sets:
    if record_set.name == netbox_ip:
        print(record_set)
        break

# Iterate through netbox ips on line 103
netbox_ip = '(insert netbox ip here)'
for record_set in zone.record_sets:
    if record_set.name == netbox_ip:
        print(record_set)
        break
    else:
        record_set.create_a_record(name, values, ttl=60, weight=None, region=None, set_identifier=None, alias_hosted_zone_id=None, alias_dns_name=None)

  # On line 109 figiure out what type of record to create with create_" "_record

  #saving a record (experiment with this) (this is if record exists but doesn't match)
record_set.values = ['insert record to be changed here']
record_set.save()

  #creating a record (pass in the ip and name from netbox)

new_record, change_info = zone.create_a_record(
name='test.some-domain.com.',
values=['8.8.8.8'],)

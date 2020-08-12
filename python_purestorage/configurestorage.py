import purestorage
from purestorage import FlashArray

# Never do this in prod. SSL warning are there for a reason.
import urllib3
urllib3.disable_warnings()

#Variables
fa_url = "myarray.fqdn"
fa_username = "pureuser"
fa_password = "pureuser"

#Start Session
array = FlashArray(fa_url, fa_username, fa_password)

#Create Volume
array.create_volume("david-python-vol01", "10G")

#Create Hosts
array.create_host("david-python-host1", iqnlist=["iqn.1998-01.com.vmware:david-python-host1"])
array.create_host("david-python-host2", iqnlist=["iqn.1998-01.com.vmware:david-python-host2"])

#Create Host Group and Add Host1 and Host2
array.create_hgroup("david-python-hostgroup", hostlist=["david-python-host1", "david-python-host2"])

#Connect Volume to Host Group
array.connect_hgroup("david-python-hostgroup", "david-python-vol01")

#End Session
array.invalidate_cookie()


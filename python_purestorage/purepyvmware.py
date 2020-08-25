#imports
from purepyvmware import base_connector
from purepyvmware import datastores

#Variables
fa_url = "myarray.fqdn"
fa_username = "pureuser"
vc_url = "vc.lab.local"
vc_username = "administrator@vsphere.local"
vc_cluster = "cluster01"

#Start Session
connector = base_connector.BaseConnector(fa_url, fa_username, vc_url, vc_username, verify_ssl=False)
flasharray = connector.fa_instance

#Get Volumes
vsphere_content = connector.vsphere_content
ds_mgr = datastores.Datastores(vsphere_content, flasharray)
pure_datastores = ds_mgr.get_all_pure_datastores()
for datastore in pure_datastores:
    print(datastore.name)

#Create Datastore
vmfs_mgr = datastores.VmfsDatastores(vsphere_content, flasharray)
vmfs_ds = vmfs_mgr.create_vmfs_datastore(vc_cluster, 'python_ds01', 500)
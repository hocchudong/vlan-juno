pip install python-keystoneclient
pip install python-novaclient
pip install python-neutronclient
pip install python-glanceclient
pip install python-cinderclient



# lay token cua Keystone
from os import environ as env
import keystoneclient.v2_0.client as ksclient
keystone = ksclient.Client(auth_url="http://8.21.28.222:5000/v2.0",
                           username="facebook849703855110876",
                           password="ek7C5sWRVx5N1nal",
                           tenant_name="facebook849703855110876",
                           region_name="RegionOne")
                           
print keystone.auth_token

#glance (phai thuc hien keystone truoc)
import glanceclient.v2.client as glclient
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)

#nova
from os import environ as env
import novaclient
nova = novaclient.client.Client(auth_url="http://controller:35357/v2.0",
                           username="admin",
                           api_key="Welcome123",
                           project_id="admin",
                           region_name="regionOne")
                           
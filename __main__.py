import pulumi
from pulumi_gcp import compute


with open(‘init_script.txt’, ‘r’) as init_script:
    data = init_script.read()
script = data
config = pulumi.Config()
instance_name = config.require(‘instance_name’)
instance_type = config.require(‘instance_type’)
instance_image = config.require(‘instance_image’)
instance_disk_size = config.require(‘instance_disk_size’)
addr = compute.address.Address(instance_name)
network = compute.Network(instance_name)
firewall = compute.Firewall(
  instance_name,
  network=network.self_link,
  allows=[
    {
      “protocol”: “tcp”,
      “ports”: [“22”]
    }
  ]
)
instance = compute.Instance(
  instance_name,
  name=instance_name,
  machine_type=instance_type,
  boot_disk={
    “initializeParams”: {
       “image”: instance_image,
       “size”: instance_disk_size
     }
  },
  network_interfaces=[
    {
      “network”: network.id,
      “accessConfigs”: [{“nat_ip”: addr.address}]
    }
  ],
  metadata_startup_script=script,
)
# Export the DNS name of the bucket

pulumi.export(“instance_name”, instance.name)
pulumi.export(“instance_network”, instance.network_interfaces)
pulumi.export(“external_ip”, addr.address)

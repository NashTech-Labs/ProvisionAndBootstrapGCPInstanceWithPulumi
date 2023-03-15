PREREQUISITE

- Install Pulumi : https://www.pulumi.com/docs/get-started/install/
- Download GCloud SDK and CLI : https://cloud.google.com/sdk/
- You can follow the setup instructions from here : https://www.pulumi.com/registry/packages/gcp/installation-configuration/

Then you can run following command : 

```
$ gcloud auth login
$ gcloud config set project PROJECT_ID
$ gcloud auth application-default login
```

Now you can cd to this template directory and To perform an initial deployment, run the following commands:
``` 
1. virtualenv -p python3 venv
2. source venv/bin/activate
3. pip3 install -r requirements.txt
```

Then, run `pulumi up`
Select yes from the prompt

Note that I pass the data from a file called init_script.txt to the compute.Instance constructor, assigning it to the variable metadata_startup_script where I add my personal ssh public key on the remote instance, then I install docker and docker-compose
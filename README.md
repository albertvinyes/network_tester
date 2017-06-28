### Networking
By using this software, you can analyse network performance indicators such as download bandwidth, upload bandwidth and latency. Furthermore, the software runs a performance test periodically and provide you a dashboard to visualize the results and interact with them.

### Contributors
- Albert Viñés: albert.vines@gmail.com
- 

#### Requirements
You will need python and pip to be installed in your system. We suggest the usage of python virtual environments to isolate  application dependencies and to avoid changing the system's python packages. You can install virtualenv with the following command:


```shell
sudo pip install virtualenv
```

#### Installation
```shell
git clone https://github.com/albertvinyes/network_tester.git
cd network_tester
virtualenv -p /usr/bin/python3.5 venv
source venv/bin/activate
pip install -r requirements.txt
```
#### Running the software
An hourly test can be run separate to the UI webserver. The test automatically stores the results in a Database which feeds the UI. To execute the hourly test run:

```shell
source venv/bin/activate
python scheduler.py
```

To run the UI webserver execute:
```shell
source venv/bin/activate
python run.py
```

#### Accessing the UI
Open your favorite browser and visit 0.0.0.0:8080

#### Configuration
You can configure the port where the webserver will listen in the **app/config.py** file. Keep in mind that listening in ports lower than 80 needs administrator privileges.

# MariaDB MaxScale Docker image

This Docker image runs the latest version of MariaDB MaxScale.

## Running
[The MaxScale docker-compose setup contains a horizontal sharding setup where two shards of a database are split and a maxscale instance that will load balance the two database shards by directing requests depending on which item of data is targeted. all zipcode requests that are in between the 0 and 41000 range that exist will go
shard one and the rest remaining ( approx 41K to 80K) will be directed to databas server shard 2]
[ To use this maxscale instance type type the following at the command line to start containers]

```

docker-compose up -d
```

After MaxScale and the servers have started  you can find
the readwrite router on port 4006 and the read only listener on port 4008. The
user `maxuser` with the password `maxpwd` can be used to test the cluster.
Make sure to install mariaDB on the machine along with pip sqlconnector if you want to use the embedded python file to run very quick and efficient queries on either database being sharded. 
For entering  inside the database  the use must supply the following script with the proper credentials
```
$ mariadb -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
you will see this displayed when you log in:
Welcome to the MariaDB monitor.  Commands end with ;
Your MySQL connection id is 
Server version: 10.2.12 2.2.9-maxscale mariadb.org binary distribution
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [test]>
```

To run the embedded main.py python file enter the following:
python3 main.py

This will allow very quick queries inside either shard via maxscale. change the code inside main.py your choosing as long as you honor SQL syntax or you will get errors just like you would if you make errors inside the maxscale mariadb when running database querries.

```
You can edit the [`maxscale.cnf.d/example.cnf`](./maxscale.cnf.d/example.cnf)
file and change the container configuration.

To exit/logout type

exit

 

To run maxctrl in the container to see the status of the cluster:
```
$ docker-compose exec maxscale maxctrl list servers
┌─────────┬─────────┬──────┬─────────────┬─────────────────┬──────────┐
│ Server  │ Address │ Port │ Connections │ State           │ GTID     │Monitor
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ primar1 │ primar12  │ 3306 │ 0           │ Master, Running             MariaDB-Monitor │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ primar2 │ primary2 │ 3306 │ 0           │ Slave, Running  │            MariaDB-Monitor│
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────


```
This Load Balancing method  uses a primary and a primary 2 shard servers which load balance by splitting the data into two seperate databases via maxscale therefore decreasing the load of each database server when user traffic is heavy


Once complete, to remove the cluster and maxscale containers:

```
docker-compose down -v
```
#references/credit:
#https://github.com/mariadb-corporation/maxscale-docker/blob/master/README.md
#was used for the initial template which supplied the information needed to enter for this to be a clear and concise guide to running this maxscale horizontal sharding instance.
#credit also goes to Christine Sutton for providing the needed material in class CNE370 to get this project off the ground and up and running

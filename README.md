# Random-Delay-and-Indirections
Preserving privacy of the users using random delays and indirections. The random delays are introduced for each message in a time gap of 1-10 seconds. Each node can generate new message or forward the duplicate message which it received (after adding it's own random delay).

# To run network simulator-

cd /Users/anujdimri/Downloads/simulations/hello-sumo/omnetpp-5.1.1 <br />
. setenv <br />
omnetpp

# To run vehicle simulator via veins

/Users/anujdimri/Downloads/veins-veins-4.6/sumo-launchd.py -vv -c sumo-gui

# Execute the following file

/veins/example/veins/omnetpp.ini


# omnet to traci function path- 
src->mobility->traci->TraciConnection.cc

# TODO
Message contents should be source ID and location in lat/lon

Give uploader also some time to move away from its original location

OSMNX street view for adversary

For each edge set of possible edges in previous circle (intersection)

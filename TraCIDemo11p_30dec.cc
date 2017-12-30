//
// Copyright (C) 2006-2011 Christoph Sommer <christoph.sommer@uibk.ac.at>
//
// Documentation for these modules is at http://veins.car2x.org/
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//

#include <omnetpp/ccomponent.h>
#include <omnetpp/cdisplaystring.h>
#include <omnetpp/clog.h>
#include <omnetpp/cobjectfactory.h>
#include <omnetpp/csimulation.h>
#include <omnetpp/regmacros.h>
#include <omnetpp/simtime.h>
#include <veins/base/modules/BaseMobility.h>
#include <veins/base/utils/Coord.h>
#include <veins/modules/application/traci/TraCIDemo11p.h>
#include <veins/modules/mac/ieee80211p/WaveAppToMac1609_4Interface.h>
#include <veins/modules/messages/WaveServiceAdvertisement_m.h>
#include <veins/modules/messages/WaveShortMessage_m.h>
#include <veins/modules/mobility/traci/TraCICommandInterface.h>
#include <veins/modules/mobility/traci/TraCIMobility.h>
#include <veins/modules/utility/Consts80211p.h>
#include <iostream>
#include <string>
#include <utility>
#include <sstream>
//#include <omnetpp/cmsgheap.h>
#include <omnetpp.h>


using Veins::TraCIMobilityAccess;
using Veins::AnnotationManagerAccess;



Define_Module(TraCIDemo11p);

void TraCIDemo11p::initialize(int stage) {
    BaseWaveApplLayer::initialize(stage);

    EV<<"ANUJ1"<<"\n";
    if (stage == 0) {
        sentMessage = false;
        lastDroveAt = simTime();
        currentSubscribedServiceId = -1;
    }
}

void TraCIDemo11p::onWSA(WaveServiceAdvertisment* wsa) {

    EV<<"ANUJ10"<<"\n";

    if (currentSubscribedServiceId == -1) {
        mac->changeServiceChannel(wsa->getTargetChannel());
        currentSubscribedServiceId = wsa->getPsid();
        if  (currentOfferedServiceId != wsa->getPsid()) {
            stopService();
            startService((Channels::ChannelNumber) wsa->getTargetChannel(), wsa->getPsid(), "Mirrored Traffic Service");
        }
    }
}

void TraCIDemo11p::onWSM(WaveShortMessage* wsm) {

    EV<<"ANUJ2"<<"\n";
    findHost()->getDisplayString().updateWith("r=16,green");

    cModule *tmpMobility = getParentModule()->getSubmodule("veinsmobility");
                mobility = dynamic_cast<Veins::TraCIMobility*>(tmpMobility);
                ASSERT(mobility);
                EV<<"hello dec";
                EV<<mobility->getExternalId();


    int cc= intuniform(1,10);
    if ((cc==2)||(cc==4))
    {
        //cancelAndDelete(wsm->dup());
        delete(wsm->dup());
    }
    else if (wsm->isScheduled())
    {
        //cancelAndDelete(wsm);
        EV<<"ANUJ dec 2 scheduled";
        delete(wsm->dup());
    }
    else{


    scheduleAt(simTime()+cc,wsm->dup());
    }

    //cSimulation::getActiveSimulation()->getFES();
    //cMessageHeap::Iterator it(heap);


    // Getting access of future event heap
    cFutureEventSet* heap = cSimulation::getActiveSimulation()->getFES();

    /*cFutureEventSet::operator it(heap);
    do {
        cMessage * event = it();
        if (event && event->isSelfMessage()) {
            cancelAndDelete(event);
            it.init(heap);
        } else {
            it++;
        }

    } while (!it.end());
    */

    // iterating through the whole heap
    int length=heap->getLength();
    int i=0;
    for (i=0;i<length;i++)
    {
        cEvent *event=heap->get(i);

        if (event->isMessage())
        {
            EV<<"ANUJ printing events";
            EV<<event->getName();
            //EV<<event->getName();
            EV<<"   ";
            EV<<wsm->getName();

            // Comparing by names
            /*********TODO delete message. If possible do this when being uplaoded to the server**************/
            if (!(std::string(event->getName()).compare(std::string(wsm->getName()))))
            {
                EV<<"Same name inside loop ";
                EV<<event->getName();
                EV<<"   ";
                EV<<wsm->getName();
            }
        }


    }





    //if (mobility->getRoadId()[0] != ':') traciVehicle->changeRoute(wsm->getWsmData(), 9999);
    //if (!sentMessage) {
    //    sentMessage = true;
        //repeat the received traffic update once in 2 seconds plus some random delay
    //    wsm->setSenderAddress(myId);
     //   wsm->setSerial(3);
     //   scheduleAt(simTime() + 2 + uniform(1,10), wsm->dup());
    //}
}

void TraCIDemo11p::handleSelfMsg(cMessage* msg) {
    if (WaveShortMessage* wsm = dynamic_cast<WaveShortMessage*>(msg)) {
        //send this message on the service channel until the counter is 3 or higher.
        //this code only runs when channel switching is enabled
        if (wsm->isScheduled())
            {

                //cancelAndDelete(wsm);
                EV<<"ANUJ dec scheduled";
                delete(wsm->dup());
            }
        else
        {
            EV<<"ANUJ dec";
            EV<<wsm->getSenderAddress();
            EV<<wsm->getSenderModuleId();




           // EV<<mySumoID;

            //wsm->getR
            EV<<wsm->getTreeId();
            sendDown(wsm->dup());

        }
        //scheduleAt(simTime()+intuniform(1,10),wsm->dup());

        EV<<"ANUJ3"<<mobility->getRoadId().c_str()<<"\n";

       // wsm->setSerial(wsm->getSerial() +1);
       // if (wsm->getSerial() >= 300) {
            //stop service advertisements
      //      stopService();
      //      delete(wsm);
     //   }
     //   else {
     //       scheduleAt(simTime()+1, wsm);
       // }
    }
    else {
        //BaseWaveApplLayer::handleSelfMsg(msg);
    }
}

void TraCIDemo11p::handlePositionUpdate(cObject* obj) {
    BaseWaveApplLayer::handlePositionUpdate(obj);


    EV<<"ANUJ4"<<"\n";
    EV<<"ANUJ4a"<<mobility->getRoadId().c_str()<<"\n";
    EV<<"ANUJ4b position"<<mobility->getPositionAt(simTime())<<"and"<<mobility->getCurrentPosition()<<"\n";
    //EV<<"ANUJ4c "<<traci->getTraCIXY(mobility->getCurrentPosition()) <<"\n";
    //traci->getLonLat(coord)

    std::pair<double,double> coordTraCI = traci->getTraCIXY(mobility->getCurrentPosition());
    EV<<"ANUJ4c"<<coordTraCI.first<<" "<<coordTraCI.second;


    // data being created every second as this function is called every second
    static int c=0;
    std::string pre="id ";
    //std::string result =  (const char *)c;
    std::stringstream ss;

    ss<<c<<"-"<<pre;
    std::string result=ss.str();

    if (c<20)
    {
    WaveShortMessage* wsm = new WaveShortMessage(result.c_str());
    c=c+1;
    populateWSM(wsm);
    wsm->setWsmData(mobility->getRoadId().c_str());
    //wsm->setWsmData(std::string(simTime()).c_str());
    scheduleAt(simTime()+intuniform(1,10),wsm);
    //wsm->setArrivalTime(simTime()+intuniform(1,10));
    //sendDown(wsm);
    }


    // stopped for for at least 10s?
    //if (mobility->getSpeed() < 0) {
    //    if (simTime() - lastDroveAt >= 100 && sentMessage == false) {
    //        findHost()->getDisplayString().updateWith("r=16,red");
    //        sentMessage = true;

    //        WaveShortMessage* wsm = new WaveShortMessage();
    //        populateWSM(wsm);
    //        wsm->setWsmData(mobility->getRoadId().c_str());


    //        EV<<"ANUJ4a"<<mobility->getRoadId().c_str()<<"\n";
    //        EV<<"ANUJ4b position"<<mobility->getPositionAt(simTime())<<"\n";

            //host is standing still due to crash
    //        if (dataOnSch) {
    //            startService(Channels::SCH2, 42, "Traffic Information Service");
                //started service and server advertising, schedule message to self to send later
    //            scheduleAt(computeAsynchronousSendingTime(1,type_SCH),wsm);
    //        }
    //        else {
                //send right away on CCH, because channel switching is disabled
    //            sendDown(wsm);
    //        }
    //    }
//    }
//    else {
//        lastDroveAt = simTime();
//    }
}

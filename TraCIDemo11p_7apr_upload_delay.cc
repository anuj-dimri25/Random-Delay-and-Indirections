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
    /*
    EV<<"ANUJ10"<<"\n";

    if (currentSubscribedServiceId == -1) {
        mac->changeServiceChannel(wsa->getTargetChannel());
        currentSubscribedServiceId = wsa->getPsid();
        if  (currentOfferedServiceId != wsa->getPsid()) {
            stopService();
            startService((Channels::ChannelNumber) wsa->getTargetChannel(), wsa->getPsid(), "Mirrored Traffic Service");
        }
    }
    */
}



void TraCIDemo11p::onWSM(WaveShortMessage* wsm) {

    EV<<"ANUJ2"<<"\n";
    //findHost()->getDisplayString().updateWith("r=16,green");
    //cQueue

    //EV<<"name "<<findHost()->getDispl<<"\n";

    cModule *tmpMobility = getParentModule()->getSubmodule("veinsmobility");
                mobility = dynamic_cast<Veins::TraCIMobility*>(tmpMobility);
                ASSERT(mobility);
                EV<<"hello dec anuj id";
                EV<<mobility->getExternalId();
                EV<<"mobility name "<<mobility->getId()<<""<<mobility->getFullName()<<" "<<mobility->getFullPath()<<" ";

                EV<<"grdgj "<<wsm->getArrivalModuleId()<<" "<<wsm->getArrivalGate()<<" "<<wsm->getSenderModule()<<" "<<wsm->getSenderAddress();
    int cc= intuniform(4,10);


    Veins::TraCIMobility* mobility =
      check_and_cast<Veins::TraCIMobility*>(
        getParentModule()->getSubmodule("veinsmobility"));

    Veins::TraCICommandInterface* traci = mobility->getCommandInterface();

    Coord currPos = mobility->getCurrentPosition();
    std::pair<double, double> currLonLat = traci->getLonLat(currPos);
    EV<<"anuj current lon lat ";
    EV<<currLonLat.first<<" "<<currLonLat.second;



    EV<<"anuj module name -- "<<getParentModule()->getFullName();


    //if (cc==3)
    //{
       // EV<<"value of cc is 3 wsm"<<wsm->getFullName();
        //delete(wsm);
        //cancelAndDelete(wsm);
        //cancelEvent(wsm);



        /*
        cFutureEventSet* heap = cSimulation::getActiveSimulation()->getFES();
        //heap->sort();
        //cFutureEventSet* heap = cSimulation::getFES();
            int length=heap->getLength();
            int i=0;
            EV<<"anuj length is "<<length<<"\n";

            while (i<heap->getLength())
            {
                cEvent *event=heap->get(i);
                EV<<event->getName()<<" "<<i<<" \n";
                i=i+1;

            }
            EV<<"end while \n";

            i=0;

            //cFutureEventSet::Iterator it(heap);
            while(i<heap->getLength())
            {
                cEvent *event=heap->get(i);


                //if (event->isMessage())
                //{
                    EV<<"ANUJ printing events";
                    EV<<event->getName();
                    //EV<<event->getName();
                    EV<<"   ";
                    EV<<wsm->getName()<<" \n";

                    // Comparing by names
                    if (!(std::string(event->getName()).compare(std::string(wsm->getName()))))
                    {
                        EV<<"Same name inside loop \n";
                        EV<<event->getName();
                        EV<<"   ";
                        EV<<wsm->getName()<<"\n";

                       //cancelEvent(event);

                        //delete(event);



                        // deleting message from queue
                        EV<<"b4 deleting "<<length<<" ";
                        cEvent *removedEvent=heap->remove(event);
                        //drop(event);
                        //heap->remove(event);

                        //i=i-1;
                        length=heap->getLength();
                        EV<<"after deleting "<<length<<" \n";
                        //length=length-1;
                        //cancelAndDelete(event);
                        EV<<"Removed event "<<i<<" ";
                        EV<<removedEvent<<"\n";
                        free(removedEvent);
                        //removedEvent->

                        //cFutureEventSet* heap = cSimulation::getActiveSimulation()->getFES();
                       // heap->sort();
                        //cFutureEventSet* heap = cSimulation::getFES();
                        //length=heap->getLength();
                        //i=0;
                        //length=length-1;
                        //i=i+1;



                        //delete removedEvent;
                       // removedEvent=NULL;

                    }
                    else
                    {
                        EV<<"in else "<<i<<"\n";
                        i=i+1;
                    }
                //}


            }*/

            //cancelAndDelete(wsm->dup());
            //drop(wsm);

   //}

    //else{


    simtime_t prev_upload=0;

    static simtime_t uploaded[100000]={};
    static simtime_t prev_upload_time[100000]={};
    static int index=0;
    int i=0;
    int flag=0;
    for(i=0;i<100000;i++)
    {
        if(wsm->getCreationTime()-uploaded[i]==0)
            {
            flag=1;
            break;
            }
        else
        {
            flag=0;
        }
    }

    // current vehicle
    std::string str=mobility->getFullPath();
             unsigned first=str.find('[');
             unsigned last=str.find(']');
             std::string strnew=str.substr(first+1,last-first);
             EV<<"printing substring "<<strnew;
             std::stringstream up(strnew);
             int x=0;
             //int x=std::stoi(strnew);
            //std::stoi(strnew, x, 10);
             up>>x;
    EV<<"printing x "<<x;
    if (flag==1)
    {
        EV<<"Already uploaded";
    }




    //else if((simTime()- wsm->getCreationTime() > 100)|| mobility->getSpeed()<3)
              //{
                  //delete(wsm->dup());
              //}
    else if ((simTime()- wsm->getCreationTime() > 15) && (simTime()-prev_upload_time[x] >15) && ((cc==6) || (cc==7) || (cc==8)))
    {
       EV<<"uploaded to server at time "<<simTime()<<" message  name is "<<wsm->getFullPath()<<" ";


       //prev_upload=simTime();

      prev_upload_time[x]=simTime();
      EV<<"prev upload "<<prev_upload_time[x]<<" "<<x;





       cModule *tmpMobility = getParentModule()->getSubmodule("veinsmobility");
                           mobility = dynamic_cast<Veins::TraCIMobility*>(tmpMobility);
                           ASSERT(mobility);
                           EV<<"update hello dec anuj id";
                           EV<<mobility->getExternalId();
                           //EV<<" update mobility name "<<mobility->getId()<<""<<mobility->getFullName()<<" "<<mobility->getFullPath()<<" ";

                           Veins::TraCIMobility* mobility =
                                 check_and_cast<Veins::TraCIMobility*>(
                                   getParentModule()->getSubmodule("veinsmobility"));

                               Veins::TraCICommandInterface* traci = mobility->getCommandInterface();

                               Coord currPos = mobility->getCurrentPosition();
                               std::pair<double, double> currLonLat = traci->getLonLat(currPos);
                               EV<<"anuj current lon lat ";
                               EV<<currLonLat.first<<" "<<currLonLat.second;

       std::ofstream myfile10;
              myfile10.open("Exampleall_29mar_042test_up.txt",std::ios_base::app);
              myfile10<<"all uplood "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<" "<<wsm->getCreationTime()<<" orig lon lat "<<wsm->getWsmData()<<" uploader "<<mobility->getFullPath()<<"\n";
              myfile10.close();


       uploaded[index]=wsm->getCreationTime();
       index=index+1;
       EV<<"Anuj index value "<<index<<"\n";

       std::stringstream ss20;

                 ss20<<getParentModule()->getFullName();
                 std::string result20=ss20.str();
                 //wsm->setName(result1.c_str());

       if (result20=="node[0]")
       {
       EV<<"uploaded by 0-id";
       EV<<"0-id "<<wsm->getFullPath()<<" "<<simTime()<<"\n";
       std::ofstream myfile0;
       myfile0.open("Example0_29mar_042test_up.txt",std::ios_base::app);
       myfile0<<"0-id "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<" "<<wsm->getCreationTime()<<"\n";
       myfile0.close();
       }

       if (mobility->getFullPath()=="RSUExampleScenario.node[0].veinsmobility")
                    {
                 EV<<"uploaded by 00-id";
                        EV<<"00-id "<<wsm->getFullPath()<<" "<<simTime()<<"\n";
                    std::ofstream myfile00;
                    myfile00.open("Example00_29mar_042test_up.txt",std::ios_base::app);
                    myfile00<<"00-id "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<" "<<wsm->getCreationTime()<<"\n";
                    myfile00.close();
                    }

       if (mobility->getFullPath()=="RSUExampleScenario.node[1].veinsmobility")
              {
           EV<<"uploaded by 1-id";
                  EV<<"1-id "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<"\n";
              std::ofstream myfile1;
              myfile1.open("Example1_29mar_042test_up.txt",std::ios_base::app);
              myfile1<<"1-id "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<" "<<wsm->getCreationTime()<<"\n";
              myfile1.close();
              }

       if (mobility->getFullPath()=="RSUExampleScenario.node[2].veinsmobility")
              {
           EV<<"uploaded by 2-id";
                  EV<<"2-id "<<wsm->getFullPath()<<" "<<simTime()<<"\n";
              std::ofstream myfile2;
              myfile2.open("Example2_29mar_042test_up.txt",std::ios_base::app);
              myfile2<<"2-id "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<" "<<wsm->getCreationTime()<<"\n";
              myfile2.close();
              }

       if (mobility->getFullPath()=="RSUExampleScenario.node[5].veinsmobility")
              {
           EV<<"uploaded by 5-id";
                  EV<<"5-id "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<"\n";
              std::ofstream myfile5;
              myfile5.open("Example5_29mar_042test_up.txt",std::ios_base::app);
              myfile5<<"5-id "<<wsm->getFullPath()<<" "<<simTime()<<" "<<cc<<" "<<wsm->getCreationTime()<<"\n";
              myfile5.close();
              }
     }

    //if(intuniform(1,10)>7)
    //{
    else
    {
        std::string pre=" ";

           //std::string result =  (const char *)c;
          std::stringstream ss;

          ss<<wsm->getFullName()<<" "<<mobility->getFullPath();
          std::string result1=ss.str();
          wsm->setName(result1.c_str());
          EV<<"time difference"<<simTime()- wsm->getCreationTime()<<"\n";


      // WaveShortMessage* wsm1 = new WaveShortMessage(result1.c_str());
                   //c=c+1;
                 // populateWSM(wsm1);
                  //wsm1->setWsmData("created in wsm");

        std::string pre11=" ";
        //std::string result =  (const char *)c;
       std::stringstream ss11;

       ss<<cc<<"-"<<pre11;
       std::string result11=ss11.str();


       sendDelayedDown(wsm->dup(),cc);
    }
       // wsm1->setWsmData(result11.c_str());
    //scheduleAt(simTime()+cc,wsm->dup());
        //scheduleAt(simTime()+cc,wsm1);
        //sendDelayedDown(wsm1,cc);
    //}
        //delete(wsm);
        //sendDown(wsm->dup());
    //}
    //delete(wsm);
    //cSimulation::getActiveSimulation()->getFES();
    //cMessageHeap::Iterator it(heap);


    // Getting access of future event heap
    //cFutureEventSet* heap = cSimulation::getActiveSimulation()->getFES();

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



    /*
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

            if (!(std::string(event->getName()).compare(std::string(wsm->getName()))))
            {
                EV<<"Same name inside loop ";
                EV<<event->getName();
                EV<<"   ";
                EV<<wsm->getName();

               //cancelEvent(event);

                //delete(event);

                // deleting message from queue
                cEvent *removedEvent=heap->remove(event);
                i=i-1;
                length=heap->getLength();
                //cancelAndDelete(event);
                EV<<"Removed event";
                EV<<removedEvent;

            }
        }


    }

 */



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

    EV<<"ANUJ in self msg";
    /*if (WaveShortMessage* wsm = dynamic_cast<WaveShortMessage*>(msg)) {
      //  if(!wsm->isScheduled())
        //{
          //  sendDown(wsm->dup());
        //}
        sendDown(wsm->dup());
        cancelAndDelete(wsm);

        //send this message on the service channel until the counter is 3 or higher.
        //this code only runs when channel switching is enabled

        if (wsm->isScheduled())
            {

                //cancelAndDelete(wsm);
                EV<<"ANUJ dec scheduled";
                //delete(wsm);
            }
        else
        {
            EV<<"ANUJ dec";
            EV<<wsm->getSenderAddress();
            EV<<wsm->getSenderModuleId();




           // EV<<mySumoID;

            //wsm->getR
            EV<<wsm->getTreeId();
            //sendDown(wsm->dup());

            int cc= intuniform(1,10);
                if (cc==7)
                {
                    EV<<"value of cc is 7 "<<wsm->getFullName();
                    cancelAndDelete(wsm->dup());

            //scheduleAt(simTime()+intuniform(1,10),wsm->dup());
                }
                else
                {
                    sendDelayedDown(wsm->dup(),simTime()+cc);
                }

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
    */
    //}
    //BaseWaveApplLayer::handleSelfMsg(msg);

}


void TraCIDemo11p::handlePositionUpdate(cObject* obj) {
   // BaseWaveApplLayer::handlePositionUpdate(obj);

    cModule *tmpMobility = getParentModule()->getSubmodule("veinsmobility");
                    mobility = dynamic_cast<Veins::TraCIMobility*>(tmpMobility);
                    ASSERT(mobility);
                    EV<<"update hello dec anuj id";
                    EV<<mobility->getExternalId();
                    EV<<" update mobility name "<<mobility->getId()<<""<<mobility->getFullName()<<" "<<mobility->getFullPath()<<" ";

    EV<<"ANUJ4"<<"\n";
    EV<<"ANUJ4a"<<mobility->getRoadId().c_str()<<"\n";
    EV<<"ANUJ4b position"<<mobility->getPositionAt(simTime())<<"and"<<mobility->getCurrentPosition()<<"\n";
    //EV<<"ANUJ4c "<<traci->getTraCIXY(mobility->getCurrentPosition()) <<"\n";
    //traci->getLonLat(coord)

    std::pair<double,double> coordTraCI = traci->getTraCIXY(mobility->getCurrentPosition());
    EV<<"ANUJ4c"<<coordTraCI.first<<" "<<coordTraCI.second;

    static simtime_t previous_msg_generated=0;
    //static simtime_t previous_time=2;
    //static simtime_t increase=1;
    static int count=0;
    // data being created every second as this function is called every second
    static int  c=0;
    std::string pre="id ";
    //std::string result =  (const char *)c;
    std::stringstream ss;

    ss<<c<<"-"<<pre;
    std::string result=ss.str();
EV<<"time difference "<<simTime()-previous_msg_generated;
    //if ( c<1000 && (simTime()-previous_msg_generated>1))
    int ww=intuniform(1,10);
    //if ((c<10000)&& (count%30==0))
            if ((c<100000) && (ww<2))
    //if (simTime()-previous_msg_generated>1)
    {


        count+=1;
        EV<<"anuj new msg generated";
        previous_msg_generated = simTime();


        Veins::TraCICommandInterface* traci = mobility->getCommandInterface();
            Coord currPos = mobility->getCurrentPosition();
             std::pair<double, double> currLonLat = traci->getLonLat(currPos);
             EV<<"anuj current lon lat ";
             EV<<currLonLat.first<<" "<<currLonLat.second;


    WaveShortMessage* wsm = new WaveShortMessage(result.c_str());
    //WaveShortMessage* wsm = new WaveShortMessage();

    c=c+1;
    populateWSM(wsm);
    //wsm->setName(result.c_str());


    // setting msg contents as lat lon of current pos

    std::stringstream data;

        data<<currLonLat.first<<" "<<currLonLat.second<<" creator "<<mobility->getFullPath();
        std::string result_data=data.str();
     wsm->setWsmData(result_data.c_str());
    //wsm->setWsmData(mobility->getRoadId().c_str());
    //wsm->setWsmData(std::string(simTime()).c_str());
    EV<<"anuj kind of message "<<wsm->getKind()<<" \n";


    //scheduleAt(simTime()+intuniform(1,10),wsm);
    sendDelayedDown(wsm,intuniform(4,10));
    //sendDown(wsm);

    //wsm->setArrivalTime(simTime()+intuniform(1,10));
    //sendDown(wsm);
    }
    count+=1;
    //previous_time+=increase;


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

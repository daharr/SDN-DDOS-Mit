from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
import time

def dosSim():
    net = Mininet( controller=RemoteController )

    net.addController ('c0' , controller=RemoteController)

    ##build network
    # Add hosts and switches
    leftoneHost = net.addHost( 'h1' )
    lefttwoHost = net.addHost( 'h2' )
    rightoneHost = net.addHost( 'h3' )
    righttwoHost = net.addHost( 'h4' )
    sampleHost = net.addHost( 'h5' )
    leftSwitch = net.addSwitch( 's1' )
    rightSwitch = net.addSwitch( 's2' )
    centerSwitch = net.addSwitch( 's3' )

    # Add links
    net.addLink( leftoneHost, leftSwitch )
    net.addLink( lefttwoHost, leftSwitch )    
    net.addLink( rightoneHost, rightSwitch )
    net.addLink( righttwoHost, rightSwitch )
    net.addLink( leftSwitch, centerSwitch )
    net.addLink( rightSwitch, centerSwitch )
    net.addLink( sampleHost, centerSwitch )

    ##start network
    net.start()
    CLI( net )

    ##en network
    net.stop()

def mycmd( self, line ):
    "this command executes the scripts for traffic generation"
    net = self.mn
    h5 = net.get('h5')
    h1 = net.get('h1')
    #net.pingAll()
    h1.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h5.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T UDP -a 10.0.0.1 -c 100 -C 10 -t 15000 -l sender.log -x receiver.log')
CLI.do_mycmd = mycmd

if __name__ == '__main__':
    dosSim()

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
    leftthreeHost = net.addHost( 'h3' )
    leftfourHost = net.addHost( 'h4' )
    leftfiveHost = net.addHost( 'h5' )
    leftsixHost = net.addHost( 'h6' )
    leftsevenHost = net.addHost( 'h7' )
    lefteightHost = net.addHost( 'h8' )
    leftnineHost = net.addHost( 'h9' )
    lefttenHost = net.addHost( 'h10' )
    rightoneHost = net.addHost( 'h11' )
    righttwoHost = net.addHost( 'h12' )
    rightthreeHost = net.addHost( 'h13' )
    rightfourHost = net.addHost( 'h14' )
    rightfiveHost = net.addHost( 'h15' )
    rightsixHost = net.addHost( 'h16' )
    rightsevenHost = net.addHost( 'h17' )
    righteightHost = net.addHost( 'h18' )
    rightnineHost = net.addHost( 'h19' )
    righttenHost = net.addHost( 'h20' )
    leftSwitch = net.addSwitch( 's1' )
    rightSwitch = net.addSwitch( 's2' )
    centerSwitch = net.addSwitch( 's3' )

    # Add links
    net.addLink( leftoneHost, leftSwitch )
    net.addLink( lefttwoHost, leftSwitch )
    net.addLink( leftthreeHost, leftSwitch )
    net.addLink( leftfourHost, leftSwitch )  
    net.addLink( leftfiveHost, leftSwitch )
    net.addLink( leftsixHost, leftSwitch )  
    net.addLink( leftsevenHost, leftSwitch )
    net.addLink( lefteightHost, leftSwitch )  
    net.addLink( leftnineHost, leftSwitch )
    net.addLink( lefttenHost, leftSwitch )      
    net.addLink( rightoneHost, rightSwitch )
    net.addLink( righttwoHost, rightSwitch )
    net.addLink( rightthreeHost, rightSwitch )
    net.addLink( rightfourHost, rightSwitch )  
    net.addLink( rightfiveHost, rightSwitch )
    net.addLink( rightsixHost, rightSwitch )  
    net.addLink( rightsevenHost, rightSwitch )
    net.addLink( righteightHost, rightSwitch )  
    net.addLink( rightnineHost, rightSwitch )
    net.addLink( righttenHost, rightSwitch )
    net.addLink( leftSwitch, centerSwitch )
    net.addLink( rightSwitch, centerSwitch )

    ##start network
    net.start()
    CLI( net )

    ##en network
    net.stop()

##normal traffic command
def nortrafcmd( self, line ):
    "this command executes the scripts for traffic generation"
    net = self.mn
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')
    h19 = net.get('h19')
    h20 = net.get('h20')
    # send normal traffic through system
    h11.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h1.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.11 -c 200 -C 1 -t 150000 -l sender1.log -x receiver1.log &')
    h12.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h2.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.12 -c 200 -C 1 -t 150000 -l sender2.log -x receiver2.log &')
    h13.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h3.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.13 -c 200 -C 1 -t 150000 -l sender3.log -x receiver3.log &')
    h14.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h4.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.14 -c 200 -C 1 -t 150000 -l sender4.log -x receiver4.log &')
    h15.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h5.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.15 -c 200 -C 1 -t 150000 -l sender5.log -x receiver5.log &')
    h16.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h6.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.16 -c 200 -C 1 -t 150000 -l sender6.log -x receiver6.log &')
    h17.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h7.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.17 -c 200 -C 1 -t 150000 -l sender7.log -x receiver7.log &')
    h18.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h8.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.18 -c 200 -C 1 -t 150000 -l sender8.log -x receiver8.log &')
    h19.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h9.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.19 -c 200 -C 1 -t 150000 -l sender9.log -x receiver9.log &')
    h20.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h10.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.20 -c 200 -C 1 -t 150000 -l sender10.log -x receiver10.log &')

##mixed traffic
def mixtrafcmd( self, line ):
    "this command executes the scripts for traffic generation"
    net = self.mn
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')
    h19 = net.get('h19')
    h20 = net.get('h20')
    # send normal traffic through system
    h11.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h1.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.11 -c 200 -C 1 -t 150000 -l sender1.log -x receiver1.log &')
    h12.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h2.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.12 -c 200 -C 1 -t 150000 -l sender2.log -x receiver2.log &')
    h13.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h3.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.13 -c 300 -C 10 -t 150000 -l sender3.log -x receiver3.log &')
    h14.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h4.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.14 -c 200 -C 1 -t 150000 -l sender4.log -x receiver4.log &')
    h15.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h5.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.15 -c 200 -C 1 -t 150000 -l sender5.log -x receiver5.log &')
    h16.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h6.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.16 -c 300 -C 10 -t 150000 -l sender6.log -x receiver6.log &')
    h17.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h7.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.17 -c 200 -C 1 -t 150000 -l sender7.log -x receiver7.log &')
    h18.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h8.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.18 -c 200 -C 1 -t 150000 -l sender8.log -x receiver8.log &')
    h19.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h9.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.19 -c 300 -C 10 -t 150000 -l sender9.log -x receiver9.log &')
    h20.cmd( '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &' )
    h10.cmd('/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.20 -c 200 -C 1 -t 150000 -l sender10.log -x receiver10.log &')

CLI.do_nortrafcmd = nortrafcmd
CLI.do_mixtrafcmd = mixtrafcmd

if __name__ == '__main__':
    dosSim()

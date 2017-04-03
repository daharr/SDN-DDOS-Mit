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

##traffic command
def dostrafcmd( self, line ):
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
    recom = '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGRecv/ITGRecv &'
    secom = '/home/ubuntu/D-ITG-2.8.1-r1023/src/ITGSend/ITGSend -T TCP -a 10.0.0.'
    secom2 = ' -c 200 -C 1 -t 150000 -l sender'
    secom2b = ' -c 300 -C 10 -t 150000 -l sender'
    secom3 = '.log -x receiver'
    secom4 = '.log &'
    h11.cmd(recom)
    h12.cmd(recom)
    h13.cmd(recom)
    h14.cmd(recom)
    h15.cmd(recom)
    h16.cmd(recom)
    h17.cmd(recom)
    h18.cmd(recom)
    h19.cmd(recom)
    h20.cmd(recom)
    for i in range(1,10):
        h1.cmd(secom + str(i + 10) + secom2 + str(i) + '1' + secom3 + str(i) + '1' + secom4)
        h2.cmd(secom + str(i + 10) + secom2 + str(i) + '2' + secom3 + str(i) + '2' + secom4)  
        h3.cmd(secom + str(i + 10) + secom2 + str(i) + '3' + secom3 + str(i) + '3' + secom4)
        h4.cmd(secom + str(i + 10) + secom2 + str(i) + '4' + secom3 + str(i) + '4' + secom4)
        h5.cmd(secom + str(i + 10) + secom2 + str(i) + '5' + secom3 + str(i) + '5' + secom4)
        h6.cmd(secom + str(i + 10) + secom2 + str(i) + '6' + secom3 + str(i) + '6' + secom4)
        h7.cmd(secom + str(i + 10) + secom2 + str(i) + '7' + secom3 + str(i) + '7' + secom4)
        h8.cmd(secom + str(i + 10) + secom2 + str(i) + '8' + secom3 + str(i) + '8' + secom4)
        h9.cmd(secom + str(i + 10) + secom2 + str(i) + '9' + secom3 + str(i) + '9' + secom4)
        h10.cmd(secom + str(i + 10) + secom2 + str(i) + '10' + secom3 + str(i) + '10' + secom4)
    h1.cmd(secom + str(20) + secom2 + '101' + secom3 + '101' + secom4)
    h2.cmd(secom + str(20) + secom2 + '102' + secom3 + '102' + secom4)  
    h3.cmd(secom + str(20) + secom2 + '103' + secom3 + '103' + secom4)
    h4.cmd(secom + str(20) + secom2 + '104' + secom3 + '104' + secom4)
    h5.cmd(secom + str(20) + secom2 + '105' + secom3 + '105' + secom4)
    h6.cmd(secom + str(20) + secom2 + '106' + secom3 + '106' + secom4)
    h7.cmd(secom + str(20) + secom2 + '107' + secom3 + '107' + secom4)
    h8.cmd(secom + str(20) + secom2 + '108' + secom3 + '108' + secom4)
    h9.cmd(secom + str(20) + secom2 + '109' + secom3 + '109' + secom4)
    h10.cmd(secom + str(20) + secom2 + '1010' + secom3 + '1010' + '.log')
    
    ##begin ddos traffic
    h11.cmd(recom)
    h12.cmd(recom)
    h13.cmd(recom)
    h14.cmd(recom)
    h15.cmd(recom)
    h16.cmd(recom)
    h17.cmd(recom)
    h18.cmd(recom)
    h19.cmd(recom)
    h20.cmd(recom)
    for i in range(1,11):
        h1.cmd(secom + str(i + 10) + secom2 + str(i) + '1' + secom3 + str(i) + '1' + secom4)
        h2.cmd(secom + str(i + 10) + secom2 + str(i) + '2' + secom3 + str(i) + '2' + secom4)  
        h3.cmd(secom + str(i + 10) + secom2b + str(i) + '3' + secom3 + str(i) + '3' + secom4)
        h4.cmd(secom + str(i + 10) + secom2 + str(i) + '4' + secom3 + str(i) + '4' + secom4)
        h5.cmd(secom + str(i + 10) + secom2 + str(i) + '5' + secom3 + str(i) + '5' + secom4)
        h6.cmd(secom + str(i + 10) + secom2b + str(i) + '6' + secom3 + str(i) + '6' + secom4)
        h7.cmd(secom + str(i + 10) + secom2 + str(i) + '7' + secom3 + str(i) + '7' + secom4)
        h8.cmd(secom + str(i + 10) + secom2 + str(i) + '8' + secom3 + str(i) + '8' + secom4)
        h9.cmd(secom + str(i + 10) + secom2b + str(i) + '9' + secom3 + str(i) + '9' + secom4)
        h10.cmd(secom + str(i + 10) + secom2 + str(i) + '10' + secom3 + str(i) + '10' + secom4)


CLI.do_dostrafcmd = dostrafcmd

if __name__ == '__main__':
    dosSim()

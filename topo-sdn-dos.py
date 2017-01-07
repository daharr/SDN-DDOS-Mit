"""Custom topology example

5 hosts
4 lower hosts for handling traffic
1 host for sampling data connected to centerswitch
3 switches
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftoneHost = self.addHost( 'h1' )
	lefttwoHost = self.addHost( 'h2' )
        rightoneHost = self.addHost( 'h3' )
        righttwoHost = self.addHost( 'h4' )
	sampleHost = self.addHost( 'h5' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )
	centerSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftoneHost, leftSwitch )
	self.addLink( lefttwoHost, leftSwitch )
        
        self.addLink( rightoneHost, rightSwitch )
	self.addLink( righttwoHost, rightSwitch )

	self.addLink( leftSwitch, centerSwitch )
	self.addLink( rightSwitch, centerSwitch )

	self.addLink( sampleHost, centerSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }

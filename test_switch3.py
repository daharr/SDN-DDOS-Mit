
#import statements
from ryu.app import simple_switch_13
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, DEAD_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib import hub
import Update3

class SamplerSwitch(simple_switch_13.SimpleSwitch13):

    def __init__(self, *args, **kwargs):
        super(SamplerSwitch, self).__init__(*args, **kwargs)
        self.datapaths = {}
        self.monitor_thread = hub.spawn(self._monitor) #hub that will query switches

    @set_ev_cls(ofp_event.EventOFPStateChange,
                [MAIN_DISPATCHER, DEAD_DISPATCHER])
    def _state_change_handler(self, ev):
        datapath = ev.datapath
        if ev.state == MAIN_DISPATCHER:
            if not datapath.id in self.datapaths:
                self.logger.debug('register datapath: %016x', datapath.id)
                self.datapaths[datapath.id] = datapath
        elif ev.state == DEAD_DISPATCHER:
            if datapath.id in self.datapaths:
                self.logger.debug('unregister datapath: %016x', datapath.id)
                del self.datapaths[datapath.id]

    def _monitor(self):
        while True:
            for dp in self.datapaths.values():
                self._request_stats(dp)
                self.clear_flows(dp)
            hub.sleep(10)

    def _request_stats(self, datapath):
        if datapath.id == 0000000000000002:
            self.logger.debug('send stats request: %016x', datapath.id)
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser
            req = parser.OFPFlowStatsRequest(datapath)
            datapath.send_msg(req)

    def clear_flows(self, datapath):
        if datapath.id == 0000000000000002:
            self.logger.debug('send stat clear: %016x', datapath.id)
            parser = datapath.ofproto_parser
            ofproto = datapath.ofproto
            actions = [parser.OFPActionOutput(ofproto.OFPP_NORMAL, 0)]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
            for i in range(1,12):
                req = parser.OFPFlowMod(datapath, 0, 0, 0, ofproto.OFPFC_MODIFY, 0, 0, 1, ofproto.OFP_NO_BUFFER, ofproto.OFPP_ANY, ofproto.OFPG_ANY, ofproto.OFPFF_RESET_COUNTS, parser.OFPMatch(in_port= i ), inst)
                datapath.send_msg(req)

    @set_ev_cls(ofp_event.EventOFPFlowStatsReply, MAIN_DISPATCHER)
    def _flow_stats_reply_handler(self, ev):
        body = ev.msg.body
        flows = []
        self.logger.info('datapath         '
                         'in-port  out-port  eth-dst           '
                         'eth-src           packets  bytes   '
                         'ip-src            ip-dst           ')
        self.logger.info('---------------- '
                         '--------  -------- ----------------- '
                         '----------------- -------- --------'
                         '----------------- -----------------')
        for stat in sorted([flow for flow in body if flow.priority == 1]):
            src = None
            if 'eth_src' in stat.match:
                src = stat.match['eth_src']
            self.logger.info('%016x %8x %8x %17s %17s %8d %8d',
                             ev.msg.datapath.id,
                             stat.match['in_port'],
                             stat.instructions[0].actions[0].port, 
                             stat.match['eth_dst'],
                             src,
                             stat.packet_count, stat.byte_count)#,
#                            stat.match['ipv4_src'], stat.match['ipv4_dst'])
            flows.append(stat)
			
        while len(flows) > 0:
			flowcount = 1.0
			bytecount = 0;
			packetcount = 0;
            for i in range(1, len(flows)):
			    if flows[0].match['eth_dst'] == flows[i].match['eth_dst']:
				    bytecount = flows[i].byte_count + bytecount
					packetcount = flows[i].packet_count + packetcount
					del flows[i]
					i--
            Update3.Update_CP(flows[0].instructions[0].actions[0].port,flows[0].match['eth_dst'], (flows[0].byte_count + bytecount) / count, (packetcount + flows[0].packet_count) / count)
			del flows[0]

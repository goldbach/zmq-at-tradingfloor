import zmq
import logging

log = logging.getLogger()

logging.basicConfig(level=logging.INFO)

ctx = zmq.Context()
in_sock  = ctx.socket(zmq.PULL)
out_sock = ctx.socket(zmq.PUB)

in_addr = "tcp://0.0.0.0:5001"
out_addr = "tcp://0.0.0.0:5002"

in_sock.bind(in_addr)
out_sock.bind(out_addr)

log.info("Receiving quotes on %s", in_addr)
log.info("Sending quotes on %s", out_addr)

while True:
	(topic, msg) = in_sock.recv_multipart()
	log.info("forwarding on topic %s: %s", topic, msg)
	out_sock.send_multipart([topic, msg, ])

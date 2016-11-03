import zmq
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

broker_addr = "tcp://localhost:5002"
ctx = zmq.Context()
s = ctx.socket(zmq.SUB)

log.info("Connecting to %s", broker_addr)
s.connect(broker_addr)

log.info("Subscibing to everything")
s.setsockopt(zmq.SUBSCRIBE, b'')

while True:
	(topic, msg) = s.recv_multipart()
	log.info("Got topic %s with msg %s", topic, msg)


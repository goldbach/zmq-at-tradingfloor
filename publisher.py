import zmq
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--broker', dest='broker', action='append', default=[])


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

broker_addr = "tcp://localhost:5001"

ctx = zmq.Context()
s = ctx.socket(zmq.PUSH)

log.info("Connecting to %s", broker_addr)
s.connect(broker_addr)

log.info("Sending quotes")
while True:
	s.send_multipart([b"FX.USD/EUR", b"42"])



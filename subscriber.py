import zmq
import logging
import argparse

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('--broker', dest='brokers', action='append', default=[])
	args = parser.parse_args()

	if len(args.brokers) == 0:
		args.brokers = ["localhost:5002", ]

	args.brokers = ["tcp://%s" % x for x in args.brokers]
	return args


def main(args):

	ctx = zmq.Context()
	s = ctx.socket(zmq.SUB)

	for broker in args.brokers:
		log.info("Connecting to %s", broker)
		s.connect(broker)

	log.info("Subscibing to everything")
	s.setsockopt(zmq.SUBSCRIBE, b'')

	while True:
		topic, msg = s.recv_multipart()
		log.info("Got topic %s with msg %s", topic, msg)

if __name__ == "__main__":
	main(parse())
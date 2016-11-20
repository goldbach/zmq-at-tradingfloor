import zmq
import logging
import argparse

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger()

def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('--broker', dest='brokers', action='append', default=[])
	args = parser.parse_args()

	if len(args.brokers) == 0:
		args.brokers = ["localhost:5001", ]

	args.brokers = ["tcp://%s" % x for x in args.brokers]
	return args


def main(args):

	ctx = zmq.Context()
	s = ctx.socket(zmq.PUSH)

	for broker in args.brokers:
		log.info("Connecting to %s", broker)
		s.connect(broker)

	log.info("Sending quotes")
	while True:
		s.send_multipart([b"FX.USD/EUR", b"0.95"])


if __name__ == "__main__":
	main(parse())

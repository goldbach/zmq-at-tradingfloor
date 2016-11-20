import zmq
import logging
import argparse

log = logging.getLogger()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

parser = argparse.ArgumentParser()
parser.add_argument('--in-port', dest='in_port', type=int, default=5001)
parser.add_argument('--out-port', dest='out_port', type=int, default=5002)


def main(args):
	ctx = zmq.Context()
	in_sock  = ctx.socket(zmq.PULL)
	out_sock = ctx.socket(zmq.PUB)

	in_addr = "tcp://0.0.0.0:%d" % args.in_port
	out_addr = "tcp://0.0.0.0:%d" % args.out_port

	in_sock.bind(in_addr)
	out_sock.bind(out_addr)

	log.info("Receiving quotes on %s", in_addr)
	log.info("Sending quotes on %s", out_addr)

	while True:
		topic, msg = in_sock.recv_multipart()
		log.info("forwarding on topic %s: %s", topic, msg)
		out_sock.send_multipart([topic, msg, ])


if __name__ == "__main__":
	args = parser.parse_args()
	main(args)
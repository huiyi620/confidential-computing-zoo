#
# Copyright (c) 2022 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC ratls.Greeter client."""

from __future__ import print_function
import logging
import argparse

import grpc

import ratls_pb2
import ratls_pb2_grpc


def run(args):
    credentials = grpc.sgxratls_channel_credentials(config_json=args.config)
    channel = grpc.secure_channel(args.host, credentials)
    stub = ratls_pb2_grpc.GreeterStub(channel)

    user_a = stub.SayHello(ratls_pb2.HelloRequest(name='a'))
    user_b = stub.SayHello(ratls_pb2.HelloRequest(name='b'))

    print("Greeter client received: ", user_a.message, user_b.message)

    channel.close()

def command_arguments():
    parser = argparse.ArgumentParser(description='GRPC client.')
    parser.add_argument(
        '-host',
        '--host',
        type=str,
        required=False,
        default='localhost:50051',
        help='The server socket address.'
    )
    parser.add_argument(
        '-cfg',
        '--config',
        type=str,
        required=False,
        default='dynamic_config.json',
        help='The path of dynamic config json'
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = command_arguments()
    logging.basicConfig()
    run(args)

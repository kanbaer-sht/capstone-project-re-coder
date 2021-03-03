import janusTracking
import getJanus
import janusTrackingv2
import argparse
import asyncio
import json
import logging
import os
import ssl
import uuid
import aiohttp
import socketio

from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaBlackhole, MediaPlayer, MediaRecorder

'''
parser = argparse.ArgumentParser(description="Janus")
parser.add_argument("url", help="Janus root URL, e.g. http://localhost:8088/janus")
parser.add_argument(
    "--room",
    type=int,
    default=1234,
    help="The video room ID to join (default: 1234).",
),
parser.add_argument("--test-id", type=int, help="TestId"),
parser.add_argument("--play-from", help="Read the media from a file and sent it."),
parser.add_argument("--record-to", help="Write received media to a file."),
parser.add_argument("--verbose", "-v", action="count")
args = parser.parse_args()
print(args)
'''


def callJanus(url, room, test_id, s_number):
    getJanus.janus_connection(url, room, test_id, s_number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Janus")
    parser.add_argument("url", help="Janus URL")
    parser.add_argument("room", type=int, help="room ID to join")
    parser.add_argument("test_id", type=int, help="test_id")
    parser.add_argument("s_number", type=int, help="s_number")
    args = parser.parse_args()

    callJanus(url="https://re-coder.net/janus", room=args.room, test_id=args.test_id, s_number=args.s_number)
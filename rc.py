from pprint import pprint
from array import array

def load_endpoint(fd):
    latency, cache_lines = [int(v) for v in fd.readline().split()]
    ep = {}
    for _ in range(cache_lines):
        cache_id, latency = [int(v) for v in fd.readline().split()]
        ep[cache_id] = latency
    return ep

def load(fname):
    with open(fname) as fd:
        video_count, endpoints_count, _, caches, cache_size = [int(v) for v in fd.readline().split()]
        video_sizes = [int(v) for v in fd.readline().split()]

        videos = []
        for _ in range(video_count):
            eps = array('I')
            eps.fromlist([0 for _ in range(endpoints_count)])
            videos.append(eps)
        videos = tuple(videos)

        endpoints = []
        for ep_id in range(endpoints_count):
            endpoints.append(load_endpoint(fd))
        for line in fd:
            vid_id, ep_id, counts = [int(v) for v in fd.readline().split()]
            videos[vid_id][ep_id] = counts
        return videos, endpoints


def __main__():
    import sys
    from time import sleep
    videos, endpoints = load(sys.argv[1])
    sleep(60)
    pprint(videos)

__main__()

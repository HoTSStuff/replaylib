#!/usr/bin/env python
"""
This file will take sample a replay and generate a heatmap.

This heatmap is based on all death events found during the replay.
"""
import heatmap as hm
import ReplayLib


def shapes_generator(events):
    for event in events:
        yield hm.Point(hm.LatLon(event['m_y'], event['m_x']),)


def setup_config(deaths):
    config = hm.Configuration()
    config.shapes = shapes_generator(deaths)
    config.projection = hm.EquirectangularProjection()
    config.projection.pixels_per_degree = 5
    config.decay = .9
    config.kernel = hm.LinearKernel(7)
    config.background = 'black'
    config.fill_missing()
    return config


def main():
    print "Starting processing"
    replay_file = '2.StormReplay'
    replay = ReplayLib.Replay(replay_file)
    deaths = replay.get_deaths()
    print "Starting heatmap generation"
    config = setup_config(deaths)
    matrix = hm.process_shapes(config)
    matrix = matrix.finalized()
    image = hm.ImageMaker(config).make_image(matrix)
    image.save('sample.png')
    print "Complete"

if __name__ == "__main__":
    main()

from math import pi, acos, degrees
import drawSvg as draw
import os


def get_start_end_degrees(radius, length, height):
    if radius <= length:
        start = 180
    else:
        start = 180 + degrees(acos(length/radius))
    if radius <= height:
        end = 270
    else:
        end = 270 - degrees(acos(height/radius))
    return start, end


def get_degree_per_bit(radius, bit_length):
    return (bit_length*360)/(2*radius*pi)


def to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def plot_dvd(filename, length, height, data, bit_length, stroke, spacing=None, overflow_text="created by Carl and Moritz"):
    d = draw.Drawing(length, height, origin=(-length, -height))
    data = to_bits(data)
    overflow_text = to_bits(overflow_text)
    current_index = 0
    radius = 0
    if spacing is None:
        spacing = stroke
    i = 0
    new_name = filename
    while os.path.exists(new_name):
        new_name = filename[0:-4] + str(i) + ".svg"
        i += 1
    filename = new_name
    while radius < length + height:
        radius += stroke + spacing
        start, end = get_start_end_degrees(radius, length, height)
        degree_per_bit = get_degree_per_bit(radius, bit_length)
        cur_start = -1
        while start < end - degree_per_bit:
            if current_index < len(data):
                current_val = data[current_index]
            else:
                current_val = overflow_text[current_index % len(overflow_text)]
            current_index += 1
            if current_val == 1 and cur_start == -1:
                cur_start = start
            elif current_val == 0 and cur_start != -1:
                d.append(draw.Arc(0, 0, radius, cur_start, start, cw=False,
                                  stroke='black', stroke_width=stroke, fill='none'))
                cur_start = -1
            start += degree_per_bit
        if cur_start != -1:
            d.append(draw.Arc(0, 0, radius, cur_start, start, cw=False,
                              stroke='black', stroke_width=stroke, fill='none'))
    d.saveSvg(filename)
    return filename




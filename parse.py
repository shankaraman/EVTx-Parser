from collections import OrderedDict
from binascii import hexlify

file_obj = open('./Application.evtx', 'rb')
data = file_obj.read()
file_obj.close()

size_of_file_header = 4096
size_of_chunk = 65536
size_of_chunk_header = 512

file_header = OrderedDict()
file_header['signature'] = 8
file_header['first_chunk_number'] = 8
file_header['last_chunk_number'] = 8
file_header['next_record_id'] = 8
file_header['header_size'] = 4
file_header['minor_version'] = 2
file_header['major_version'] = 2
file_header['header_block_size'] = 2
file_header['number_of_chunks'] = 2
file_header['unknown1'] = 76
file_header['file_flags'] = 4
file_header['checksum'] = 4
file_header['unknown2'] = 3968

chunk_header = OrderedDict()
chunk_header['signature'] = 8
chunk_header['first_event_record_number'] = 8
chunk_header['last_event_record_number'] = 8
chunk_header['first_event_id'] = 8
chunk_header['last_event_id'] = 8
chunk_header['header_size'] = 40



index = 0
for header, value in file_header.items():
    try:
        print(header, hexlify(data[index: index + value]), index)
    except Exception as msg:
        print(msg)
    index += value


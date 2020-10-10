import ray

def init_cluster(ip_address, port):
    import random
    if ip_address in ['localhost','127.0.0.1']:
        ray.init()
    else:
        ray_address = "{}:{}".format(ip_address, port)
        ray.init(address=ray_address)
    return random.randint(0, 9999)

def run_mapred(input_data, map_fn, reduce_fn, output_location):
    from mapreduce.raymapreduce import RayMapReduce
    import glob
    mapred = RayMapReduce(map_fn, reduce_fn)
    input_files = glob.glob(input_data)
    result = mapred(input_files)
    with open(output_location, 'w') as filehandle:
        filehandle.writelines("{}\n".format(r) for r in result)
    return result

def destroy_cluster(cluster_id):
    ray.shutdown()
    
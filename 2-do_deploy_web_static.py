#!/usr/bin/python3

"""
This script distributes an archive to your web servers,
using the function do_deploy:
"""


from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.237.33.154', '3.85.1.156']


def do_deploy():
    """distributes an archive to the web server"""
    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        not_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f'mkdir -p {path}{not_ext}/')
        run(f'tar -xzf /tmp/{file_n} -C {path}{not_ext}/')
        run(f'rm /tmp/{file_n}')
        run('mv {0}{1}/web_static/* {0}{1}'.format(path, not_ext))
        run(f'rm -rf {path}{not_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {path}{not_ext}/ /data/web_static/current')
        return True
    except Exception as e:
        return False
#!/usr/bin/python3
""" This script make a full deployment """

from datetime import datetime
from fabric.api import local
from fabric.api import put, run, env
import os
env.hosts = ['54.237.33.154', '3.85.1.156']


def do_pack():
    """This function generates a tgz archive"""
    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if not os.path.isdir("versions"):
            local("mkdir -p versions")
        file_name = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except Exceptio as e:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web server"""
    if not os.path.exists(archive_path):
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


def deploy():
    """
    This function creates and distributes
    an archive to the web server
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

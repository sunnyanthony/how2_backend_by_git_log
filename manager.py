import socket, select
import signal, os
import logging

logging.basicConfig(filename='/data/socket_server.log', encoding='utf-8', level=logging.DEBUG)

def signal_handler(sig, frame):
    print(f'game over {sig} {frame}')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as fd:
    conn = None
    fd.bind(('', 1234))
    fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fd.listen(2)
    fd.setblocking(0)
    fd_lists = {fd.fileno()}

    epoll = select.epoll()
    epoll.register(fd.fileno(), select.EPOLLIN | select.EPOLLOUT | select.EPOLLPRI | select.EPOLLHUP | select.EPOLLERR )
    logging.info('wait client')
    events = epoll.poll()
    if not events:
        logger.warring('listen failed')
        sys.exit(1)

    logging.info('try to get data')
    try:
        for s, event in events:
            if s not in fd_lists:
                continue
            conn, _ = fd.accept()
            logging.info('connected')
        if conn is None:
            raise
        epoll.unregister(fd.fileno())
        fd_lists.remove(fd.fileno())
        epoll.register(conn)
        fd_lists.update([conn.fileno()])
        while True:
            events = epoll.poll()
            for s, event in events:
                if s not in fd_lists:
                    continue
                fd.setblocking(True)
                data = conn.recv(1024).decode()
                logging.info(f'get {data}')
                conn.send("Roger".encode())
    except Exception as e:
        logging.exception(f'{e}')

logging.info('abort')

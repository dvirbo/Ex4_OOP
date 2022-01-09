"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
from threading import Thread
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from pygame.constants import RESIZABLE
from main_code.graphAlgo import GraphAlgo
import time

start = time.time()
# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('Ex4 by Dvir & Yuval')
# counter:
MOVE_COUNTER = 0
font = pygame.font.SysFont("verdana", 20)  # step 1 - load a font
clock = pygame.time.Clock()
pygame.font.init()
client = Client()
client.start_connection(HOST, PORT)

pokemons = client.get_pokemons()
graph_json = client.get_graph()
main_graph = GraphAlgo()
main_graph.load_json(graph_json)  # only one time..
main_graph.distances_nodes()

FONT = pygame.font.SysFont('Arial', 20, bold=True)
max_x, min_x, max_y, min_y = main_graph.getMin()
# LOAD AND SCALE ALL THE NEEDED PICTURES:
programIcon = pygame.image.load("../pictures/icon.png")
programIcon = pygame.transform.scale(programIcon, (35, 35))
pygame.display.set_icon(programIcon)
pic1 = pygame.image.load("../pictures/pic1.png")
pic1 = pygame.transform.scale(pic1, (35, 35))
pic2 = pygame.image.load("../pictures/pic2.png")
pic2 = pygame.transform.scale(pic2, (35, 35))
ash = pygame.image.load("../pictures/ash.png")
ash = pygame.transform.scale(ash, (35, 35))


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


def load_pok():
    pok = client.get_pokemons()
    main_graph.load_Pokemon(pok)


def show_moves():
    count = font.render("Move count :" + str(MOVE_COUNTER), True, (255, 255, 255))
    screen.blit(count, (0.5, 0.5))


def show_time():
    timer = font.render("Run time: " + str(time.time() - start), True, (255, 255, 255))
    screen.blit(timer, (0.5, 23))


def show_score(data: float):
    score = font.render("score: " + str(data), True, (255, 255, 255))
    screen.blit(score, (0.5, 80))


def my_move(seconds):
    """
    :param seconds: the second that the move will sleep
    :return:
    """
    client.move()
    global MOVE_COUNTER
    MOVE_COUNTER += 1
    time.sleep(seconds)


radius = 15
data = json.loads(client.get_info())
agentNum = data["GameServer"]["agents"]
# check how much agents there is in the game:
if agentNum == 1:
    client.add_agent("{\"id\":1}")
elif agentNum == 2:
    client.add_agent("{\"id\":1}")
    client.add_agent("{\"id\":2}")
else:
    client.add_agent("{\"id\":1}")
    client.add_agent("{\"id\":2}")
    client.add_agent("{\"id\":3}")

main_graph.load_agents(client.get_agents(), agentNum)
my_agents = main_graph.agents  # list of all the agents
thread = Thread(target=my_move, args=(1,), name="move_thread")

# this commnad starts the server - the game is running now
client.start()
thread.start()
thread.join()
timer = 0

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""
while client.is_running() == 'true':
    main_graph.load_Pokemon(client.get_pokemons())
    main_graph.load_agents(client.get_agents(),agentNum)
    pokemons = json.loads(client.get_pokemons(),
                          object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
        # need to send the pos of the poc to function that check if the poc is on d<s or else
        if p.type == -1:  # draw the pokemons different to debug
            screen.blit(pic1, (p.pos.x - 5, p.pos.y - 10))
        else:
            screen.blit(pic2, (p.pos.x - 5, p.pos.y - 10))

    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))

    # refresh surface
    screen.fill(Color(0, 0, 0))
    # draw nodes
    for n in main_graph.Nodes.values():
        x = my_scale(n.pos[0], x=True)
        y = my_scale(n.pos[1], y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.key), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for e in main_graph.Edges:
        # find the edge nodes
        src = next(n for n in main_graph.Nodes.values() if n.key == e.src)
        dest = next(n for n in main_graph.Nodes.values() if n.key == e.dest)

        # scaled positions
        src_x = my_scale(src.pos[0], x=True)
        src_y = my_scale(src.pos[1], y=True)
        dest_x = my_scale(dest.pos[0], x=True)
        dest_y = my_scale(dest.pos[1], y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        screen.blit(ash, (int(agent.pos.x), int(agent.pos.y)))

    for p in pokemons:
        # need to send the pos of the poc to function that check if the poc is on d<s or else
        if p.type == -1:  # draw the pokemons different to debug
            screen.blit(pic1, (p.pos.x - 5, p.pos.y - 10))
        else:
            screen.blit(pic2, (p.pos.x - 5, p.pos.y - 10))

    # check events to stop the game:
    stop = FONT.render('click to stop', True, Color(255, 255, 255))
    button = stop.get_rect(center=(41, 61), size=(110, 34))
    pygame.draw.rect(screen, (100, 100, 100), button)
    screen.blit(stop, (5, 50))

    data = json.loads(client.get_info())
    score = data["GameServer"]["grade"]
    show_score(score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                client.stop()

    # update screen changes
    show_moves()
    show_time()
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    for agent in my_agents:
        if agent.dest != -1:
            continue
        dist, path, pokemon = main_graph.allocateAgent(agent)
        if dist == -1:
            continue
        if float(dist) == 0.0:
            client.choose_next_edge(
                '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(pokemon.edge.src) + '}')
            timer = 0.1115
        else:
            client.choose_next_edge(
                '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(path[1]) + '}')

            ttl = client.time_to_end()
            print(ttl, client.get_info())
            timer = 0.135
            """
            t = 0.135
            change the time that the "move" sleep in case that the agent stand on the src of the edge that
            the pokemon is on
            {"GameServer":{"pokemons":3,"is_logged_in":false,"moves":197,"grade":58,"game_level":8,"max_user_level":-1,"id":0,"graph":"data/A2","agents":1}}
            """
    my_move(timer)
# game over:
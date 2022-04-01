from abc import ABC
from random import randrange
from typing import Union
import pygame
from classes.Cell import Cell
from classes.Entity import Entity
from classes.Food import Food
from classes.Movement import Coordinates, Corners
from classes.Settings import Settings
import sys
from classes.Statistics import Statistics

if Settings.FPS: 
    pygame.init()

class Simulation(ABC):
    Clock: Union[pygame.time.Clock, None] = None
    Screen: Union[pygame.Surface, None] = None
    Paused: bool = False

    days: int = 0

    def _draw() -> None:
        Simulation.Screen.fill('#000000')
        length = max(len(Entity.cells), len(Entity.food))
        for i in range(length):
            if i < len(Entity.cells):
                pygame.draw.rect(Simulation.Screen, Entity.cells[i].COLOR, Entity.cells[i].asRect())
            if i < len(Entity.food):
                pygame.draw.rect(Simulation.Screen, Entity.food[i].COLOR, Entity.food[i].asRect())
        pygame.display.flip()

    def _catchEvents() -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Simulation.Paused = not Simulation.Paused

    def initialize() -> None:
        if Settings.FPS:
            Simulation.Clock = pygame.time.Clock()
            Simulation.Screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        for _ in range(Settings.CELLS):
            coordinates: Coordinates = None
            match randrange(0, 4):
                case 0: coordinates = Corners.TOP_LEFT()
                case 1: coordinates = Corners.TOP_RIGHT()
                case 2: coordinates = Corners.BOTTOM_LEFT()
                case _: coordinates = Corners.BOTTOM_RIGHT()
            Cell(coordinates, Settings.SIZE, '#fff2f5', Settings.SPEED, Settings.SENSE).spawn()
        Food.generate()
        Cell.startGeneration()
            

    def run() -> bool:
        if (not len(Entity.cells) or len(Statistics.all) >= Settings.GENERATIONS): return False
        if (Settings.FPS):
            Simulation.Clock.tick(Settings.FPS)
            Simulation._catchEvents()
            Simulation._draw()
        if not Simulation.Paused:
            if Cell.areAllHome():
                Cell.endGeneration()
                Food.generate()
                Cell.startGeneration()
            for cell in Entity.cells:
                cell: Cell
                cell.executeState()
        return True
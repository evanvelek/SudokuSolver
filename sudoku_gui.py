import pygame
from sudoku_solver import solve
from sudoku_solver import is_valid

def draw_grid(surface:pygame.display, grid: list[list[int]], x_lines: list[float], y_lines: list[float]) -> None:
    'Draws the board'
    width = surface.get_width()
    height = surface.get_height()
    for i in range(0, 10):
        line_width = 2
        if i % 3 == 0:
            line_width = 6
        pygame.draw.line(surface, pygame.Color(0, 0, 0),
                         (i * (width - 20) / 9 + 10, 10),
                         (i * (width - 20) / 9 + 10, height - 10),
                         width = line_width)
        pygame.draw.line(surface, pygame.Color(0, 0, 0),
                         (10, i * (height - 20) / 9 + 10),
                         (width - 10, i * (height - 20) / 9 + 10),
                         width = line_width)
def update_surface(surface:pygame.display, selected_tile: tuple[int, int] | None, x_lines: list[int|float], y_lines: list[int|float], outline_color:pygame.Color, queued_number: int | None, grid: list[list[int]], original_grid:list[list[int]]) -> None:
    'Enacts any changes to the gui'
    surface.fill((255, 255, 255))
    draw_grid(surface, grid, x_lines, y_lines)
    if selected_tile != None:
        x1 = x_lines[selected_tile[0]]
        x2 = x_lines[selected_tile[0] + 1]
        y1 = y_lines[selected_tile[1]]
        y2 = y_lines[selected_tile[1] + 1]
        if selected_tile[0] % 3 == 0:
            x1 += 4
        else:
            x1 += 2
            x2 += 1
        if selected_tile[1] % 3 == 0:
            y1 += 4
        else:
            y1 += 2
            y2 += 1
        if selected_tile[0] == 6:
            x2 += 1
        rec = pygame.Rect(x1, y1, x2-x1, y2-y1)
        inner_rec = pygame.Rect(x1 + 4, y1 + 4, x2-x1-8, y2-y1-8)
        pygame.draw.rect(surface, outline_color, rec)
        pygame.draw.rect(surface, pygame.Color(255, 255, 255), inner_rec)


    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            x1 = x_lines[col_index]
            x2 = x_lines[col_index + 1]
            y1 = y_lines[row_index]
            y2 = y_lines[row_index + 1]
            if grid[row_index][col_index] != 0:
                if grid[row_index][col_index] == original_grid[row_index][col_index]:
                    color = pygame.Color((0, 0, 0))
                else:
                    color = pygame.Color((0, 0, 155))
                font = pygame.font.SysFont('Helvetica', surface.get_height() // 15)
                text = font.render(str(grid[row_index][col_index]), True, color)
                text_rect = text.get_rect()
                text_rect.center = ((x1 + x2) / 2, (y1 + y2) / 2)
                surface.blit(text, text_rect)






    pygame.display.flip()


def run():
    pygame.init()

    original_grid = [
        [3, 0, 0, 0, 4, 0, 0, 7, 0],
        [0, 0, 6, 0, 2, 0, 0, 0, 0],
        [5, 0, 0, 7, 0, 6, 0, 0, 9],
        [0, 0, 5, 3, 0, 1, 0, 2, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 1, 5, 0, 7, 0, 3, 0]
    ]
    grid = [
        [3, 0, 0, 0, 4, 0, 0, 7, 0],
        [0, 0, 6, 0, 2, 0, 0, 0, 0],
        [5, 0, 0, 7, 0, 6, 0, 0, 9],
        [0, 0, 5, 3, 0, 1, 0, 2, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 1, 5, 0, 7, 0, 3, 0]
    ]

    surface = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    running = True
    surface.fill((255, 255, 255))
    selected_tile = None
    x_lines = [x * (surface.get_width() - 20) / 9 + 10 for x in range(10)]
    y_lines = [y * (surface.get_height() - 20) / 9 + 10 for y in range(10)]
    outline_color = pygame.Color(0, 0, 200)
    queued_number = None
    draw_grid(surface, grid, x_lines, y_lines)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                x_lines = [x * (surface.get_width() - 20) / 9 + 10 for x in range(10)]
                y_lines = [y * (surface.get_height() - 20) / 9 + 10 for y in range(10)]
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos = event.pos[0]
                y_pos = event.pos[1]
                x_val = None
                y_val = None
                for index in range(len(x_lines) - 1):
                    if x_lines[index] < x_pos < x_lines[index + 1]:
                        x_val = index
                for index in range(len(y_lines) - 1):
                    if y_lines[index] < y_pos < y_lines[index + 1]:
                        y_val = index
                if x_val != None and y_val != None:
                    selected_tile = (x_val, y_val)
                    outline_color = pygame.Color(0, 0, 200)
            if event.type == pygame.KEYDOWN:
                a = event.key
                if a == 49 or a == 50 or a == 51 or a == 52 or a == 53 or a == 54 or a == 55 or a == 56 or a == 57:
                    if selected_tile:
                        before_list = [] #so id's aren't the same
                        for row in grid:
                            before_list.append([])
                            for val in row:
                                before_list[-1].append(val)
                        if not grid[selected_tile[1]][selected_tile[0]]:
                            grid[selected_tile[1]][selected_tile[0]] = a - 48
                            grid_copy = []
                            for row in grid:
                                grid_copy.append([])
                                for val in row:
                                    grid_copy[-1].append(val)
                            if not solve(0, 0, grid) or not is_valid(selected_tile[1], selected_tile[0], before_list, a - 48):
                                grid = before_list
                                outline_color = pygame.Color((200, 0, 0))
                            else:
                                grid = grid_copy
                                outline_color = pygame.Color((0, 0, 200))
                elif event.key == 13:
                    showing_solve(0, 0, surface, selected_tile, x_lines, y_lines, outline_color, queued_number, grid, original_grid, clock)
                elif event.key == 32:
                    solve(0, 0, grid)


        update_surface(surface, selected_tile, x_lines, y_lines, outline_color, queued_number, grid, original_grid)
    pygame.quit()

def showing_solve(row:int, col:int, surface, selected_tile, x_lines, y_lines, outline_color, queued_number, grid, original_grid, clock):
    'Same as solve except it updates the screen and slows down to show process'
    if row == (len(grid) - 1) and col == len(grid[row]):
        return True
    if col == len(grid[row]):
        col = 0
        row += 1
    selected_tile = (col, row)
    outline_color = pygame.Color((0, 0, 200))
    if grid[row][col] != 0:
        return showing_solve(row, col + 1, surface, selected_tile, x_lines, y_lines, outline_color,
                               queued_number, grid, original_grid, clock)
    for i in range(1, 10):

        if is_valid(row, col, grid, i):
            grid[row][col] = i
            update_surface(surface, selected_tile, x_lines, y_lines, outline_color,
                           queued_number, grid, original_grid)
            clock.tick(100)
            if showing_solve(row, col + 1, surface, selected_tile, x_lines, y_lines, outline_color,
                               queued_number, grid, original_grid, clock):

                return True
        grid[row][col] = 0
    return False

if __name__ == '__main__':
    run()
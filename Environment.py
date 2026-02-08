import os
import platform
import pygame


class Environment:

    def __init__(self):
        pygame.init()

        # Default size
        self.size = (800, 600)

        # Choose mode
        if platform.system() == "Windows":
            self._init_standard_display()

        elif self.getUserInterface() == "graphics":
            self._init_standard_display()

        else:
            self._init_framebuffer_display()

        self.screen.fill((0, 0, 0))
        pygame.display.update()
        pygame.mouse.set_visible(True)  # keep mouse on for development

    # -----------------------------------------------------
    # Display Modes
    # -----------------------------------------------------
    def _init_standard_display(self):
        pygame.display.set_caption("pySokoban")
        self.screen = pygame.display.set_mode(self.size)

    def _init_framebuffer_display(self):
        # Fallback backend for Linux without X11
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print(f"I'm running under X display = {disp_no}")

        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False

        for driver in drivers:
            print(f"Trying framebuffer driver: {driver}")
            if not os.getenv("SDL_VIDEODRIVER"):
                os.putenv("SDL_VIDEODRIVER", driver)

            try:
                pygame.display.init()
                found = True
                break
            except pygame.error:
                print(f"Driver {driver} failed.")
                continue

        if not found:
            raise Exception("No suitable framebuffer video driver found!")

        info = pygame.display.Info()
        self.size = (info.current_w, info.current_h)
        print(f"Framebuffer size: {self.size[0]} x {self.size[1]}")

        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)

    # -----------------------------------------------------
    # Helper Functions
    # -----------------------------------------------------
    def getOS(self):
        return platform.system()

    def getUserInterface(self):
        return "graphics" if os.getenv("DISPLAY") else "framebuffer"

    def getPath(self):
        return os.path.dirname(os.path.abspath(__file__))

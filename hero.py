class Hero():
    def __init__(self,pos,land):
        self.mode = True
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        #self.cameraBind()
        self.cameraUp()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1]+5, -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False


    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()


    def accept_events(self):
        base.accept('j', self.turn_left)
        base.accept('j'+'-repeat', self.turn_left)
        base.accept('c' , self.changeView)
        base.accept('l', self.turn_right)
        base.accept('l'+'-repeat', self.turn_right)
        base.accept('i', self.turn_up)
        base.accept('i'+'-repeat', self.turn_up)
        base.accept('k', self.turn_down)
        base.accept('k'+'-repeat', self.turn_down)
        #movement
        base.accept('w', self.forward)
        base.accept('w'+'-repeat', self.forward)

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def turn_up(self):
        self.hero.setP((self.hero.getP() - 5) % 360)

    def turn_down(self):
        self.hero.setP((self.hero.getP() + 5) % 360)

    def just_move(self, angle):
        pos  = self.look_at(angle)
        self.hero.setPos(pos)


    def try_move(self, angle):
        pass

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move()

    """def check_dir(self, angle):
        # Your implementation of check_dir method here
        # Calculate dx and dy based on the input angle
        dx = math.cos(math.radians(angle))
        dy = math.sin(math.radians(angle))
        return dx, dy"""



    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        elif angle > 20 and angle <= 65:
            return +1, -1
        elif angle > 65 and angle <= 110:
            return +1, 0
        elif angle > 110 and angle <= 155:
            return +1, +1
        elif angle > 155 and angle <= 200:
            return 0, +1
        elif angle > 200 and angle <= 245:
            return -1, +1
        elif angle > 245 and angle <= 290:
            return -1, 0
        elif angle > 290 and angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())
        dx, dy  = self.check_dir(angle)
        return from_x + dx,from_y + dy, from_z


    def back(self):
        angle =(self.hero.getH()+180) % 360
        self.move_to(angle)

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def left(self):
        angle =(self.hero.getH()+90) % 360
        self.move_to(angle)

    def right(self):
        angle =(self.hero.getH()+270) % 360
        self.move_to(angle)

class car:
    def __init__(self, windscreen, engine, mirror, bonnet, boot, brake):
        self.windscreen = windscreen
        self.engine = engine
        self.mirror = mirror
        self.bonnet = bonnet
        self.boot = boot
        self.brake =brake


    def to_protect(self, windscreen):
        return self.windscreen
    def to_convert(self, engine):
        return self.engine
    def to_view(self, mirror):
        return self.mirror
    def to_check(self, bonnet):
        return self.bonnet
    def to_store (self, boot):
        return self.boot
    def to_control(self, brake):
        return self.brake

Honda_new = car("working perfectly", "is in motion", "serves as a multitude of purpose", "rest over the engine", "storage space in a car", "controls my motion")

print("my honda windscreen is", Honda_new.windscreen)
print("my engine", Honda_new.engine)
print("my honda glass is", Honda_new.mirror)
print("my honda bonnet", Honda_new.bonnet)
print("my honda boot serves as a", Honda_new.boot)
print("my honda brake", Honda_new.brake)




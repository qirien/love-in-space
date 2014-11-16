# BACKGROUNDS
image cuttlefish = "bg/cuttlefish-logo.jpg"
image bg stars = "bg/starscape.jpg"
image bg earth = "bg/earth.jpg"
image bg farm_exterior = "bg/farm-exterior.jpg"
image bg farm_exterior flip = im.Flip("bg/farm-exterior.jpg", horizontal = True)
image bg farm_exterior flip burned = "bg/farm-exterior-burned.jpg"
image bg porch = "bg/farm-porch.jpg"
image bg wedding = "bg/wedding.jpg"
image bg farm_interior = "bg/farm-interior.jpg"
image bg farm_interior flip = im.Flip("bg/farm-interior.jpg", horizontal = True)
image bg fields = "bg/fields.jpg"
image bg fields flip = im.Flip("bg/fields.jpg", horizontal = True)
image bg colony_ship_bunk = "bg/colony-ship-bunk.jpg"
image bg talam = "bg/talam.jpg"
image bg talaam_space = "bg/talaam-from-space.jpg"
image bg pond = "bg/pond.jpg"
image bg path = "bg/path.jpg"
image bg laundry = "bg/laundry.jpg"
image bg library = "bg/library.jpg"
image bg classroom = "bg/classroom.jpg"
image bg clinic = "bg/clinic.jpg"
image bg bedroom = "bg/bedroom.jpg"
image bg sunset = "bg/sunset.jpg"
image bg machine_shop = "bg/machine-shop.jpg"
image bg workshop = "bg/workshop.jpg"
image bg ocean = "bg/ocean.jpg"
image bg storehouse = "bg/storehouse.jpg"
image bg community_center = "bg/community-center.jpg"
image bg lab = "bg/lab.jpg"
image bg barn = "bg/barn.jpg"
image bg mountains = "bg/mountains.jpg"
image bg stream = "bg/stream.jpg"
image bg hotspring = "bg/hot-spring.jpg"
image bg tractor = "bg/tractor.jpg"
image bg church = "bg/church.jpg"
image bg city_street = "bg/city-street.jpg"
image bg bathhouse = "bg/bathhouse.jpg"
image bg gray_silk = "bg/silk-gray.jpg"
image overlay night = "bg/night.png"
image overlay bathhouse = "bg/bathhouse-overlay.png"
image overlay bedroom_covers = "bg/bedroom-overlay.png"
image overlay computer_pad = "bg/computer-pad.png"


# SPRITES
# TODO: Make sure bottom of sprites looks good; cut off if needed

# Him
image him normal = "sprites/him.png"
image him angry = "sprites/him-angry.png"
image him annoyed = "sprites/him-annoyed.png"
image him concerned = "sprites/him-concerned.png"
image him flirting = "sprites/him-flirt.png"
image him happy = "sprites/him-happy.png"
image him laughing = "sprites/him-happy.png"
image him sad = "sprites/him-sad.png"
image him surprised = "sprites/him-surprised.png"
image him serious = "sprites/him-annoyed.png" #TODO: does this work OK?
image him sleeping = "sprites/him-sleeping.png" #TODO: make color (shirtless?) version?

# Her
image her normal = "sprites/her.png"
# TODO: Fix angry, annoyed, flirting, serious,sleeping when they are done.
image her angry = "sprites/her-angry.png"
image her annoyed = "sprites/her-annoyed.png"
image her concerned = "sprites/her-concerned.png"
image her flirting = "sprites/her-flirt.png"
image her happy = "sprites/her-happy.png"
image her laughing = "sprites/her-laughing.png"
image her sad = "sprites/her-sad.png"
image her surprised = "sprites/her-surprised.png"
image her serious = "sprites/her-serious.png"
image her sleeping = "sprites/her-sleeping.png"

define SMALL_IMAGE_SCALE = 0.55
define SMALL_IMAGE_CROP = 90

image her sad head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her-sad.png", SMALL_IMAGE_SCALE))
image her concerned head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her-concerned.png", SMALL_IMAGE_SCALE))
image her serious head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her-serious.png", SMALL_IMAGE_SCALE))
image her normal head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her.png", SMALL_IMAGE_SCALE))
image her happy head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her-happy.png", SMALL_IMAGE_SCALE))

image him concerned head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him-concerned.png", SMALL_IMAGE_SCALE))
image him annoyed head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him-annoyed.png", SMALL_IMAGE_SCALE))
image him normal head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him.png", SMALL_IMAGE_SCALE))
image him happy head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him-happy.png", SMALL_IMAGE_SCALE))


# Other Characters
image female_child = "sprites/female-child.png"
image sara = "sprites/sara.png"
image sara normal = "sprites/sara.png"
image sara sad = "sprites/sara-sad.png"
image pavel = "sprites/pavel.png"
image thuc = "sprites/thuc.png"
image natalia = "sprites/natalia.png"
image julia = "sprites/julia.png"
image brennan = "sprites/brennan.png"
image lily = "sprites/lily.png"
image lily normal = "sprites/lily.png"
image lily upset = "sprites/lily-upset.png"
image lily happy = "sprites/lily-happy.png"
image naomi = "sprites/naomi.png"
image pete = "sprites/pete.png"
image helen = "sprites/helen.png"
image ilian = "sprites/ilian.png"
image martin = "sprites/martin.png"
image kid = "sprites/kid.png"

# Animals
image lettie = "sprites/horse.png"
image lettie_head = LiveCrop((0,0,300,570), "sprites/horse.png")
image goat = "sprites/goat.png"
image goat_flip = im.Flip("sprites/goat.png", horizontal = True)
image goat_small = im.FactorScale("sprites/goat.png", 0.85)
image seastar = "sprites/seastar.png"


# GUI
image ctc_blink:
       "GUI/ctc.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 
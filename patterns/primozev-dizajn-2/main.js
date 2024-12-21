import { initializeJelka } from 'jelka'
import { basic, colors, lights } from 'jelka/interface'
import { Axis, Relation } from 'jelka/types'

function randint(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min)
}

initializeJelka()

basic.setFrameRate(50)

lights.setLights(lights.getLights(), colors.rgbColor(255, 0, 0))

let random = randint(0, 225)
let random2 = randint(0, 225)
let random3 = randint(0, 225)

let x = 0
let x2 = 100

basic.onFrame(function (frameNumber, timeSinceStart) {
  x2 += -1
  x += 1
  lights.setLights(
    lights.lightsWhere(
      Axis.Y,
      Relation.Greater,
      0,
      lights.lightsWhere(
        Axis.X,
        Relation.Greater,
        0,
        lights.lightsWhere(Axis.Z, Relation.Less, x, lights.getLights()),
      ),
    ),
    colors.rgbColor(random, random2, random3),
  )
  lights.setLights(
    lights.lightsWhere(
      Axis.Y,
      Relation.Greater,
      0,
      lights.lightsWhere(
        Axis.X,
        Relation.Less,
        0,
        lights.lightsWhere(Axis.Z, Relation.Greater, x2, lights.getLights()),
      ),
    ),
    colors.rgbColor(random, random2, random3),
  )
  lights.setLights(
    lights.lightsWhere(
      Axis.Y,
      Relation.Less,
      0,
      lights.lightsWhere(
        Axis.X,
        Relation.Greater,
        0,
        lights.lightsWhere(Axis.Z, Relation.Greater, x2, lights.getLights()),
      ),
    ),
    colors.rgbColor(random, random2, random3),
  )
  lights.setLights(
    lights.lightsWhere(
      Axis.Y,
      Relation.Less,
      0,
      lights.lightsWhere(
        Axis.X,
        Relation.Less,
        0,
        lights.lightsWhere(Axis.Z, Relation.Less, x, lights.getLights()),
      ),
    ),
    colors.rgbColor(random, random2, random3),
  )
  if (x === 100) {
    random = randint(0, 225)
    random2 = randint(0, 225)
    random3 = randint(0, 225)
    x = 0
    x2 = 100
  }
})

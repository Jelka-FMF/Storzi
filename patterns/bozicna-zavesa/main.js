import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

function randint(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min)
}

initializeJelka()

let višina = 0
let odtenekrdeče = randint(0, 255)
let odtenekzelena = randint(0, 255)
let odtenekmodra = randint(0, 255)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(
    shapes.plane(0, 0, višina, 0, 90, 10),
    colors.rgbColor(odtenekrdeče, odtenekmodra, odtenekzelena),
  )

  višina += 0.5
  odtenekrdeče += 0.5
  odtenekzelena += 0.5
  odtenekmodra += 0.5

  if (višina > 100) {
    višina = 0
    odtenekrdeče = randint(0, 255)
    odtenekzelena = randint(0, 255)
    odtenekmodra = randint(0, 255)
  }
})

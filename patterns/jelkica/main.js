import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

basic.setFrameRate(50)

let a = 200

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(shapes.sphere(100, 50, 50, frameNumber % a, 20), colors.cmykColor(45, 16, 0, 17))
  lights.setLights(shapes.sphere(110, 50, 50, frameNumber % a, 20), colors.cmykColor(5, 16, 75, 10))
  lights.setLights(shapes.sphere(120, 50, 50, frameNumber % a, 20), colors.cmykColor(0, 41, 14, 10))
  lights.setLights(shapes.sphere(130, 50, 50, frameNumber % a, 20), colors.cmykColor(18, 0, 40, 11))
  lights.setLights(
    shapes.sphere(140, 50, 50, frameNumber % a, 20),
    colors.cmykColor(56, 47, 40, 10),
  )
  lights.setLights(
    shapes.sphere(150, 50, 50, frameNumber % a, 20),
    colors.cmykColor(10, 55, 57, 40),
  )
})

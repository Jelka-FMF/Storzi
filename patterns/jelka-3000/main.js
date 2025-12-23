import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

let a = 0
let b = 0

basic.onFrame(function (frameNumber, timeSinceStart) {
  a += 1
  b += 2

  lights.resetLights(lights.getLights())
  lights.setLights(shapes.sphere(0, 0, 50, a, 5), colors.rgbColor(241, 255, 34))
  lights.setLights(shapes.sphere(0, 0, 50, a + 2, 5), colors.rgbColor(255, 0, 20))
  lights.setLights(shapes.sphere(0, 0, 50, a + 4, 5), colors.rgbColor(255, 128, 0))
  lights.setLights(shapes.plane(0, 0, 50, b, b, 10), colors.rgbColor(0, 0, 255))

  if (a > 50) {
    a = 0
  }
  if (b > 360) {
    b = 0
  }
})

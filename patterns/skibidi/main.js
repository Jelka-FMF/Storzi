import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

let r = 0

basic.setFrameRate(60)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(shapes.cylinder(0, 0, 50, 90, 0, r, 200), colors.hslColor(frameNumber, r, 50))
  if (r > 100) r = 0
  r += 0.5
})

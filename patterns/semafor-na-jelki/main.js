import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'

initializeJelka()

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.resetLights(lights.getLights())
  lights.setLights(lights.getLights(), colors.hslColor(frameNumber % 0.5, 100, 0))
  lights.setLights(shapes.plane(150, 0, 0, 0, frameNumber % 110, 10), colors.rgbColor(64, 120, 0))
  lights.setLights(shapes.plane(50, 0, 0, 0, frameNumber % 110, 10), colors.rgbColor(255, 0, 0))
  lights.setLights(shapes.plane(100, 0, 0, 0, frameNumber % 110, 10), colors.rgbColor(255, 199, 0))
})

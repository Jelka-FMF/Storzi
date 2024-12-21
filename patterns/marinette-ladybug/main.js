import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'
import { Axis, Relation } from 'jelka/types'

initializeJelka()

basic.setFrameRate(50)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(
    shapes.planeRelation(0, 0, 0, 0, frameNumber, Relation.Greater),
    colors.rgbColor(0, 0, 255),
  )
  lights.setLights(shapes.plane(0, 0, 50, frameNumber, 0, 20), colors.rgbColor(255, 0, 0))
  lights.setLights(
    lights.lightsWhere(Axis.Z, Relation.Greater, frameNumber, lights.getLights()),
    colors.cmykColor(0, 0, 0, 100),
  )
})

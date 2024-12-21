import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'
import { Relation } from 'jelka/types'

initializeJelka()

basic.setFrameRate(60)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.setLights(
    shapes.planeRelation(0, 0, frameNumber % 100, 90, 90, Relation.Greater),
    colors.cmykColor(0, 40, 100, 0),
  )
  lights.setLights(
    shapes.planeRelation(0, 0, frameNumber % 110, 90, 90, Relation.Less),
    colors.cmykColor(0, 0, 37, 0),
  )
  lights.setLights(shapes.plane(0, 0, frameNumber % 120, 0, 90, 30), colors.cmykColor(0, 60, 56, 0))
})

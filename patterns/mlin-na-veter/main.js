import { initializeJelka } from 'jelka'
import { basic, colors, lights, shapes } from 'jelka/interface'
import { Axis, Relation } from 'jelka/types'

initializeJelka()

let stolp = shapes.plane(0, 0, 50, 0, 0, 30, lights.lightsWhere(Axis.Z, Relation.Less, 65))
let streha = shapes.ball(0, 0, 65, 15)
let vetrnice = shapes.cylinder(0, 0, 65, 90, 0, 40, 100)

basic.onFrame(function (frameNumber, timeSinceStart) {
  lights.resetLights(lights.getLights())
  lights.setLights(stolp, colors.hsvColor(frameNumber / 10 + 180, 50, 60))
  lights.setLights(streha, colors.hsvColor(frameNumber / 10 + 180, 50, 60))
  lights.setLights(
    shapes.plane(0, 0, 65, 0, frameNumber * 2, 10, vetrnice),
    colors.hsvColor(frameNumber / 10, 100, 100),
  )
  lights.setLights(
    shapes.plane(0, 0, 65, 0, frameNumber * 2 + 90, 10, vetrnice),
    colors.hsvColor(frameNumber / 10, 100, 100),
  )
})

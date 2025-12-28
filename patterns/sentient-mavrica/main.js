import { initializeJelka } from 'jelka'
import { basic, colors, lights } from 'jelka/interface'
import { Axis, Relation } from 'jelka/types'

initializeJelka()

let pointx = 0
let pointy = 0
let pointz = -100

let goalx = 0
let goaly = 0
let goalz = 50

let cooldown = 0
let modeCooldown = 0

//  Modes
//  0 = choose a random point every now and then
//  1 = slowly circle around
//  2 = shake in the center
let mode = 0

function sq(x) {
  return x * x
}

function switchMode(prob) {
  modeCooldown -= 1

  if (Math.random() < prob && modeCooldown <= 0) {
    modeCooldown = 30
    mode = Math.trunc(Math.random() * 2.3)
  }
}

function rainbowRgb(x, period = 1.0) {
  let h = (x / period) % 1.0
  let i = Math.trunc(h * 6)
  let f = h * 6 - i
  let q = 1 - f
  i %= 6

  if (i === 0) {
    return [1, f, 0]
  } else if (i === 1) {
    return [q, 1, 0]
  } else if (i === 2) {
    return [0, 1, f]
  } else if (i === 3) {
    return [0, q, 1]
  } else if (i === 4) {
    return [f, 0, 1]
  } else {
    return [1, 0, q]
  }
}

basic.onFrame((frameNumber, timeSinceStart) => {
  if (mode === 0) {
    switchMode(1 / 1000)
    let rng = Math.trunc(Math.random() * 200)
    cooldown -= 1
    if (rng === 0 && cooldown <= 0) {
      cooldown = 50
      goalx = Math.random() * 100 - 50
      goaly = Math.random() * 100 - 50
      goalz = Math.random() * 100
    }
  }

  if (mode === 1) {
    switchMode(1 / 1000)
    let prog = (frameNumber % 400) / 400
    goalz = 50
    goalx = Math.sin(prog * 2 * Math.PI) * 20
    goaly = Math.cos(prog * 2 * Math.PI) * 20
  }

  if (mode === 2) {
    switchMode(1 / 60)
    let prog = (frameNumber % 10) / 10
    goalz = Math.sin(prog * 2 * Math.PI) * 30 + 50
    goalx = 0
    goaly = 0
  }

  let speed = 0.1
  pointx += (goalx - pointx) * speed
  pointy += (goaly - pointy) * speed
  pointz += (goalz - pointz) * speed

  let allLights = lights.getLights()
  for (let light of allLights) {
    let x = lights.getCoordinate(Axis.X, light)
    let y = lights.getCoordinate(Axis.Y, light)
    let z = lights.getCoordinate(Axis.Z, light)
    let dist = Math.sqrt(sq(x - pointx) + sq(y - pointy) + sq(z - pointz))
    let [r, g, b] = rainbowRgb(dist, 20)
    lights.setLights([light], colors.rgbColor(r * 255, g * 255, b * 255))
  }
})

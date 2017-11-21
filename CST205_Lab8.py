
#Lab 8
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*2)
  return sound
    
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value/2)
  return sound
    
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
  return sound
    
def maxSample(sound):
  maxValue = 0
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    maxValue = max(maxValue, value)
  return maxValue

def maxVolume(sound):
    factor = 32767 / maxSample(sound)
    for sample in getSamples(sound):
        value = getSampleValue(sample)
        setSampleValue(sample, value * factor)
    return sound

def goToEleven(sound):
    for sample in range(0, getLength(sound)):
        if getSampleValueAt(sound, sample) > 0:
            setSampleValueAt(sound, sample, 32767)
        elif getSampleValueAt(sound, sample) < 0:
            setSampleValueAt(sound, sample, -32768)
    return sound

#Call Function                                                                                                 
s = pickAFile()
sd = makeSound(s)

             

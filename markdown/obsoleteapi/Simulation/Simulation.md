---
title: "Simulation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation.htm"
---

# Simulation

## Simulation Object

This interface is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

| image\Feature.gif |  |  |
| --- | --- | --- |
|  | image\branch1.gif |  |
|  |  | image\branch1.gif |

Allows access to the data that defines a Physical Simulation, which is the Simulation folder that is created when you create Physical Simulation elements such as linear or rotary motors, springs, and gravity in an assembly document.

NOTE: Do not confuse Physical Simulation with animation. The SolidWorks software computes a Physical Simulation, which generates a number of steps (and transforms) and elapsed time for those steps. The SolidWorks software then displays the computed Physical Simulation using animation. To create the display, the animation process takes the Physical Simulation steps and does a linear interpolation of those steps for the elapsed time. The elapsed time and frames of Physical Simulation will most likely be different than the elapsed time and frames of an animation.

Use the Accessors link to obtain a list of functions that return this object.

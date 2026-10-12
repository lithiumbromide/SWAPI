---
title: "Simulation::Duration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__Duration.htm"
---

# Simulation::Duration

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This property gets the elapsed time of the Physical Simulation.

Syntax (OLE Automation)

Retval = Simulation.Duration (VB Get property)

Retval = Simulation.GetDuration ( ) (C++ Get property)

| Output: | (double) Retval | Elapsed time in seconds |
| --- | --- | --- |

Syntax (COM)

status = Simulation->get_Duration ( &Retval )

| Output: | (double) Retval | Elapsed time in seconds |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the Physical Simulation has not yet been calculated, then Retval is 0.0.

The return value represents the length of time that the simulation is expected to last. This means that if a bouncing ball takes 15 seconds to come to a stop, then this property returns a value of 15.

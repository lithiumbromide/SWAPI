---
title: "Simulation::Frames"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__Frames.htm"
---

# Simulation::Frames

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This property gets the number of steps, or frames, in the Physical Simulation.

Syntax (OLE Automation)

Retval = Simulation.Frames (VB Get property)

Retval = Simulation.GetFrames ( ) (C++ Get property)

| Output: | (long) Retval | Number of steps |
| --- | --- | --- |

Syntax (COM)

status = Simulation->get_Frames ( &Retval )

| Output: | (long) Retval | Number of steps |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the Physical Simulation is not yet calculated, then Retval is 0.0.

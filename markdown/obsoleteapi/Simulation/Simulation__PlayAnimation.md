---
title: "Simulation::PlayAnimation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__PlayAnimation.htm"
---

# Simulation::PlayAnimation

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method plays an animation of this simulation.

Syntax (OLE Automation)

Retval = Simulation.PlayAnimation ()

| Output: | (LPANIMATION) Retval | Pointer to Animation object |
| --- | --- | --- |

Syntax (COM)

status = Simulation->PlayAnimation ( &Retval)

| Output: | (LPANIMATION) Retval | Pointer to Animation object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If an animation is playing when this method is used, then this method returns the Animation object for that animation. To check to see if an animation is currently playing, use Simulation::IsAnimationPlaying.

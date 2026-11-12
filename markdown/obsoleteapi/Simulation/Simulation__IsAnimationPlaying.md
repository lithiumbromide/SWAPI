---
title: "Simulation::IsAnimationPlaying"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__IsAnimationPlaying.htm"
---

# Simulation::IsAnimationPlaying

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method checks to see if an animation is currently playing.

Syntax (OLE Automation)

Retval = Simulation.IsAnimationPlaying ()

| Output: | (VARIANT_BOOL) Retval | TRUE if an animation is playing, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = Simulation->IsAnimationPlaying ( &Retval)

| Output: | (VARIANT_BOOL) Retval | TRUE if an animation is playing, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To play an animation, use Simluation::PlayAnimation.

---
title: "Simulation::Animation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Simulation/Simulation__Animation.htm"
---

# Simulation::Animation

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This property gets the Animation object without playing the animation or displaying the Animation Controller pop-up toolbar.

Syntax (OLE Automation)

Retval = Simulation.Animation (VB Get property)

Retval = Simulation.GetAnimation ( ) (C++ Get property)

| Output: | (LPANIMATION) Retval | Animation object |
| --- | --- | --- |

Syntax (COM)

status = Simulation->get_Animation ( &Retval )

| Output: | (LPANIMATION) Retval | Animation object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| To... | Then... |
| --- | --- |
| Get the duration of an animation | Use Animation::Duration after using this property |
| Play the animation | Use Animation::Play after using this property |
| Display the Animation Controller pop-up toolbar | Use Simulation::PlayAnimation instead of using this property |

NOTE: Use only the following Animation property and method with Simulution::Animation: Animation::Duration and Animation::PlayAnimation. The other Animation properties and methods do nothing with an Animation object returned by Simlulation::Animation because they expect an animation to be playing. Use Simluation::IsAnimationPlaying to determine whether an animation is playing.

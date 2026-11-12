---
title: "Animation::Speed"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__Speed.htm"
---

# Animation::Speed

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method gets the speed at which the animation plays.

Syntax (OLE Automation)

Speed = Animation.Speed (VB Get property)

Animation.Speed = Speed (VB Set property)

Speed = Animation.GetSpeed ( ) (C++ Get property)

Animation.SetSpeed ( Speed ) (C++ Set property)

| Output: | (long) Speed | Speed at which the animation plays as defined by swAnimationPlaySpeed_e |
| --- | --- | --- |

Syntax (COM)

status = Animation->get_Speed ( &Speed )

status = Animation->put_Speed ( Speed )

| Output: | (long) Speed | Speed at which the animation plays as defined by swAnimationPlaySpeed_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property affects the duration of the animation. It allows you to specify whether or not to play the animation at half speed or double speed, which halves or doubles the animation duration.

If you use Animation::Duration while an animation is playing, then you may not get the same result as when the animation is not running.

| If you get the Animation object using... | And then use... | Then the duration... |
| --- | --- | --- |
| Simulation::Animation | Animation::Duration | Is at the normal playing speed |
| Simulation::PlayAnimation | Animation::Duration | May be different a different value because the animation is playing and the Animation Controller speed may be set to Normal , Slow Play , or Fast Play |

.

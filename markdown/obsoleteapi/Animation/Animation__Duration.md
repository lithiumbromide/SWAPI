---
title: "Animation::Duration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__Duration.htm"
---

# Animation::Duration

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This property gets the length of time, in seconds, this animation plays.

Syntax (OLE Automation)

Duration = Animation.Duration (VB Get property)

Duration = Animation.GetDuration ( ) (C++ Get property)

| Output: | (double) Duration | Length of time, in seconds, this animation plays |
| --- | --- | --- |

Syntax (COM)

status = Animation->get_Duration ( &Duration )

| Output: | (double) Duration | Length of time, in seconds, this animation plays |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Animation::Speed affects the duration of the animation. Animation::Speed allows you to specify whether or not to play the animation at half speed or double speed, which halves or doubles the animation duration.

If you use Animation::Duration while an animation is playing, then you may not get the same result as when the animation is not running.

| If you get the Animation object using... | And then use... | Then the duration... |
| --- | --- | --- |
| Simulation::Animation | Animation::Duration | Is at the normal playing speed |
| Simulation::PlayAnimation | Animation::Duration | May be a different value because the animation is playing and the Animation Controller speed may be set to Normal , Slow Play , or Fast Play |

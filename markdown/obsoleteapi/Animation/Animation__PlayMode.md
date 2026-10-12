---
title: "Animation::PlayMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__PlayMode.htm"
---

# Animation::PlayMode

This property is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method gets mode in which this animation is playing.

Syntax (OLE Automation)

Mode = Animation.PlayMode (VB Get property)

Animation.PlayMode = Mode (VB Set property)

Mode = Animation.GetPlayMode ( ) (C++ Get property)

Animation.SetPlayMode ( Mode ) (C++ Set property)

| Output: | (long) Mode | Mode in which this animation is playing as defined in swAnimationPlayMode_e |
| --- | --- | --- |

Syntax (COM)

status = Animation->get_PlayMode ( &Mode )

status = Animation->put_PlayMode ( Mode )

| Output: | (long) Mode | Mode in which this animation is playing as defined in swAnimationPlayMode_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

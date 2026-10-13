---
title: "Animation::Play"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__Play.htm"
---

# Animation::Play

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method plays the animation.

Syntax (OLE Automation)

Retval = Animation.Play ()

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation plays, FALSE if the animation controller is not running |
| --- | --- | --- |

Syntax (COM)

status = Animation->Play ( &Retval)

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation plays, FALSE if the animation controller is not running |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

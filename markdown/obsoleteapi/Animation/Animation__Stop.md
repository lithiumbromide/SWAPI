---
title: "Animation::Stop"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__Stop.htm"
---

# Animation::Stop

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method stops playing animation, and the position of the animation returns it to its beginning.

Syntax (OLE Automation)

Retval = Animation.Stop ()

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation stops playing and is positioned at its beginning, FALSE if an animation controller is not running |
| --- | --- | --- |

Syntax (COM)

status = Animation->Stop ( &Retval)

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation stops playing and is positioned at its beginning, FALSE if an animation controller is not running |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

---
title: "Animation::End"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__End.htm"
---

# Animation::End

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method positions the animation at its ends.

Syntax (OLE Automation)

Retval = Animation.End ()

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation is positioned at its ends, FALSE if the animation controller is not running |
| --- | --- | --- |

Syntax (COM)

status = Animation->End ( &Retval)

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation is positioned at its ends, FALSE if the animation controller is not running |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

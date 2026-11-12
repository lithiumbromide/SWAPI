---
title: "Animation::Close"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Animation/Animation__Close.htm"
---

# Animation::Close

This method is:

- obsolete and has not been superseded.
- nonfunctional in SolidWorks 2008 and later.

  Use the interfaces related to motion studies introduced in SolidWorks 2008 to access animation and simulation.

Description

This method closes the animation controller.

Syntax (OLE Automation)

Retval = Animation.Close ()

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation controller closes, FALSE if the animation controller is not running |
| --- | --- | --- |

Syntax (COM)

status = Animation->Close ( &Retval)

| Output: | (VARIANT_BOOL) Retval | TRUE if the animation controller closes, FALSE if the animation controller is not running |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

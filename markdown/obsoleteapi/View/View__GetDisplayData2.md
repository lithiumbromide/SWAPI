---
title: "View::GetDisplayData2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDisplayData2.htm"
---

# View::GetDisplayData2

This method is obsolete and has been superseded by [View::GetDisplayData3](sldworksAPI.chm::/View/View__GetDisplayData3.htm).

Description

This method gets the DisplayData object for this drawing view.

NOTE: The DisplayData object provides information for additional display data, such as reference plane display, reference axis display, unused sketch geometry from a part, and so on. The data kept with the DisplayData object is strictly for display purposes and allows you to recreate unintelligent geometry. It does not provide associations or detailed information about the geometry.

Syntax (OLE Automation)

retval = View.GetDisplayData2 ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the DisplayData object for this drawing view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDisplayData2 ( &retval )

| Output: | (LPDISPLAYDATA) retval | Pointer to the DisplayData object for this drawing view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method supersedes the now obsolete View::GetDisplayData and should be used in its place. The previous version of this method returned sketch entities based on their hide or show setting from the model document. This method returns the sketch entities based on the hide or show setting from this drawing view. This behavior is more appropriate because it gives you the display as seen in the drawing view.

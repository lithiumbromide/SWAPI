---
title: "View::GetDisplayData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDisplayData.htm"
---

# View::GetDisplayData

This method is obsolete and has been superseded by [View::GetDisplayData2](View__GetDisplayData2.htm).

Description

This method gets the DisplayData object for this drawing view.

NOTE: The DisplayData object provides information for additional display data, such as reference plane display, reference axis display, unused sketch geometry from a part, and so on. The data kept with the DisplayData object is strictly for display purposes and allows you to recreate unintelligent geometry. It does not provide associations or detailed information about the geometry.

Syntax (OLE Automation)

retval = View.GetDisplayData ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the DisplayData object for this drawing view. |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDisplayData ( &retval )

| Output: | (LPDISPLAYDATA) retval | Pointer to the DisplayData object for this drawing view. |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

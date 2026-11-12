---
title: "Body2::Display2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__Display2.htm"
---

# Body2::Display2

This method is obsolete and has been superseded by [Body2::Display3](sldworksAPI.chm::/Body2/Body2__Display3.htm).

Description

This method displays a temporary body object in the context of the specified part.

Syntax (OLE Automation)

void = Body2.Display2 ( part, color, option)

| Input: | (LPPARTDOC) part | Part document in which body exists |
| --- | --- | --- |
| Input: | (long) color | COLORREF value for color |
| Input: | (long) option | Selection state of temporary body as defined by swTempBodySelectOptions_e |

Syntax (COM)

status = Body2->Display2 ( part, color, option)

| Input: | (LPPARTDOC) part | Part document in which body exists |
| --- | --- | --- |
| Input: | (long) color | COLORREF value for color |
| Input: | (long) option | Selection state of temporary body as defined by swTempBodySelectOptions_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Using this method, you can select temporary bodies. You can then assign colors to faces on temporary bodies and to entire temporary bodies using Face2::MaterialPropertyValues and Body2::MaterialPropertyValues2, respectively. To determine if a body is temporary, call Body2::IsTemporaryBody.

If you specify swTempBodySelectable for the option argument, then the blocking state is set to swModifyBlock. The blocking state is unset after Body2::Hide is called.

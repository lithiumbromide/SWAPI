---
title: "Body::Save"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__Save.htm"
---

# Body::Save

This method is obsolete and has been superseded by [Body2::Save](sldworksAPI.chm::/Body2/Body2__Save.htm).

Description

This method saves a temporary body.

Syntax (OLE Automation)

void Body.Save ( streamIn)

| Input: | (LPUNKNOWN) streamIn | Stream to be used for the save |
| --- | --- | --- |

Syntax (COM)

status = Body->ISave ( streamIn )

| Input: | (LPUNKNOWN) streamIn | Stream to be used for the save |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If you want to save the solid body object that is associated with the document, then save the document.

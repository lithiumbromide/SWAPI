---
title: "Face::Highlight"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__Highlight.htm"
---

# Face::Highlight

This method is obsolete and has been superseded by [Face2::Highlight](sldworksAPI.chm::/Face2/Face2__Highlight.htm).

Description

This method highlights or de-highlights this face object.

Syntax (OLE Automation)

void Face.Highlight ( state)

| Input: | (BOOL) state | TRUE highlights the face, FALSE de-highlights the face |
| --- | --- | --- |

Syntax (COM)

status = Face->IHighlight ( state )

| Input: | (VARIANT_BOOL) state | TRUE highlights the face, FALSE de-highlights the face |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The highlight state remains in place until the model is rebuilt or redrawn.

SolidWorks does not support this method for faces obtained from reference surface bodies.

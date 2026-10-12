---
title: "View::SetDisplayTangentEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__SetDisplayTangentEdges.htm"
---

# View::SetDisplayTangentEdges

This method is obsolete and has been superseded by [View::SetDisplayTangentEdges2](sldworksAPI.chm::/View/View__SetDisplayTangentEdges2.htm).

Description

This method sets the tangent edge display mode of the drawing view.

NOTE: Tangent edges are the transition lines between, for example, a blend and a face.

Syntax (OLE Automation)

void View.SetDisplayTangentEdges ( displayIn)

| Input: | (BOOL) displayIn | TRUE if tangent edges show, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = View->SetDisplayTangentEdges ( displayIn )

| Input: | (VARIANT_BOOL) displayIn | TRUE if tangent edges show, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

See also View::GetDisplayMode, View::SetDisplayMode, and View::GetDisplayTangentEdges,

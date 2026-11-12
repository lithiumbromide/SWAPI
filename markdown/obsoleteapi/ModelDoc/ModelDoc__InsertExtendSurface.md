---
title: "ModelDoc::InsertExtendSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertExtendSurface.htm"
---

# ModelDoc::InsertExtendSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertExtendSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertExtendSurface.htm).

Description

This method extends a surface along the selected faces or edges.

Syntax (OLE Automation)

void ModelDoc.InsertExtendSurface ( extendLinear, endCondition, distance )

| Input: | (BOOL) extendLinear | TRUE to extend surface linearly, FALSE to extend along the same surface |
| --- | --- | --- |
| Input: | (long) endCondition | 0 – Extend surface by given distance 1 – Extend surface up to a selected point 2 – Extend surface up to a selected surface |
| Input: | (double) distance | Distance to extend surface along |

Syntax (COM)

status = ModelDoc->InsertExtendSurface ( extendLinear, endCondition, distance )

| Input: | (VARIANT_BOOL) extendLinear | TRUE to extend surface linearly, FALSE to extend along the same surface |
| --- | --- | --- |
| Input: | (long) endCondition | 0 – Extend surface by given distance 1 – Extend surface up to a selected point 2 – Extend surface up to a selected surface |
| Input: | (double) distance | Distance to extend surface along |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selection list can contain faces or edges from the surface. These selected entities will be extended away from the surface according to the input arguments.

The selected point or surface to extend to should be in the selection list. If endCondition is to a selected surface, then currently only faces from solids are supported.

---
title: "ModelDoc::InsertPlanarRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertPlanarRefSurface.htm"
---

# ModelDoc::InsertPlanarRefSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertPlanarRefSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertPlanarRefSurface.htm).

Description

This method inserts a planar reference surface.

Syntax (OLE Automation)

retval = ModelDoc.InsertPlanarRefSurface ( )

| Return: | (BOOL) retval | TRUE if the reference surface was created, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertPlanarRefSurface ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the reference surface was created, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as interactively creating a planar surface by selecting Insert, Reference Geometry, Planar Surface. See SolidWorks Help for more information about what entities are valid for selection.

Make the selections using ModelDoc::SelectByID before calling this method.

---
title: "ModelDoc::UserFavors"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__UserFavors.htm"
---

# ModelDoc::UserFavors

This method is obsolete and has been superseded by [ModelDoc2::UserFavors](sldworksAPI.chm::/ModelDoc2/ModelDoc2__UserFavors.htm).

Description

This method specifies whether geometric relations are automatically created as you add sketch elements.

Syntax (OLE Automation)

void ModelDoc.UserFavors ()

Syntax (COM)

status = ModelDoc->UserFavors ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

If this option is toggled on, then the cursor changes shape as you sketch to show you which relations can be created: horizontal, vertical, parallel, perpendicular, tangent, midpoint, and coincident.

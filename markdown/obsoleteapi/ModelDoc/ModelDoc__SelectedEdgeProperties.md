---
title: "ModelDoc::SelectedEdgeProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectedEdgeProperties.htm"
---

# ModelDoc::SelectedEdgeProperties

This method is obsolete and has been superseded by [ModelDoc2::SelectedEdgeProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectedEdgeProperties.htm).

Description

This method sets the property values of the selected edge.

Syntax (OLE Automation)

retval = ModelDoc.SelectedEdgeProperties ( edgeName)

| Input: | (BSTR) edgeName | Name of the edge |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successfully changed the edge properties, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SelectedEdgeProperties ( edgeName, &retval )

| Input: | (BSTR) edgeName | Name of the edge |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully changed the edge properties, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If this edge does not already have a name, then this method sets the name.

If the edge already has a name, then this method does not change the name and returns FALSE. This behavior is intended to prevent a program from renaming an edge that is referenced in some other location.

name to that edge. If you were to change that name, then there is no guarantee that the mate will still be valid. Therefore, when using entity names, you should first check to see if the entity is already named, and if so, use the existing name. If no name exists for the edge, then you can give the edge a name.

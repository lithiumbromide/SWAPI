---
title: "ModelDoc2::InsertAxis"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertAxis.htm"
---

# ModelDoc2::InsertAxis

This method is obsolete and has been superseded by [ModelDoc2::InsertAxis2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertAxis2.htm).

Description

This method will insert a reference axis based on the currently selected items.

Syntax (OLE Automation)

retval = ModelDoc2.InsertAxis ( )

| Return: | (BOOL) retval | TRUE if the reference axis is created, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->InsertAxis ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the reference axis is created, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The behavior of this method is identical when interactively creating axes. The reference axis is created based on the combination of items selected (for example, two vertices, an edge, a cylindrical surface, and so on). The set of valid selection combinations match the set of valid selection combinations for the interactive operation.

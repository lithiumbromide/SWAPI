---
title: "ModelDoc::InsertAxis"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertAxis.htm"
---

# ModelDoc::InsertAxis

This method is obsolete and has been superseded by [ModelDoc2::InsertAxis](../ModelDoc2/ModelDoc2__InsertAxis.htm).

Description

This method inserts a reference axis based on the currently selected items.

Syntax (OLE Automation)

retval = ModelDoc.InsertAxis ( )

| Return: | (Boolean) retval | TRUE if the reference axis is created successfully, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertAxis ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if the reference axis is created successfully, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The behavior of this method is identical to that used to interactively create axes. SolidWorks creates the reference axis based on the combination of items selected (for example, two vertices, an edge, a cylindrical surface, and so on). The set of valid selection combinations will match the set of valid selection combinations for the interactive operation.

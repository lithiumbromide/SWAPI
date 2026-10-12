---
title: "ModelDoc::AddDiameterDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddDiameterDimension2.htm"
---

# ModelDoc::AddDiameterDimension2

This method is obsolete and has been superseded by [ModelDoc2::AddDiameterDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddDiameterDimension2.htm).

Description

This method adds a diameter dimension at the specified location for the selected item.

Syntax (OLE Automation)

retval = ModelDoc.AddDiameterDimension2 ( x, y, z )

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Return: | (LPDISPATCH) retval | Pointer to the newly created diameter dimension |

Syntax (COM)

status = ModelDoc->IAddDiameterDimension2 ( x, y, z, &retval )

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Output: | (LPDISPLAYDIMENSION) retval | A pointer to the newly created diameter dimension |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

---
title: "ModelDoc2::AddDiameterDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddDiameterDimension.htm"
---

# ModelDoc2::AddDiameterDimension

This method is obsolete and has been superseded by [ModelDoc2::AddDiameterDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddDiameterDimension2.htm).

Description

This method adds a diameter dimension at the specified location for the selected item.

Syntax (OLE Automation)

retval = ModelDoc2.AddDiameterDimension ( x, y, z)

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Return: | (BOOL) retval | TRUE if the dimension was added successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->AddDiameterDimension ( x, y, z, &retval )

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Output: | (VARIANT_BOOL) retval | TRUE if the dimension was added successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

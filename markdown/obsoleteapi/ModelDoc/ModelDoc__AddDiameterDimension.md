---
title: "ModelDoc::AddDiameterDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddDiameterDimension.htm"
---

# ModelDoc::AddDiameterDimension

This method is now obsolete and has been superseded by [ModelDoc::AddDiameterDimension2](ModelDoc__AddDiameterDimension2.htm)

Description

This method adds a diameter dimension at the specified location for the selected item.

Syntax (OLE Automation)

retval = ModelDoc.AddDiameterDimension ( x, y, z)

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Return: | (BOOL) retval | TRUE if the dimension was added successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->AddDiameterDimension ( x, y, z, &retval )

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Output: | (VARIANT_BOOL) retval | TRUE if the dimension was added successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

---
title: "ModelDoc::AddRadialDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddRadialDimension2.htm"
---

# ModelDoc::AddRadialDimension2

This method is obsolete and has been superseded by [ModelDoc2::AddRadialDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddRadialDimension2.htm).

Description

This method adds a radial dimension at the specified location for the selected item.

Syntax (OLE Automation)

retval = ModelDoc.AddRadialDimension2 ( x, y, z )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Return: | (LPDISPATCH) retval | Pointer to the newly created dimension |

Syntax (COM)

status = ModelDoc->IAddRadialDimension2 ( x, y, z, &retval )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the newly created dimension |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

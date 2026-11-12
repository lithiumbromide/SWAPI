---
title: "ModelDoc::AddVerticalDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddVerticalDimension2.htm"
---

# ModelDoc::AddVerticalDimension2

This method is obsolete and has been superseded by [ModelDoc2::AddVerticalDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddVerticalDimension2.htm).

Description

This method creates a vertical dimension for the current selected entities at the specified location.

Syntax (OLE Automation)

retval = ModelDoc.AddVerticalDimension2 ( x, y, z )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Return: | (LPDISPATCH) retval | A pointer to the newly created dimension |

Syntax (COM)

status = ModelDoc->IAddVerticalDimension2 ( x, y, z, &retval )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Output: | (LPDISPLAYDIMENSION) retval | A pointer to the newly created dimension |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

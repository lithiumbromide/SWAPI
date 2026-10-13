---
title: "ModelDoc2::AddVerticalDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddVerticalDimension.htm"
---

# ModelDoc2::AddVerticalDimension

This method is obsolete and has been superseded by [ModelDoc2::AddVerticalDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddVerticalDimension2.htm).

Description

This method creates a vertical dimension for the current selected entities at the specified location.

Syntax (OLE Automation)

retval = ModelDoc2.AddVerticalDimension ( x, y, z)

| Input: | (double) x | Dimension text location in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location in meters |
| Input: | (double) z | Dimension text location in meters |
| Return: | (BOOL) retval | 1 = Success, 0 = Failure |

Syntax (COM)

status = ModelDoc2->AddVerticalDimension ( x, y, z, &retval )

| Input: | (double) x | Dimension text location in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location in meters |
| Input: | (double) z | Dimension text location in meters |
| Output: | (VARIANT_BOOL) retval | 1 = Success, 0 = Failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

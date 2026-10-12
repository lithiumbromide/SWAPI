---
title: "ModelDoc::AddVerticalDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddVerticalDimension.htm"
---

# ModelDoc::AddVerticalDimension

This method is now obsolete and has been superseded by [ModelDoc::AddVerticalDimension2](ModelDoc__AddVerticalDimension2.htm).

Description

This method creates a vertical dimension for the current selected entities at the specified location.

Syntax (OLE Automation)

retval = ModelDoc.AddVerticalDimension ( x, y, z)

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Return: | (BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc->AddVerticalDimension ( x, y, z, &retval )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

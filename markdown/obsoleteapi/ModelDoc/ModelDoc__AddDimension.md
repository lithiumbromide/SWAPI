---
title: "ModelDoc::AddDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddDimension.htm"
---

# ModelDoc::AddDimension

This method is now Obsolete and has been superseded by [ModelDoc::AddDimension2](ModelDoc__AddDimension2.htm).

Description

This method creates a dimension for the current selected entities at the specified location.

Syntax (OLE Automation)

retval = ModelDoc.AddDimension ( x, y, z)

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Return: | (BOOL) retval | 1 = success, 0 = failure |

Syntax (COM)

status = ModelDoc->AddDimension ( x, y, z, &retval )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Output: | (VARIANT_BOOL) retval | 1 = success, 0 = failure |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Dimensions are created based on selection location. For example, creating an angular dimension between two lines will get different results based on which line endpoints are selected. Therefore, if you are using ModelDoc2::SelectByID to select the entities for dimensioning, you should specify the XYZ selection coordinates.

You must also leave the objectName argument empty, because if you pass the objectName argument to ModelDoc2::SelectByID, then the selection routines will try to locate that item without using the coordinates. Because coordinates are ignored when an objectName is passed, the dimensioning routines will not use a specific selection location for the dimension. This will cause unpredictable results in your dimension creation because you cannot be sure which line endpoint is selected by the ModelDoc2::SelectByID routine.

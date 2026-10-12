---
title: "ModelDoc2::AddDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddDimension.htm"
---

# ModelDoc2::AddDimension

This method is obsolete and has been superseded by [ModelDoc2::AddDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddDimension2.htm).

Description

This method creates a dimension for the currently selected entities at the specified location.

Syntax (OLE Automation)

retval = ModelDoc2.AddDimension ( x, y, z)

| Input: | (double) x | Dimension text location in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location in meters |
| Input: | (double) z | Dimension text location in meters |
| Return: | (BOOL) retval | 1 = Success, 0 = Failure |

Syntax (COM)

status = ModelDoc2->AddDimension ( x, y, z, &retval )

| Input: | (double) x | Dimension text location in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location in meters |
| Input: | (double) z | Dimension text location in meters |
| Output: | (VARIANT_BOOL) retval | 1 = Success, 0 = Failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Dimensions are created based on selection location. For example, creating an angular dimension between two lines gets different results based on which line endpoints are selected. Therefore, if you are using ModelDoc2::SelectByID to select the entities for dimensioning, you should specify the XYZ selection coordinates. You must also leave the objectName argument empty, because if you pass the objectName argument to ModelDoc2::SelectByID, then the selection routines tries to locate that item without using the coordinates.

Because coordinates are ignored when an objectName is passed, the dimensioning routines are not able to use a specific selection location for the dimension. This causes unpredictable results in your dimension creation because you cannot be sure which line endpoint is selected by the ModelDoc2::SelectByID routine.

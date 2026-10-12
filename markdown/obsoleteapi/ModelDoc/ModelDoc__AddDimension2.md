---
title: "ModelDoc::AddDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddDimension2.htm"
---

# ModelDoc::AddDimension2

This method is obsolete and has been superseded by [ModelDoc2::AddDimension2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddDimension2.htm).

Description

This method creates a dimension for the current selected entities at the specified location.

Syntax (OLE Automation)

retval = ModelDoc.AddDimension2 ( x, y, z )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Return: | (LPDISPATCH) retval | A pointer to the newly created dimension |

Syntax (COM)

status = ModelDoc->IAddDimension2 ( x, y, z, &retval )

| Input: | (double) x | Dimension text location, in meters |
| --- | --- | --- |
| Input: | (double) y | Dimension text location, in meters |
| Input: | (double) z | Dimension text location, in meters |
| Output: | (LPDISPLAYDIMENSION) retval | A pointer to the newly created dimension |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Be aware that dimensions are created based on selection location. For example, creating an angular dimension between two lines will get different results based on which line endpoints are selected. Therefore, if you are using ModelDoc2::SelectByID to select the entities for dimensioning, you should specify the XYZ selection coordinates.

You must also leave the objectName argument empty, because if you pass the objectName argument to ModelDoc2::SelectByID, then the selection routines will try to locate that item without using the coordinates. Because coordinates are ignored when an objectName is passed, the dimensioning routines will not be able to use a specific selection location for the dimension. This will cause unpredictable results in your dimension creation because you cannot be sure which line endpoint is selected by the ModelDoc2::SelectByID routine.

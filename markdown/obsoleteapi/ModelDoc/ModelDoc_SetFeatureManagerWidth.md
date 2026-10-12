---
title: "ModelDoc::SetFeatureManagerWidth"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_SetFeatureManagerWidth.htm"
---

# ModelDoc::SetFeatureManagerWidth

This method is obsolete and has been superseded by [ModelDoc2::SetFeatureManagerWidth](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetFeatureManagerWidth.htm).

Description

This method sets the width of the Feature Manager design tree in pixels.

Syntax (OLE Automation)

retval = ModelDoc.SetFeatureManagerWidth ( width )

| Input: | (long) width | Width of the FeatureManager design tree view, in pixels |
| --- | --- | --- |
| Output: | (long) retval | Status of the set width operation |

Syntax (COM)

status = ModelDoc->SetFeatureManagerWidth ( width, &retval )

| Input: | (long) width | Width of the FeatureManager design tree view, in pixels |
| --- | --- | --- |
| Output: | (long) retval | Status of the set width operation |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The retval argument indicates the success or failure of the set width operation. A value of 0 indicates the window width was successfully set. A value of -1 indicates that the window width was not successfully set.

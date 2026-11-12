---
title: "ModelDoc::GetFeatureCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFeatureCount.htm"
---

# ModelDoc::GetFeatureCount

This method is obsolete and has been superseded by [ModelDoc2::GetFeatureCount.](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetFeatureCount.htm)

Description

This method returns the number of features in this document.

Syntax (OLE Automation)

retval = ModelDoc.GetFeatureCount ()

| Return: | (long) retval | Number of features in this document, excluding nay subfeatures |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetFeatureCount ( &retval )

| Output: | (long) retval | Number of features in this document, excluding nay subfeatures |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The number of features returned by this method does not include subfeatures. Subfeatures include, for example, mate features within a mate group, drawing views on a sheet, and so on. One way to identify a subfeature is whether it can be returned by Feature::GetFirstSubFeature or Feature::GetNextSubFeature.

This method returns the number of features returned when traversing the feature list with ModelDoc::FirstFeature and Feature::GetNextFeature. This value may be useful in feature traversal or in accessing the feature by position using ModelDoc::FeatureByPositionReverse.

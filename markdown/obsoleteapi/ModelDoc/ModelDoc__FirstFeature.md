---
title: "ModelDoc::FirstFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FirstFeature.htm"
---

# ModelDoc::FirstFeature

This method is obsolete and has been superseded by [ModelDoc2::FirstFeature](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FirstFeature.htm).

Description

This returns the first feature in the document.

Syntax (OLE Automation)

retval = ModelDoc.FirstFeature ()

| Return: | (LPDISPATCH) retval | Pointer to Dispatch object for the first feature in the document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IFirstFeature ( &retval )

| Output: | (LPFEATURE) retval | Pointer to the first feature in the document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For access to the next feature in the FeatureManager design tree and access to subfeatures, see Feature::GetNextFeature and Feature::GetFirstSubFeature, respectively.

If a feature is suppressed, this method still accesses the feature.

Your application should not assume that the name or the order of SolidWorks features is always the same. For example, you should not assume that the first feature in the list is always be a reference plane. Additionally, because feature names are customizable, you cannot assume that the first reference plane feature is named Plane1. See Feature::GetTypeName and Feature::Name for details.

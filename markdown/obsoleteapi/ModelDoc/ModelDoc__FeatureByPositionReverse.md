---
title: "ModelDoc::FeatureByPositionReverse"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureByPositionReverse.htm"
---

# ModelDoc::FeatureByPositionReverse

This method is obsolete and has been superseded by [ModelDoc2::FeatureByPositionReverse](sldworksAPI.chm::/ModelDoc2/ModelDoc2__FeatureByPositionReverse.htm).

Description

This method returns the nth from last feature in the document.

Syntax (OLE Automation)

retval = ModelDoc.FeatureByPositionReverse ( positionFromEnd )

| Input: | (long) positionFromEnd | Number of feature from last in the FeatureManager design tree; 0 gives last in the FeatureManager design tree |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object for the nth from last feature in the document |

Syntax (COM)

status = ModelDoc->IFeatureByPositionReverse ( positionFromEnd, &retval )

| Input: | (long) positionFromEnd | Number of feature from last in the FeatureManager design tree; 0 gives last in the FeatureManager design tree |
| --- | --- | --- |
| Output: | (LPFEATURE) retval | Pointer to Dispatch object for the nth from last feature in the document |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Your application should not assume that the name or the order of SolidWorks features are always the same. For example, you should not assume that the last feature in the list is always the Annotations folder. In addition, because feature names are customizable, you cannot assume that the first reference plane feature is named Plane1 or that the Annotations folder is called Annotations. See Feature::GetTypeName and Feature::Name for details.

Because SolidWorks does not guarantee the name or positioning of default features, your application should not make any assumptions in this area. If your application is trying to access geometric features (for example, sketches, fillets, bosses, reference surfaces, and so on) using this method, then it is safest to determine the number of default features at the top and bottom of the tree for each particular document. This could be done once for each document by traversing the FeatureManager design tree using ModelDoc::FirstFeature and Feature::GetNextFeature. Based on the feature type, Feature::GetTypeName, you can recognize where new features will be placed in the FeatureManager design tree upon creation.

For example, a new fillet will be created at position (n-1) where n is the total number of features in the part. Therefore, to obtain this Feature object the positionFromEnd argument should be passed as 1. This allows you to obtain the newly created fillet feature, which is 1 from the bottom of the list.

If you are using this method to obtain the last Feature object created by your application, then, as a precaution, you may also want to check the feature count immediately before your feature creation and immediately after your feature creation. If the feature count has increased by 1, then it is relatively safe to assume that only your application has modified the document and added a feature. You should be aware that this is not a guarantee because other third-party applications may be running and may have also modified your document. Feature count can be determined by calling ModelDoc::GetFeatureCount.

For access to the first feature in the FeatureManager design tree and access to subfeatures, see [ModelDoc::FirstFeature](ModelDoc__FirstFeature.htm) and Feature::GetFirstSubFeature , respectively.

If a feature is suppressed, this method still lets you access the feature.

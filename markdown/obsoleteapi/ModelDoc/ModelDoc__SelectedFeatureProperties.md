---
title: "ModelDoc::SelectedFeatureProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectedFeatureProperties.htm"
---

# ModelDoc::SelectedFeatureProperties

This method is obsolete and has been superseded by [ModelDoc2::SelectedFeatureProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectedFeatureProperties.htm).

Description

This method sets the property values of the selected feature.

Syntax (OLE Automation)

retval = ModelDoc.SelectedFeatureProperties ( rgbColor, ambient, diffuse, specular, shininess, transparency, emission, usePartProps, suppressed, featureName)

| Input: | (long) rgbColor | Feature color |
| --- | --- | --- |
| Input: | (double) ambient | Feature ambient value; valid range is from 0 to 1 |
| Input: | (double) diffuse | Feature diffuse value; valid range is from 0 to 1 |
| Input: | (double) specular | Feature specular value; valid range is from 0 to 1 |
| Input: | (double) shininess | Feature shininess value; valid range is from 0 to 1 |
| Input: | (double) transparency | Feature transparency value; valid range is from 0 to 1 |
| Input: | (double) emission | Feature emission value; valid range is from 0 to 1 |
| Input: | (BOOL) usePartProps | TRUE if the feature will inherit the part properties, FALSE otherwise |
| Input: | (BOOL) suppressed | TRUE if the feature is suppressed, FALSE otherwise |
| Input: | (BSTR) featureName | Name of the feature |
| Return: | (BOOL) retval | TRUE if successfully changed the feature properties, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SelectedFeatureProperties ( rgbColor, ambient, diffuse, specular, shininess, transparency, emission, usePartProps, suppressed, featureName, &retval )

| Input: | (long) rgbColor | Feature color |
| --- | --- | --- |
| Input: | (double) ambient | Feature ambient value; valid range is from 0 to 1 |
| Input: | (double) diffuse | Feature diffuse value; valid range is from 0 to 1 |
| Input: | (double) specular | Feature specular value; valid range is from 0 to 1 |
| Input: | (double) shininess | Feature shininess value; valid range is from 0 to 1 |
| Input: | (double) transparency | Feature transparency value; valid range is from 0 to 1 |
| Input: | (double) emission | Feature emission value; valid range is from 0 to 1 |
| Input: | (VARIANT_BOOL) usePartProps | TRUE if the feature will inherit the Part properties, FALSE otherwise |
| Input: | (VARIANT_BOOL) suppressed | TRUE if the feature is suppressed, FALSE otherwise |
| Input: | (BSTR) featureName | Name of the feature |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully changed the feature properties, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is different from ModelDoc::SelectedFaceProperties and ModelDoc::SelectedEdgeProperties in that it will allow you to change the name of this feature. The reasoning is that all features have names; whereas, a face or edge typically have a name only if it is being referenced. Because it is dangerous to change the name of a referenced object, we do not allow you to programmatically change the names of faces or edges. See Feature::Name and PartDoc::SetEntityName.

This method requires the feature to be selected. To select the feature programmatically, you can use ModelDoc::SelectByID and pass in the feature name along with the appropriate object type (for example,"BODYFEATURE", "ATTRIBUTE", "PLANE", "SKETCH", and so on) and the selection coordinates 0,0,0. You can determine the feature name and object type using Feature::Name and Feature::GetTypeName, respectively.

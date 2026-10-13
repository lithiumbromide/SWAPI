---
title: "WizardHoleFeatureData::Face"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__Face.htm"
---

# WizardHoleFeatureData::Face

This property is obsolete and has been superseded by [WizardHoleFeatureData2::Face](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__Face.htm).

Description

This property gets or sets the hole wizard feature end condition face.

Syntax (OLE Automation)

face = WizardHoleFeatureData.Face (VB Get property)

WizardHoleFeatureData.Face = face (VB Set property)

face = WizardHoleFeatureData.GetFace ( ) (C++ Get property)

WizardHoleFeatureData.SetFace ( face ) (C++ Set property)

| Property: | (LPDISPATCH) face | Pointer to a dispatch object, the end condition face, or NULL if the operation fails |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_IFace ( &face )

status = WizardHoleFeatureData ->put_IFace ( face )

| Property: | (LPFACE) face | Pointer to the end condition Face object or NULL if the operation fails |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call WizardFeatureData::AccessSelections before using this property.

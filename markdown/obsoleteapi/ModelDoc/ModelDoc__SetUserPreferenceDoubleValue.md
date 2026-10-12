---
title: "ModelDoc::SetUserPreferenceDoubleValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceDoubleValue.htm"
---

# ModelDoc::SetUserPreferenceDoubleValue

This method is obsolete and has been superseded by [ModelDoc2::SetUserPreferenceDoubleValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceDoubleValue.htm).

Description

This method sets various user preference values for this ModelDoc object. This method is intended for user preferences of type double.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceDoubleValue ( userPreferenceValue, value)

| Input: | (long) userPreferenceValue | User preference value you wish to get as defined in swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Input: | (double) value | Numeric value you wish to give to the user preference specified in userPreferenceValue |
| Return: | (BOOL) retval | TRUE if the user preference was set successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetUserPreferenceDoubleValue ( userPreferenceValue, value, &retval )

| Input: | (long) userPreferenceValue | User preference value you wish to get as defined in swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Input: | (double) value | the numeric value you wish to give to the user preference specified in userPreferenceValue |
| Output: | (VARIANT_BOOL) retval | TRUE if the user preference was set successfully, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is equivalent to using the Tools, Options menu item in SolidWorks.

To use this method, choose one of the available items from the swUserPreferenceDoubleValue_e enumeration. Then call this method and pass in the desired user preference from the swUserPreferenceDoubleValue_e enumeration and the desired value for that user preference.

For a description of the user preference types and the types supported by each object, see swUserPreferenceDoubleValue_e.

---
title: "ModelDoc::GetUserPreferenceDoubleValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceDoubleValue.htm"
---

# ModelDoc::GetUserPreferenceDoubleValue

This method is obsolete and has been superseded by [ModelDoc2::GetUserPreferenceDoubleValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceDoubleValue.htm).

Description

This method gets various user preference values for this ModelDoc object. This method is intended for user preferences of type double.

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceDoubleValue ( userPreferenceValue)

| Input: | (long) userPreferenceValue | User-preference value you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Return: | (double) retval | Numeric value of the user preference specified in userPreferenceValue |

Syntax (COM)

status = ModelDoc->GetUserPreferenceDoubleValue ( userPreferenceValue, &value )

| Input: | (long) userPreferenceValue | User-preference value you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Output: | (double) value | Numeric value of the user preference specified in userPreferenceValue |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as selecting the Tools, Options menu item.

To use this method, choose one of the available items from swUserPreferenceDoubleValue_e. The value returned is based on which user preference you are querying.

For a description of the user preference types and the object supported by each type, see swUserPreferenceDoubleValue_e.

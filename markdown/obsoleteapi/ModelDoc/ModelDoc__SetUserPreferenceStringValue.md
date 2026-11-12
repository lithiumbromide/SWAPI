---
title: "ModelDoc::SetUserPreferenceStringValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceStringValue.htm"
---

# ModelDoc::SetUserPreferenceStringValue

This method is obsolete and has been superseded by [ModelDoc2::SetUserPreferenceStringValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceStringValue.htm).

Description

This method sets various system default user preference values. This method is intended for user preferences of type string.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceStringValue ( userPreference, userPrefVal )

| Input: | ( long ) userPreference | User preference value you wish to set as defined in swUserPreferenceStringValue_e |
| --- | --- | --- |
| Input: | ( BSTR ) userPrefVal | String value of the user preference specified in userPreference |
| Return: | (BOOL) retval | TRUE if User Preference value was replaced |

Syntax (COM)

status = ModelDoc->SetUserPreferenceStringValue ( userPreference, userPrefVal, &retval )

| Input: | ( long ) userPreference | User preference value you wish to set as defined in swUserPreferenceStringValue_e |
| --- | --- | --- |
| Input: | ( BSTR ) userPrefVal | the string value of the user preference specified in userPreference |
| Output: | (VARIANT_BOOL) retval | TRUE if User Preference value was replaced |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is equivalent to using the Tools, Options menu item in SolidWorks.

To use this method, choose one of the available items from the swUserPreferenceStringValue_e enumeration. The value passed in the userPrefVal argument will become the current system default value for the user preference you are setting.

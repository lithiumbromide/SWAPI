---
title: "ModelDoc::GetUserPreferenceStringValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceStringValue.htm"
---

# ModelDoc::GetUserPreferenceStringValue

This method is obsolete and has been superseded by [ModelDoc2::GetUserPreferenceStringValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceStringValue.htm).

Description

This method gets various system default user preference values. This method is intended for user preferences of type string.

Syntax (OLE Automation)

userPrefVal = ModelDoc.GetUserPreferenceStringValue ( userPreference )

| Input: | ( long ) userPreference | User-preference value you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceStringValue_e |
| --- | --- | --- |
| Return: | ( BSTR ) userPrefVal | String value of the user preference specified in userPreference |

Syntax (COM)

status = ModelDoc->GetUserPreferenceStringValue ( userPreference, &userPrefVal )

| Input: | ( long ) userPreference | User-preference value you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceStringValue_e |
| --- | --- | --- |
| Output: | ( BSTR ) userPrefVal | String value of the user preference specified in userPreference |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as using the Tools, Options menu item.

To use this method, choose one of the available items from the swUserPreferenceStringValue_e enumeration. The value returned is the current system default value for the user preference that you are querying.

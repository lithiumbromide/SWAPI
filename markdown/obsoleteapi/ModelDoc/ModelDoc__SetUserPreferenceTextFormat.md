---
title: "ModelDoc::SetUserPreferenceTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceTextFormat.htm"
---

# ModelDoc::SetUserPreferenceTextFormat

This method is obsolete and has been superseded by [ModelDoc2::SetUserPreferenceTextFormat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ISetUserPreferenceTextFormat.htm).

Description

This method sets the specified integer user preference value on this document

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceTextFormat ( userPreferenceValue, value )

| Input: | (long) userPreferenceValue | User preference you wish to change as defined in swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Input: | (LPDISPATCH) value | Dispatch pointer to the TextFormat object you wish to give to the user preference specified in userPreferenceValue |
| Return: | (BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise. |

Syntax (COM)

status = ModelDoc->ISetUserPreferenceTextFormat ( userPreferenceValue, value, &retval )

| Input: | (long) userPreferenceValue | User preference you wish to change as defined in swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT) value | Pointer to the TextFormat object you wish to give to the user preference specified in userPreferenceValue |
| Output: | (VARIANT_BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is equivalent to using the Tools, Options menu item in SolidWorks.

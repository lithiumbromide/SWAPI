---
title: "ModelDoc::GetUserPreferenceTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceTextFormat.htm"
---

# ModelDoc::GetUserPreferenceTextFormat

This method is obsolete and has been superseded by [ModelDoc2::GetUserPreferenceTextFormat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceTextFormat.htm).

Description

This method gets the specified text format user preference from this document.

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceTextFormat ( userPreferenceValue, retval )

| Input: | (long) userPreferenceValue | User-preference toggle you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the TextFormat object associated with the specified userPreferenceValue setting. |

Syntax (COM)

status = ModelDoc->IGetUserPreferenceTextFormat ( userPreferenceValue, &retval )

| Input: | (long) userPreferenceValue | User-pPreference toggle you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Output: | (LPTEXTFORMAT) retval | Pointer to the TextFormat object associated with the specified userPreferenceValue setting |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is the same as using the Tools, Options menu item.

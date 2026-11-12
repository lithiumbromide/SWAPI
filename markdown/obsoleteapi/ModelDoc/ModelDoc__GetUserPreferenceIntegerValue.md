---
title: "ModelDoc::GetUserPreferenceIntegerValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceIntegerValue.htm"
---

# ModelDoc::GetUserPreferenceIntegerValue

This method is obsolete and has been superseded by [ModelDoc2::GetUserPreferenceIntegerValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceIntegerValue.htm).

Description

This method gets the specified integer user-preference value from this document

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceIntegerValue ( userPreferenceValue )

| Input: | (long) userPreferenceValue | User-preference toggle you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Return: | (long) retval | Value associated with the specified userPreferenceValue setting |

Syntax (COM)

status = ModelDoc->GetUserPreferenceIntegerValue ( userPreferenceValue, &retval )

| Input: | (long) userPreferenceValue | User-preference toggle you wish to get; for a complete and up-to-date list of available options, see swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Output: | (long) retval | Value associated with the specified userPreferenceValue setting |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is this same as using the Tools, Options menu item.

To use this method, choose one of the available items from swUserPreferenceIntegerValue_e.

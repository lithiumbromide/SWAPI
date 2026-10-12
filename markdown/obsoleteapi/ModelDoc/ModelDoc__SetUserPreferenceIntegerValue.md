---
title: "ModelDoc::SetUserPreferenceIntegerValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceIntegerValue.htm"
---

# ModelDoc::SetUserPreferenceIntegerValue

This method is obsolete and has been superseded by [ModelDoc2::SetUserPreferenceIntegerValu](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceIntegerValue.htm)e.

Description

This method sets various user preference integer values.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceIntegerValue ( userPreferenceValue, value )

| Input: | (long) userPreferenceValue | Toggle to change as defined by swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Input: | (long) value | Numeric value to give to the user preference specified in userPreferenceValue |
| Return: | (BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetUserPreferenceIntegerValue ( userPreferenceValue, value, &retval )

| Input: | (long) userPreferenceValue | Toggle to change as defined by swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Input: | (long) value | Numeric value to give to the user preference specified in userPreferenceValue |
| Output: | (VARIANT_BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

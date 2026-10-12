---
title: "ModelDoc::GetUserPreferenceToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceToggle.htm"
---

# ModelDoc::GetUserPreferenceToggle

This method is obsolete and has been superseded by [ModelDoc2::GetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceToggle.htm).

Description

This method gets various user preference toggles for this ModelDoc object.

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceToggle ( userPreferenceToggle)

| Input: | (long) userPreferenceToggle | User-preference toggle you wish to ge; for a complete and up-to-date list of available options, see swUserPreferenceToggle_e |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the item specified by userPreferenceToggle is currently toggled on, FALSE if the item is currently toggled off |

Syntax (COM)

status = ModelDoc->GetUserPreferenceToggle ( userPreferenceToggle, &retval )

| Input: | (long) userPreferenceToggle | User-preference toggle you wish to ge; for a complete and up-to-date list of available options, see swUserPreferenceToggle_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the item specified by userPreferenceToggle is currently toggled on, FALSE if the item is currently toggled off |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as using the Tools, Options menu item.

To use this method, choose one of the available items from swUserPreferenceToggle_e. The value returned is TRUE if the item is currently toggled on, and FALSE if the item is currently toggled off.

For example,

boolean curState = m_ModelDoc.GetUserPreferenceToggle( swIgnoreFeatureColors )

For a description of the user preference types, refer to swUserPreferenceToggle_e.

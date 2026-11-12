---
title: "ModelDoc::SetUserPreferenceToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceToggle.htm"
---

# ModelDoc::SetUserPreferenceToggle

This method is obsolete and has been superseded by [ModelDoc2::SetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceToggle.htm).

Description

This method sets various user preference toggles.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceToggle ( userPreferenceValue, onFlag)

| Input: | (long) userPreferenceValue | User preference toggle you wish to change as defined in swUserPreferenceToggle_e |
| --- | --- | --- |
| Input: | (BOOL) onFlag | TRUE if you wish to toggle the item specified by userPreferenceToggle on, FALSE if you wish to toggle the item off |
| Return: | (BOOL) retval | TRUE if the setting was made successfully, = FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetUserPreferenceToggle ( userPreferenceValue, onFlag, &retval )

| Input: | (long) userPreferenceValue | User preference toggle you wish to change as defined in swUserPreferenceToggle_e |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) onFlag | TRUE if you wish to toggle the item specified by userPreferenceToggle on, FALSE if you wish to toggle the item off |
| Output: | (VARIANT_BOOL) retval | TRUE if the setting was made successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is equivalent to using the Tools, Options menu item in SolidWorks.

To use this method, choose one of the available items from the swUserPreferenceToggle_e enumeration. Pass in turnOn = TRUE if you wish the item to be toggled on, and FALSE if the you want the item toggled off.

For example, the following command will force SolidWorks to ignore feature colors:

```vb
swapp.SetUserPreferenceToggle( swIgnoreFeatureColors, TRUE )
```

For a description of the user preference types and the types supported by each object see swUserPreferenceToggle_e.

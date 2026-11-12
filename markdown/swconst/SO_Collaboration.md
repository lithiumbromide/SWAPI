---
title: "System Options > Collaboration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Collaboration.htm"
---

# System Options > Collaboration

This topic contains two tables. The information in the table:

- appearing immediately after the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete or have been moved to another location.

THe Collaboration settings are not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Enable multi-user environment | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabEnableMultiuser) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabEnableMultiuser, < OnFlag >) | Boolean value | Specifies whether to enable multi-user environment |
| Add shortcut menu items for multi-user environment | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabAddShortcutMenuItems) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabAddShortcutMenuItems, < OnFlag >) | Boolean value | Specifies whether to add shortcut menu items for multi-user environment |
| Check if files opened read-only have been modified by other users | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabCheckReadOnlyModifiedByOthers) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabCheckReadOnlyModifiedByOthers, < OnFlag >) | Boolean value | Specifies whether to check if files opened read-only have been modified by others; works with swUserPreferenceIntegerValue_e.swCollabCheckReadOnlyModifiedInterval |
| Check files every < n > minutes | ISldWorks::GetUserPreferenceIntegerValue (wUserPreferenceIntegerValue_e.swCollabCheckReadOnlyModifiedInterval) ISldWorks::SetUserPreferenceIntegerValue (wUserPreferenceIntegerValue_e.swCollabCheckReadOnlyModifiedInterval, swCollabCheckReadOnlyModifiedInterval_e .< Value >) | See swCollabCheckReadOnlyModifiedInterval_e for valid options | Works with swUserPreferenceToggle_e.swCollabCheckReadOnlyModifiedByOthers |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swCollabAddTimeStampToComments | Moved to Tools > Options > FeatureManager |
| swCollabShowCommentsInPropertyManager | Moved to Tools > Options > FeatureManager |

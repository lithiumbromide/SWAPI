---
title: "System Options > Synchronize Settings"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_SynchronizeSettings.htm"
---

# System Options > Synchronize Settings

This dialog is only available in SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

| Setting | Get/Set Methods | Return value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Last Synchronization | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swLastSynchronizationTimeStamp) | String value |  |
| Automatic Synchronization - Automatically synchronize settings | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticSyncSettings) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutomaticSyncSettings, < OnFlag >) | Boolean value | When set to true, specified settings to include are automatically synchronized when logging in and out of SOLIDWORKS Design connected to the 3DEXPERIENCE platform |
| Automatic Synchronization - Settings to include - System Options | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_SystemOptions) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_SystemOptions, < OnFlag >) | Boolean value | Valid only if swUserPreferenceToggle_e.swAutomaticSyncSettings is set to true |
| Automatic Synchronization - Settings to include - File Locations | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_FileLocations) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_FileLocations, < OnFlag >) | Boolean value | Valid only if swUserPreferenceToggle_e.swAutomaticSyncSettings is set to true |
| Automatic Synchronization - Settings to include - Customizations | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_Customizations) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSyncSettingsToInclude_Customizations, < OnFlag >) | Boolean value | Valid only if swUserPreferenceToggle_e.swAutomaticSyncSettings is set to true |
| Synchronize Now - Upload Settings... | ISldWorks::UploadToMySolidWorksSettings | Integer value |  |
| Synchronize Now - Download Settings... | ISldWorks::DownloadFromMySolidWorksSettings | Integer value |  |

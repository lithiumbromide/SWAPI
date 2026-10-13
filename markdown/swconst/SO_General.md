---
title: "System Options > General"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_General.htm"
---

# System Options > General

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

| Setting | Get/Set Methods | Return Value or <Value> or < O nFlag > | Comment |
| --- | --- | --- | --- |
| Recent documents - Maximum recent documents displayed | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swMaximumRecentDocuments) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swMaximumRecentDocuments, < Value >) | 1 <= Integer value <= 100 | Specifies how many documents to display in the File > Open Recent list |
| Recent documents - Include documents opened from other documents | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIncludeDocumentsOpenedFromOtherDocuments) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIncludeDocumentsOpenedFromOtherDocuments, <OnFlag> ) | Boolean value | Specifies whether to include the documents opened from other documents in the File > Open Recent list |
| Recent documents - Open last used document(s) at startup | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swOpenLastUsedDocumentAtStart) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swOpenLastUsedDocumentAtStart, <OnFlag> ) | Boolean value | Specifies whether to open the last-used document when starting up SOLIDWORKS software; true if always, false if never |
| Input dimension value | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swInputDimValOnCreate) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swInputDimValOnCreate, <OnFlag> ) | Boolean value | Specifies whether to automatically display Modify dialog when dimensioning new entities |
| Single command per pick | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSingleCommandPerPick) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSingleCommandPerPick, <OnFlag> ) | Boolean value | Specifies whether to deselect sketch and dimension tools after each use |
| Use shaded face highlighting | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseShadedFaceHighlight) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseShadedFaceHighlight, <OnFlag> ) | Boolean value | Specifies whether selected faces are displayed in a solid color (green by default) |
| Show thumbnail graphics in File Explorer | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swThumbnailGraphics) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swThumbnailGraphics, <OnFlag> ) | Boolean value | Specifies whether thumbnail graphic instead of an icon in File Explorer is displayed for each SOLIDWORKS part or assembly document |
| Use system separator for dimensions | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseSystemSeparatorForDims) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseSystemSeparatorForDims, <OnFlag> ) | Boolean value | Specifies whether default system decimal separator is used when displaying decimal numbers |
| Use English language menus | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseEnglishLanguage) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseEnglishLanguage, <OnFlag> ) | Boolean value | Specifies whether to change to English if another language was selected when SOLIDWORKS software was installed; SOLIDWORKS software must be restarted for this change to take effect |
| Use English language feature and file names | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseEnglishLanguageFeatureNames) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseEnglishLanguageFeatureNames, <OnFlag> ) | Boolean value | Specifies whether to use English feature and file names in languages other than English |
| Enable Confirmation Corner | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEnableConfirmationCorner) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEnableConfirmationCorner, <OnFlag> ) | Boolean value | Specifies whether to display Confirmation Corner in the upper-right corner of the graphics area |
| Auto-show PropertyManager | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoShowPropertyManager) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoShowPropertyManager, <OnFlag> ) | Boolean value | Specifies whether to automatically display PropertyManager when editing an entity |
| Auto-size PropertyManager when panels are split | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSizePropertyManager) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSizePropertyManager, <OnFlag> ) | Boolean value | Specifies whether to autosize PropertyManager pages when panels are split |
| Automatically edit macro after recording | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEditMacroAfterRecord) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEditMacroAfterRecord, <OnFlag> ) | Boolean value | Specifies whether to automatically edit a macro after recording it NOTE: If after recording a macro you select to save the macro as all macro types (. swp , . csproj , and . vbproj ), then this option has no effect. |
| Stop VSTA debugger on macro exit | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swStopDebuggingVstaOnExit) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, <OnFlag> ) | Boolean value | Specifies whether to stop the debugger when the macro exits main() IMPORTANT: When debugging VSTA macros with user-interface components such as PropertyManager pages, manipulators, or other objects that use events or handler objects, it is necessary to keep the debugger running after the main() method of the VSTA macro exits. |
| Enable FeatureXpert | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUserEnableAutoFix) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUserEnableAutoFix, <OnFlag> ) | Boolean value | Specifies whether to enable FeatureXpert |
| Enable Freeze bar | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUserEnableFreezeBar) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUserEnableFreezeBar, <OnFlag> ) | Boolean value | Specifies whether to enable or disable the freeze bar |
| When rebuild error occurs | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRebuildErrorAction) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swRebuildErrorAction, swStopContinuePrompt_e.< Value >) | See swStopContinuePrompt_e for valid options |  |
| Custom property used as component description | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swCustomPropertyUsedAsComponentDescription, < Value >) | String value |  |
| Show latest Technical Alerts and News in Welcome dialog (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowNewsFeedsInTaskPane) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowNewsFeedsInTaskPane, <OnFlag> ) | Boolean value | Specifies whether to show the latest Technical Alerts and News in the Welcome dialog |
| Check for solutions when SOLIDWORKS crashes | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swCheckCrashSolutions) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swCheckCrashSolutions, <OnFlag> ) | Boolean value |  |
| Enable sounds for SOLIDWORKS events | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEnableSoundsForSOLIDWORKSEvents) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEnableSoundsForSOLIDWORKSEvents, <OnFlag> ) | Boolean value |  |
| Allow cosmetic threads for upgrade | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEnableAllowCosmeticThreadsUpgrade) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEnableAllowCosmeticThreadsUpgrade, <OnFlag> ) | Boolean value | Specifies whether to upgrade cosmetic threads to the latest design |
| SOLIDWORKS Customer Experience Improvement Program - Help make SOLIDWORKS products better by automatically sending your log files to DS SOLIDWORKS Corporation (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPerformanceFeedback) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPerformanceFeedback, swPerformanceFeedback_e.< Value >) | See swPerformanceFeedback_e for valid options | Specifies whether to enable or disable performance feedback or when to remind the user to enable it |

Obsolete Enumerators

| Enumerator | Comment |
| --- | --- |
| swCreateConfigurationTableOnOpen | Obsolete |
| swEnablePerformanceEmail | Obsolete |
| swEnablePerformanceFeedback | Obsolete; use swUserPreferenceIntegerValue_e .swPerformanceFeedback (shown in previous table) |
| swEnablePropertyManager | Obsolete; always enabled |
| swMaximizeDocumentOnOpen | Obsolete |
| swSaveEModelData | Obsolete |
| swShowDimensionNames | Obsolete |
| swEnableVSTAVersion3 | Obsolete |

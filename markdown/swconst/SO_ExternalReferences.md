---
title: "System Options > ExternalReferences"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_ExternalReferences.htm"
---

# System Options > ExternalReferences

## System Options > External References

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture of the dialog corresponds to the settings on that dialog.
- titled [Obsolete Enumerators](#Obsolete) contains enumerators that previously appeared on the dialog but are now obsolete.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Open referenced documents with read-only access (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefOpenReadOnly) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefOpenReadOnly, < OnFlag >) | Boolean value | Specifies whether to open referenced documents as read-only |
| Don't prompt to save read-only referenced documents (discard changes) (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefNoPromptOrSave) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefNoPromptOrSave, < OnFlag >) | Boolean value | Specifies whether to close read-only reference documents without prompting or attempting to save changes made to them when saving or closing the parent document |
| Allow multiple contexts for parts when editing in assembly | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefMultipleContexts) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefMultipleContexts, < OnFlag >) | Boolean value | Specifies whether to create external references to a single part from more than one assembly context |
| Load referenced documents | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLoadExternalReferences) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swLoadExternalReferences, swLoadExternalReferences_e.< Value >) | See swLoadExternalReferences_e for valid options | Note: If this setting is swLoadExternalReferences_e.swLoadExternalReferences_None, then IDocumentSpecification::LoadExternalReferencesInMemory is not observed |
| Load documents in memory only | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefLoadRefDocsInMemory) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefLoadRefDocsInMemory, < OnFlag >) | Boolean value | Specifies whether to load reference documents in memory only This setting (whether in the user interface or through the API) is ignored when opening documents through the API because IDocumentSpecification::LoadExternalReferencesInMemory and ISldWorks::OpenDoc6 ( swOpenDocOptions_e .swOpenDocOptions_LoadExternalReferencesInMemory) have sole control over reference loading |
| Search external references in - Reference Documents specified in File Location (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseFolderSearchRules) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseFolderSearchRules, < OnFlag >) | Boolean value | Specifies whether to search the Referenced Documents list of folders in the File Locations Options dialog |
| Search external references in - Reference Documents specified in File Location - Include sub-folders (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefIncludeSubFolders) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefIncludeSubFolders, < OnFlag >) | Boolean value | Specifies whether to search for reference documents in sub-folders in the specified file location; valid only if Reference Documents specified in File Location is true |
| Search external references in - Reference Documents specified in File Location - Exclude active folders and recent save locations (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefExcludeActiveFoldersAndRecentSaveLocations) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefExcludeActiveFoldersAndRecentSaveLocations, < OnFlag >) | Boolean value | Specifies whether to block searching for reference documents in open folders and folders containing recently saved items; valid only if Reference Documents specified in File Location is true |
| Update out-of-date linked design tables to (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExternalReferencesUpdateOutOfDateLinkedDesignTable) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExternalReferencesUpdateOutOfDateLinkedDesignTable, swExternalReferencesUpdateOutOfDateLinkedDesignTable_e.< Value >) | See swExternalReferencesUpdateOutOfDateLinkedDesignTable_e for valid options |  |
| Assemblies - Automatically generate names for referenced geometry | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefAutoGenNames) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefAutoGenNames, < OnFlag >) | Boolean value | Specifies whether to automatically generate names for referenced geometry |
| Assemblies - Update component names when documents are replaced (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefUpdateCompNames) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefUpdateCompNames, < OnFlag >) | Boolean value | Specifies whether to mate to read-only parts using internal face IDs of the parts or to replace components using surface identifiers to write-access parts |
| Assemblies - Allow creation of references external to the model | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAllowCreationOfReferencesExternalToModel) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAllowCreationOfReferencesExternalToModel, < OnFlag >) | Boolean value | Specifies whether to permit creation of external references when designing in the context of an assembly |
| Assemblies - Allow creation of references external to the model - Reference component type: | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swReferenceOnlyEnvelopeComponentType) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swReferenceOnlyEnvelopeComponentType, < OnFlag >) | Boolean value | True if only envelope component, false if any component |
| Assemblies - Allow creation of references external to the model - In the context of: | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swReferenceInContextOfTopLevelAssembly) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swReferenceInContextOfTopLevelAssembly, < OnFlag >) | Boolean value | True if in context of top level assembly, false if in context of same subassembly |
| Show "x" in feature tree for broken external references | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefShowXInFeatureTree) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefShowXInFeatureTree, < OnFlag >) | Boolean value | Specifies whether to hide or show the x that appears in the FeatureManager design tree to indicate broken references |
| Force referenced document to save to current major version | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefForceSaveToCurrentVersion) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swExtRefForceSaveToCurrentVersion, < OnFlag >) | Boolean value |  |

**Obsolete Enumerators**

| Enumerator | Comment |
| --- | --- |
| swExternalReferencesDisable | Obsolete |
| swIncludeSubfoldersForDrawingsSearchInPackAndGo | Obsolete |

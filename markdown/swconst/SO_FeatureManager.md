---
title: "System Options > FeatureManager"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_FeatureManager.htm"
---

# System Options > FeatureManager

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Scroll selected item into view | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerEnsureVisible) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerEnsureVisible,
< OnFlag >) | Boolean value | Specifies whether FeatureManager design tree should automatically scroll
to display feature icon related to selected items in graphics area |
| Name feature on creation | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerNameFeatureWhenCreated) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerNameFeatureWhenCreated,
< OnFlag >) | Boolean value | Specifies to automatically select new feature in FeatureManager design
tree to name it |
| Arrow key navigation | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerKeyboardNavigation) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerKeyboardNavigation,
< OnFlag >) | Boolean value | Specifies whether arrow keys can be used to traverse FeatureManager
design tree, and expand or collapse design tree and its contents |
| Dynamic highlight | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerDynamicHighlight) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerDynamicHighlight,
< OnFlag >) | Boolean value | Specifies whether geometry in graphics area is highlighted when pointer
passes over item in FeatureManager design tree |
| Auto-resolve lightweight components upon expansion in FeatureManager tree | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoResolveLightweightCompUponExpInFMTree) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoResolveLightweightCompUponExpInFMTree,
< OnFlag >) | Boolean value | Specifies whether to automatically resolve lightweight components when they
are expanded in the FeatureManager design tree |
| Use transparent flyout FeatureManager tree in parts/assemblies | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerTransparentFlyout) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerTransparentFlyout,
< OnFlag >) | Boolean value | Specifies whether to use transparent flyout FeatureManager in part and
assembly documents |
| Enable FeatureManager tree filter | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerEnableTreeFilter) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerEnableTreeFilter,
< OnFlag >) | Boolean value | Specifies whether to display the
FeatureManager design tree filter Unlike the user interface, you can turn this setting on or
off when a model document is open |
| Allow component files to be renamed from FeatureManager tree (Not
supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e. swFeatureManagerEnableRenamingComponent ) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e. swFeatureManagerEnableRenamingComponent ,
< OnFlag >) | Boolean value | Specifies whether to enable renaming components |
| Enable preview of hidden components | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e. swFeatureManagerEnablePreviewHiddenComponents ) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e. swFeatureManagerEnablePreviewHiddenComponents ,
< OnFlag >) | Boolean value | Specifies whether to enable preview of hidden components |
| Edit name with slow double click | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e. sw EditNameWithSlowDoubleClick ) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e. swEditNameWithSlowDoubleClick ,
< OnFlag >) | Boolean value |  |
| Show translated feature names in FeatureManager tree | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerShowTranslatedNameInFMTree) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swFeatureManagerShowTranslatedNameInFMTree,
< OnFlag >) | Boolean value |  |
| Language drop-down | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerTranslatedLanguage) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerTranslatedLanguage,
swAutoHideShowResponse_e.< Value >) | See swUserPreferencesLanguages_e for valid options | Valid only if
swUserPreferenceToggle_e.swFeatureManagerShowTranslatedNameInFMTree is set to
true. |
| Override document level tree display | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swOverrideTreeDisplaySysSettings) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swOverrideTreeDisplaySysSettings,
< OnFlag >) | Boolean value |  |
| Comments - Automatically add timestamp to comments | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabAddTimeStampToComments) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabAddTimeStampToComments,
< OnFlag >) | Boolean value |  |
| Comments - Show Comments in PropertyManager | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabShowCommentsInPropertyManager) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swCollabShowCommentsInPropertyManager,
< OnFlag >) | Boolean value |  |
| Select a configuration view for the FeatureManager Tree Area - Only CAD
Family View or Both CAD Family and Configurations (SOLIDWORKS Connected
only) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swConfigurationViewForFeatureManagerTree) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swConfigurationViewForFeatureManagerTree,
swFeatureManagerTreeViewCADFamily_e.< Value >) | See swFeatureManagerTreeViewCADFamily_e for valid options |  |
| Hide/show tree items - Blocks | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerBlocksVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerBlocksVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Design Binder | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerDesignBinderVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerDesignBinderVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Annotations | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerAnnotationsVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerAnnotationsVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Solid Bodies | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSolidBodiesVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSolidBodiesVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Surface Bodies | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSurfaceBodiesVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSurfaceBodiesVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Tables | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerTableFolderVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerTableFolderVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Favorites | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerFavorites) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerFavorites,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - eDrawing Markups (not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerEDrawingMarkups) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerEDrawingMarkups,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Selection Sets | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSelectionSetsVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSelectionSetsVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Equations | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerEquationsVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerEquationsVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Material | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMaterialVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMaterialVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Default Planes | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerDefaultPlanesVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerDefaultPlanesVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Origin | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerOriginVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerOriginVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Mate References | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMateReferencesVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMateReferencesVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Design Table | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerDesignTableVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerDesignTableVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Sensors | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSensorVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerSensorVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - History | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerHistory) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerHistory,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Graphic
Bodies | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMeshBodiesVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMeshBodiesVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |
| Hide/show tree items - Markups | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMarkupsVisibility) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swFeatureManagerMarkupsVisibility,
swAutoHideShowResponse_e.< Value >) | See swAutoHideShowResponse_e for valid options |  |

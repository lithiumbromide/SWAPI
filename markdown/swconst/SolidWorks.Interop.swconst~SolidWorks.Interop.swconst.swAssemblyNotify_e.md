---
title: "swAssemblyNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAssemblyNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyNotify_e.html"
---

# swAssemblyNotify_e Enumeration

Assembly notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAssemblyNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAssemblyNotify_e
```

### C#

```csharp
public enum swAssemblyNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAssemblyNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAssemblyActiveAnnotationViewChangeNotify | 98 = ActiveAnnotationViewChangeNotify |
| swAssemblyActiveDisplayStateChangePostNotify | 71 = ActiveDisplayStateChangePostNotify |
| swAssemblyActiveDisplayStateChangePreNotify | 70 = ActiveDisplayStateChangePreNotify |
| swAssemblyActiveViewChangeNotify | 66 = ActiveViewChangeNotify |
| swAssemblyAddCustomPropertyNotify | 26 = AddCustomPropertyNotify |
| swAssemblyAddDvePagePreNotify | 60 = Not used. |
| swAssemblyAddItemNotify | 18 = AddItemNotify |
| swAssemblyAddMatePostNotify | 72 = Obsolete |
| swAssemblyAddMatePostNotify2 | 95 = AddMatePostNotify |
| swAssemblyAutoSaveNotify | 12 = AutoSaveNotify |
| swAssemblyAutoSaveToStorageNotify | 13 = AutoSaveToStorageNotify |
| swAssemblyAutoSaveToStorageStoreNotify | 82 = AutoSaveToStorageStoreNotify |
| swAssemblyBeginInContextEditNotify | 14 = BeginInContextEditNotify |
| swAssemblyBodyVisibleChangeNotify | 37 = BodyVisibleChangeNotify |
| swAssemblyChangeCustomPropertyNotify | 27 = ChangeCustomPropertyNotify |
| swAssemblyClearSelectionsNotify | 53 = ClearSelectionsNotify |
| swAssemblyCloseDesignTableNotify | 58 = CloseDesignTableNotify |
| swAssemblyCommandManagerTabActivatedPreNotify | 89 = CommandManagerTabActivatedPreNotify |
| swAssemblyComponentConfigurationChangeNotify | 73 = ComponentConfigurationChangeNotify |
| swAssemblyComponentDisplayModeChangePostNotify | 88 = ComponentDisplayModeChangePostNotify |
| swAssemblyComponentDisplayModeChangePreNotify | 87 = ComponentDisplayModeChangePreNotify |
| swAssemblyComponentDisplayStateChangeNotify | 47 = ComponentDisplayStateChangeNotify |
| swAssemblyComponentMoveNotify | 35 = Obsolete |
| swAssemblyComponentMoveNotify2 | 44 = ComponentMoveNotify2 |
| swAssemblyComponentReferredDisplayStateChangeNotify | 79 = ComponentReferredDisplayStateChangeNotify |
| swAssemblyComponentReorganizeNotify | 64 = ComponentReorganizeNotify |
| swAssemblyComponentStateChangeNotify | 22 = Obsolete |
| swAssemblyComponentStateChangeNotify2 | 25 = Obsolete |
| swAssemblyComponentStateChangeNotify3 | 96 = ComponentStateChangeNotify3 |
| swAssemblyComponentVisibleChangeNotify | 36 = ComponentVisibleChangeNotify |
| swAssemblyComponentVisualPropertiesChangeNotify | 46 = ComponentVisualPropertiesChangeNotify |
| swAssemblyConfigChangeNotify | 10 = ActiveConfigChangeNotify |
| swAssemblyConfigChangePostNotify | 11 = ActiveConfigChangePostNotify |
| swAssemblyConfigurationChangeNotify | 63 = ConfigurationChangeNotify |
| swAssemblyDeleteCustomPropertyNotify | 28 = DeleteCustomPropertyNotify |
| swAssemblyDeleteItemNotify | 20 = DeleteItemNotify |
| swAssemblyDeleteItemPreNotify | 52 = DeleteItemPreNotify |
| swAssemblyDeleteSelectionPreNotify | 33 = DeleteSelectionPreNotify |
| swAssemblyDestroyNotify | 2 = Obsolete |
| swAssemblyDestroyNotify2 | 62 = DestroyNotify2 |
| swAssemblyDimensionChangeNotify | 48 = DimensionChangeNotify |
| swAssemblyDisplayPaneCollapseNotify | 100 = DisplayPaneCollapseNotify |
| swAssemblyDisplayPaneExpandNotify | 99 = DisplayPaneExpandNotify |
| swAssemblyDragStateChangeNotify | 83 = DragStateChangeNotify |
| swAssemblyDynamicHighlightNotify | 45 = DynamicHighlightNotify |
| swAssemblyElectricalDataUpdateNotify | 43 = AssemblyElectricalDataUpdateNotify |
| swAssemblyEndInContextEditNotify | 15 = EndInContextEditNotify |
| swAssemblyEquationEditorPostNotify | 56 = EquationEditorPostNotify |
| swAssemblyEquationEditorPreNotify | 55 = EquationEditorPreNotify |
| swAssemblyFeatureEditPreNotify | 29 = FeatureEditPreNotify |
| swAssemblyFeatureManagerFilterStringChangeNotify | 67 = FeatureManagerFilterStringChangeNotify |
| swAssemblyFeatureManagerTabActivatedNotify | 93 = FeatureManagerTabActivatedNotify |
| swAssemblyFeatureManagerTabActivatedPreNotify | 92 = FeatureManagerTabActivatedPreNotify |
| swAssemblyFeatureManagerTreeRebuildNotify | 42 = FeatureManagerTreeRebuildNotify |
| swAssemblyFeatureSketchEditPreNotify | 30 = FeatureSketchEditPreNotify |
| swAssemblyFileDropNotify | 23 = FileDropNotify |
| swAssemblyFileDropPostNotify | 54 = FileDropPostNotify |
| swAssemblyFileDropPreNotify | 38 = FileDropPreNotify |
| swAssemblyFileReloadCancelNotify | 49 = FileReloadCancelNotify |
| swAssemblyFileReloadNotify | 24 = FleReloadNotify |
| swAssemblyFileReloadPreNotify | 34 = FileReloadPreNotify |
| swAssemblyFileSaveAsNotify | 7 = Obsolete |
| swAssemblyFileSaveAsNotify2 | 31 = FilesSaveAsNotify2 |
| swAssemblyFileSaveNotify | 6 = Obsolete |
| swAssemblyFileSavePostCancelNotify | 50 = FileSavePostCancelNotify |
| swAssemblyFileSavePostNotify | 39 = FileSavePostNotify |
| swAssemblyFlipLoopNotify | 68 = FlipLoopNotify |
| swAssemblyInsertTableNotify | 84 = InsertTableNotify |
| swAssemblyInterferenceNotify | 32 = InterferenceNotify |
| swAssemblyLargeDesignReviewStateChangeNotify | 101 = LargeDesignReviewStateChangeNotify |
| swAssemblyLightingDialogCreateNotify | 17 = LightingDialogCreateNotify |
| swAssemblyLoadFromStorageNotify | 8 = LoadFromStorageNotify |
| swAssemblyLoadFromStorageStoreNotify | 40 = LoadFromStorageStoreNotify |
| swAssemblyModifyNotify | 21 = ModifyNotify |
| swAssemblyModifyTableNotify | 85 = ModifyTableNotify |
| swAssemblyNewSelectionNotify | 5 = NewSelectionNotify |
| swAssemblyOpenDesignTableNotify | 57 = OpenDesignTableNotify |
| swAssemblyPreRenameItemNotify | 90 = PreRenameItemNotify |
| swAssemblyPromptBodiesToKeepNotify | 59 = PromptBodiesToKeepNotify |
| swAssemblyPublishTo3DPDFNotify | 96 = PublishTo3DPDFNotify |
| swAssemblyRedoPostNotify | 76 = RedoPostNotify |
| swAssemblyRedoPreNotify | 77 = RedoPreNotify |
| swAssemblyRegenNotify | 1 = RegenNotify |
| swAssemblyRegenPostNotify | 3 = RegenPostNotify |
| swAssemblyRegenPostNotify2 | 81 = RegenPostNotify2 |
| swAssemblyRenamedDocumentNotify | 91 = RenamedDocumentNotify |
| swAssemblyRenameDisplayTitleNotify | 97 = RenameDisplayTitleNotify |
| swAssemblyRenameItemNotify | 19 = RenameItemNotify |
| swAssemblySaveToStorageNotify | 9 = SaveToStorageNotify |
| swAssemblySaveToStorageStoreNotify | 41 = SaveToStorageStore |
| swAssemblySelectiveOpenPostNotify | 80 = SelectiveOpenPostNotify |
| swAssemblySensorAlertPreNotify | 69 = SensorAlertPreNotify |
| swAssemblySketchSolveNotify | 51 = SketchSolveNotify |
| swAssemblySuppressionStateChangeNotify | 65 = SuppressionStateChangeNotify |
| swAssemblyUndoPostNotify | 74 = UndoPostNotify |
| swAssemblyUndoPreNotify | 78 = UndoPreNotify |
| swAssemblyUnitsChangeNotify | 61 = UnitsChangeNotify |
| swAssemblyUserSelectionPostNotify | 86 = UserSelectionPostNotify |
| swAssemblyUserSelectionPreNotify | 75 = UserSelectionPreNotify |
| swAssemblyViewNewNotify | 4 = Obsolete |
| swAssemblyViewNewNotify2 | 16 = ViewNewNotify2 |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports assembly events (e.g., Assembly.h), include:

BEGIN_SINK_MAP(CSwAssembly)

SINK_ENTRY_EX(ID_ASSEMBLYDOC_EVENTS, DIID_DAssemblyDocEvents, swAssemblyDestroyNotify, DestroyNotify)

SINK_ENTRY_EX(ID_ASSEMBLYDOC_EVENTS, DIID_DAssemblyDocEvents, swAssemblyNewSelectionNotify, NewSelectionNotify)

END_SINK_MAP()

If developing a C++ application, use the enumerators to[register for notifications](sldworksapiprogguide.chm::/overview/events.htm)for the[IAssemblyDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc.html)events (see the**Members**list in this topic).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)

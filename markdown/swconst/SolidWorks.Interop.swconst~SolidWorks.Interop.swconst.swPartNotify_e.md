---
title: "swPartNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPartNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartNotify_e.html"
---

# swPartNotify_e Enumeration

Part notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPartNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPartNotify_e
```

### C#

```csharp
public enum swPartNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPartNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPartActiveAnnotationViewChangeNotify | 80 = ActiveAnnotationViewChangeNotify |
| swPartActiveDisplayStateChangePostNotify | 61 = ActiveDisplayStateChangePostNotify |
| swPartActiveDisplayStateChangePreNotify | 60 = ActiveDisplayStateChangePreNotify |
| swPartActiveViewChangeNotify | 53 = ActiveViewChangeNotify |
| swPartAddCustomPropertyNotify | 21 = AddCustomPropertyNotify |
| swPartAddDvePagePreNotify | Not used |
| swPartAddItemNotify | 16 = AddItemNotify |
| swPartAutoSaveNotify | 12 = AutoSaveNotify |
| swPartAutoSaveToStorageNotify | 13 = AutoSaveToStorageNotify |
| swPartAutoSaveToStorageStoreNotify | 66 = AutoSaveToStorageStoreNotify |
| swPartBodyVisibleChangeNotify | 29 = BodyVisibleChangeNotify |
| swPartChangeCustomPropertyNotify | 22 = ChangeCustomPropertyNotify |
| swPartClearSelectionsNotify | 42 = ClearSelectionsNotify |
| swPartCloseDesignTableNotify | 46 = CloseDesignTableNotify |
| swPartCommandManagerTabActivatedPreNotify | 71 = CommandManagerTabActivatedPreNotify |
| swPartConfigChangeNotify | 10 = ActiveConfigChangeNotify |
| swPartConfigChangePostNotify | 11 = ActiveConfigChangePostNotify |
| swPartConfigurationChangeNotify | 51 = ConfigurationChangeNotify |
| swPartConvertToBodiesPostNotify | 78 = ConvertToBodiesPostNotify |
| swPartConvertToBodiesPreNotify | 77 = ConvertToBodiesPreNotify |
| swPartDeleteCustomPropertyNotify | 23 = DeleteCustomPropertyNotify |
| swPartDeleteItemNotify | 18 = DeleteItemNotify |
| swPartDeleteItemPreNotify | 41 = DeleteItemPreNotify |
| swPartDeleteSelectionPreNotify | 27 = DeleteSelectionPreNotify |
| swPartDestroyNotify | Obsolete |
| swPartDestroyNotify2 | 50 = DestroyNotify2 |
| swPartDimensionChangeNotify | 37 = DimensionChangeNotify |
| swPartDisplayPaneCollapseNotify | 82 = DisplayPaneCollapseNotify |
| swPartDisplayPaneExpandNotify | 81 = DisplayPaneExpandNotify |
| swPartDragStateChangeNotify | 67 = DragStateChangeNotify |
| swPartDynamicHighlightNotify | 36 = DynamicHighlightNotify |
| swPartEquationEditorPostNotify | 44 = EquationEditorPostNotify |
| swPartEquationEditorPreNotify | 43 = EquationEditorPreNotify |
| swPartFeatureEditPreNotify | 24 = FeatureEditPreNotify |
| swPartFeatureManagerFilterStringChangeNotify | 54 = FeatureManagerFilterStringChangeNotify |
| swPartFeatureManagerTabActivatedNotify | 75 = FeatureManagerTabActivatedNotify |
| swPartFeatureManagerTabActivatedPreNotify | 74 = FeatureManagerTabActivatedPreNotify |
| swPartFeatureManagerTreeRebuildNotify | 34 = FeatureManagerTreeRebuildNotify |
| swPartFeatureSketchEditPreNotify | 25 = FeatureSketchEditPreNotify |
| swPartFileDropPostNotify | 35 = FileDropPostNotify |
| swPartFileDropPreNotify | 56 = FileDropPreNotify |
| swPartFileReloadCancelNotify | 38 = FileReloadCancelNotify |
| swPartFileReloadNotify | 20 = FileReloadNotify |
| swPartFileReloadPreNotify | 28 = FileReloadPreNotify |
| swPartFileSaveAsNotify | Obsolete |
| swPartFileSaveAsNotify2 | 26 = FileSaveAsNotify2 |
| swPartFileSaveNotify | 6 = FileSaveNotify |
| swPartFileSavePostCancelNotify | 39 = FileSavePostCancelNotify |
| swPartFileSavePostNotify | 31 = FileSavePostNotify |
| swPartFlipLoopNotify | 55 = FlipLoopNotify |
| swPartInsertTableNotify | 68 = InsertTableNotify |
| swPartLightingDialogCreateNotify | 15 = LightingDialogCreateNotify |
| swPartLoadFromStorageNotify | 8 = LoadFromStorageNotify |
| swPartLoadFromStorageStoreNotify | 32 = LoadFromStorageStoreNotify |
| swPartModifyNotify | 19 = ModifyNotify |
| swPartModifyTableNotify | 69 = ModifyTableNotify |
| swPartNewSelectionNotify | 5 = NewSelectionNotify |
| swPartOpenDesignTableNotify | 45 = OpenDesignTableNotify |
| swPartPreRenameItemNotify | 72 = PreRenameItemNotify |
| swPartPromptBodiesToKeepNotify | 47 = PromptBodiesToKeepNotify |
| swPartPublishTo3DPDFNotify | 78 = PublishTo3DPDFNotify |
| swPartRedoPostNotify | 62 = RedoPostNotify |
| swPartRedoPreNotify | 63 = RedoPreNotify |
| swPartRegenNotify | 1 = RegenNotify |
| swPartRegenPostNotify | Obsolete |
| swPartRegenPostNotify2 | 30 = RegenPostNotify2 |
| swPartRenamedDocumentNotify | 73 = RenamedDocumentNotify |
| swPartRenameDisplayTitleNotify | 79 = RenameDisplayTitleNotify |
| swPartRenameItemNotify | 17 = RenameItemNotify |
| swPartSaveToStorageNotify | 9 = SaveToStorageNotify |
| swPartSaveToStorageStoreNotify | 33 = SaveToStorageStoreNotify |
| swPartSensorAlertPreNotify | 57 = SensorAlertPreNotify |
| swPartSketchSolveNotify | 40 = SketchSolveNotify |
| swPartSuppressionStateChangeNotify | 52 = SuppressionStateChangeNotify |
| swPartUndoPostNotify | 58 = UndoPostNotify |
| swPartUndoPreNotify | 64 = UndoPreNotify |
| swPartUnitsChangeNotify | 49 = UnitsChangeNotify |
| swPartUserSelectionPostNotify | 70 = UserSelectionPostNotify |
| swPartUserSelectionPreNotify | 59 = UserSelectionPreNotify |
| swPartViewNewNotify | Obsolete |
| swPartViewNewNotify2 | 14 = ViewNewNotify2 |
| swPartWeldmentCutListUpdatePostNotify | 65 = WeldmentCutListUpdatePostNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object. For example:

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports part events (e.g., PartDoc.h), include:

BEGIN_SINK_MAP(CSwPart)

SINK_ENTRY_EX(ID_PARTDOC_EVENTS, DIID_DPartDocEvents, swPartDestroyNotify, DestroyNotify)

SINK_ENTRY_EX(ID_PARTDOC_EVENTS, DIID_DPartDocEvents, swPartNewSelectionNotify, NewSelectionNotify)

END_SINK_MAP()

If developing a C++ application, use these enumerators to[register for notifications](sldworksapiprogguide.chm::/overview/events.htm)for[IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html)events.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)

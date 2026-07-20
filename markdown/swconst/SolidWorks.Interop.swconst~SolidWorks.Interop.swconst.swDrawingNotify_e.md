---
title: "swDrawingNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDrawingNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDrawingNotify_e.html"
---

# swDrawingNotify_e Enumeration

Drawing notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDrawingNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDrawingNotify_e
```

### C#

```csharp
public enum swDrawingNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDrawingNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDrawingActivateSheetPostNotify | 53 = ActivateSheetPostNotify |
| swDrawingActivateSheetPreNotify | 52 = ActivateSheetPreNotify |
| swDrawingAddCustomPropertyNotify | 20 = AddCustomPropertyNotify |
| swDrawingAddDvePagePreNotify | 40 = Not used. |
| swDrawingAddItemNotify | 15 = AddItemNotify |
| swDrawingAutoSaveNotify | 10 = AutoSaveNotify |
| swDrawingAutoSaveToStorageNotify | 11 = AutoSaveToStorageNotify |
| swDrawingAutoSaveToStorageStoreNotify | 48 = AutoSaveToStorageStoreNotify |
| swDrawingChangeCustomPropertyNotify | 21 = ChangeCustomPropertyNotify |
| swDrawingClearSelectionsNotify | 37 = ClearSelectionsNotify |
| swDrawingCommandManagerTabActivatedPreNotify | 54 = CommandManagerTabActivatedPreNotify |
| swDrawingConfigChangeNotify | 12 = ActiveConfigChangeNotify |
| swDrawingConfigChangePostNotify | 13 = ActiveConfigChangePostNotify |
| swDrawingDeleteCustomPropertyNotify | 22 = DeleteCustomPropertyNotify |
| swDrawingDeleteItemNotify | 17 = DeleteItemNotify |
| swDrawingDeleteItemPreNotify | 36 = DeleteItemPreNotify |
| swDrawingDeleteSelectionPreNotify | 24 = DeleteSelectonPreNotify |
| swDrawingDestroyNotify | 2 = Obsolete |
| swDrawingDestroyNotify2 | 42 = DestroyNotify2 |
| swDrawingDimensionChangeNotify | 32 = DimensionChangeNotify |
| swDrawingDisplayPaneCollapseNotify | 59 = DisplayPaneCollapseNotify |
| swDrawingDisplayPaneExpandNotify | 58 = DisplayPaneExpandNotify |
| swDrawingDynamicHighlightNotify | 31 = DynamicHighlightNotify |
| swDrawingEquationEditorPostNotify | 39 = EquationEditorPostNotify |
| swDrawingEquationEditorPreNotify | 38 = EquationEditorPreNotify |
| swDrawingFeatureManagerTabActivatedNotify | 56 = FeatureManagerTabActivatedNotify |
| swDrawingFeatureManagerTabActivatedPreNotify | 55 = FeatureManagerTabActivatedPreNotify |
| swDrawingFeatureManagerTreeRebuildNotify | 29 = FeatureManagerTreeRebuildNotify |
| swDrawingFileReloadCancelNotify | 33 = Not used. |
| swDrawingFileReloadNotify | 19 = Not used. |
| swDrawingFileReloadPreNotify | 25 = Not used. |
| swDrawingFileSaveAsNotify | 7 = Obsolete |
| swDrawingFileSaveAsNotify2 | 23 = FileSaveAsNotify2 |
| swDrawingFileSaveNotify | 6 = FileSaveNotify |
| swDrawingFileSavePostCancelNotify | 34 = FileSavePostCancelNotify |
| swDrawingFileSavePostNotify | 26 = FileSavePostNotify |
| swDrawingInsertTableNotify | 49 = InsertTableNotify |
| swDrawingLoadFromStorageNotify | 8 = LoadFromStorageNotify |
| swDrawingLoadFromStorageStoreNotify | 27 = LoadFromStorageStoreNotify |
| swDrawingModifyNotify | 18 = ModifyNotify |
| swDrawingModifyTableNotify | 50 = ModifyTableNotify |
| swDrawingNewSelectionNotify | 5 = NewSelectionNotify |
| swDrawingRedoPostNotify | 45 = RedoPostNotify |
| swDrawingRedoPreNotify | 46 = RedoPreNotify |
| swDrawingRegenNotify | 1 = RegenNotify |
| swDrawingRegenPostNotify | 3 = RegenPostNotify |
| swDrawingRenameDisplayTitleNotify | 57 = RenameDisplayTitleNotify |
| swDrawingRenameItemNotify | 16 = RenameItemNotify |
| swDrawingSaveToStorageNotify | 9 = SaveToStorageNotify |
| swDrawingSaveToStorageStoreNotify | 28 = SaveToStorageStoreNotify |
| swDrawingSketchSolveNotify | 35 = SketchSolveNotify |
| swDrawingStateChangeNotify | 60 = DrawingStateChangeNotify |
| swDrawingUndoPostNotify | 43 = UndoPostNotify |
| swDrawingUndoPreNotify | 47 = UndoPreNotify |
| swDrawingUnitsChangeNotify | 41 = UnitsChangeNotify |
| swDrawingUserSelectionPostNotify | 51 = UserSelectionPostNotify |
| swDrawingUserSelectionPreNotify | 44 = UserSelectionPreNotify |
| swDrawingViewCreatePreNotify | 30 = ViewCreatePreNotify |
| swDrawingViewNewNotify | 4 = Obsolete |
| swDrawingViewNewNotify2 | 14 = ViewNewNotify2 |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports drawing events (e.g., Drawing.h), include:

BEGIN_SINK_MAP(CSwDrawing)

SINK_ENTRY_EX(ID_DRAWINGDOC_EVENTS, DIID_DDrawingDocEvents, swDrawingDestroyNotify, DestroyNotify)

SINK_ENTRY_EX(ID_DRAWINGDOC_EVENTS, DIID_DDrawingDocEvents, swDrawingNewSelectionNotify, NewSelectionNotify)

END_SINK_MAP()

If developing a C++ application, use the enumerators to[register for notifications](sldworksapiprogguide.chm::/overview/events.htm)for[IDrawingDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html)events.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)

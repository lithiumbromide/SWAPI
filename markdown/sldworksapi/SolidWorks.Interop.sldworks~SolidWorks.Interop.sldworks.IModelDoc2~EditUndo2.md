---
title: "EditUndo2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditUndo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUndo2.html"
---

# EditUndo2 Method (IModelDoc2)

Undoes the specified number of actions in the active SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditUndo2( _
   ByVal Steps As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Steps As System.Integer

instance.EditUndo2(Steps)
```

### C#

```csharp
void EditUndo2(
   System.int Steps
)
```

### C++/CLI

```cpp
void EditUndo2(
   System.int Steps
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Steps`: Number of actions to undo

## VBA Syntax

See [ModelDoc2::EditUndo2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditUndo2.html).

## Examples

[Undo Feature and Fire Undo Post-Notify Event (VBA)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)
[Undo Feature and Fire Undo Post-Notify Event (VB.NET)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)
[Undo Feature and Fire Undo Post-Notify Event (C#)](Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ClearUndoList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearUndoList.html)
[IModelDoc2::EditRedo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRedo2.html)
[IModelDoc2::SketchUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchUndo.html)
[IModelDocExtension::FinishRecordingUndoObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject.html)
[IModelDocExtension::StartRecordingUndoObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~StartRecordingUndoObject.html)
[IModelDoc2::SketchUndo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchUndo.html)
[DAssemblyDocEvents_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UndoPostNotifyEventHandler.html)
[DDrawingDocEvents_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UndoPostNotifyEventHandler.html)
[DPartDocEvents_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UndoPostNotifyEventHandler.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

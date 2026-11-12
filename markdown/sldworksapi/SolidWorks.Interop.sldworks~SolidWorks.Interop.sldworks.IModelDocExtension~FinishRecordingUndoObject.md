---
title: "FinishRecordingUndoObject Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "FinishRecordingUndoObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject.html"
---

# FinishRecordingUndoObject Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::FinishRecordingUndoObject2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FinishRecordingUndoObject( _
   ByVal UndoObjectName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UndoObjectName As System.String
Dim value As System.Boolean

value = instance.FinishRecordingUndoObject(UndoObjectName)
```

### C#

```csharp
System.bool FinishRecordingUndoObject(
   System.string UndoObjectName
)
```

### C++/CLI

```cpp
System.bool FinishRecordingUndoObject(
   System.String^ UndoObjectName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UndoObjectName`: String to appear in SOLIDWORKS Undo list

### Return Value

True if recording of the SOLIDWORKS Undo object ends, false if not

## VBA Syntax

See [ModelDocExtension::FinishRecordingUndoObject](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~FinishRecordingUndoObject.html).

## Remarks

Place [IModelDocExtension::StartRecordingUndoObject](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~StartRecordingUndoObject.html) at the beginning and this method at the end of any SOLIDWORKS API calls in your application that you want your user to undo as a group.

For example, if your application creates a complex gear that requires many SOLIDWORKS API calls, place IModelDocExtension::StartRecordingUndoObject and this method around the SOLIDWORKS API calls that create that gear. Then your user need only select the string specified for UndoObjectName in the SOLIDWORKS Undo list to undo all of the SOLIDWORKS API calls that created the gear.

NOTE: Only SOLIDWORKS operations that support Undo will be undone. Both SOLIDWORKS API and non-API operations are undone.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::ClearUndoList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearUndoList.html)
[IModelDoc2::EditUndo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUndo2.html)
[IModelDoc2::EditRedo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRedo2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

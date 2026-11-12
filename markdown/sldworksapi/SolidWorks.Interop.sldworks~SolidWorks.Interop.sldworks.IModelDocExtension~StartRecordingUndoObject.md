---
title: "StartRecordingUndoObject Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "StartRecordingUndoObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~StartRecordingUndoObject.html"
---

# StartRecordingUndoObject Method (IModelDocExtension)

Starts recording the SOLIDWORKS Undo object.

## Syntax

### Visual Basic (Declaration)

```vb
Sub StartRecordingUndoObject()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension

instance.StartRecordingUndoObject()
```

### C#

```csharp
void StartRecordingUndoObject()
```

### C++/CLI

```cpp
void StartRecordingUndoObject();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDocExtension::StartRecordingUndoObject](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~StartRecordingUndoObject.html).

## Examples

[Create Hidden Undo Object (VBA)](Create_Multiple_Undo_Command_Example_VB.htm)
[Create Hidden Undo Object (VB.NET)](Create_Multiple_Undo_Command_Example_VBNET.htm)
[Create Hidden Undo Object (C#)](Create_Multiple_Undo_Command_Example_CSharp.htm)

## Remarks

To add an object with the name UndoObjectName to the SOLIDWORKS Undo list, place the SOLIDWORKS API calls between IModelDocExtension::StartRecordingUndoObject and [IModelDocExtension::FinishRecordingUndoObject2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~FinishRecordingUndoObject2.html):

For example, assume that your application creates a complex gear that requires many SOLIDWORKS API calls and you would like your SOLIDWORKS Design user to be able to undo that gear from the user interface at a later time. Your application can create an Undo object by calling:

1. IModelDocExtension::StartRecordingUndoObject
2. SOLIDWORKS API calls that create the gear
3. IModelDocExtension::FinishRecordingUndoObject2 with MakeHidden = False

Now assume that your application performs many temporary operations that you do not want your users to see in the SOLIDWORKS Undo list, because they are not essential to the modeling and design process. For this case, your application can place the non-essential SOLIDWORKS API calls between IModelDocExtension::StartRecordingUndoObject and IModelDocExtension::FinishRecordingUndoObject2 with MakeHidden = True. The Undo object is still added to the SOLIDWORKS Undo list, but the user does not see it in the list.

****WARNING**:** If your application hides an Undo object in the Undo list by setting MakeHidden = True and the Undo object is the first item in the SOLIDWORKS Undo list, then SOLIDWORKS discards the Undo object from the Undo list. If this happens, the SOLIDWORKS API calls in this Undo object cannot be undone.

Similarly, if the last item to be redone is a hidden API Undo object, then SOLIDWORKS discards it, and the SOLIDWORKS API calls cannot be redone.

Only SOLIDWORKS operations that support Undo are undone. Both SOLIDWORKS API and non-API operations are undone.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::ClearUndoList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearUndoList.html)
[IModelDoc2::EditRedo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRedo2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

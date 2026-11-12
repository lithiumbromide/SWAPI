---
title: "SetApiUndoObject Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetApiUndoObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetApiUndoObject.html"
---

# SetApiUndoObject Method (IModelDocExtension)

Implements an undo object for an add-in application.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetApiUndoObject( _
   ByVal PHandler As System.Object, _
   ByVal DisplayName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PHandler As System.Object
Dim DisplayName As System.String
Dim value As System.Boolean

value = instance.SetApiUndoObject(PHandler, DisplayName)
```

### C#

```csharp
System.bool SetApiUndoObject(
   System.object PHandler,
   System.string DisplayName
)
```

### C++/CLI

```cpp
System.bool SetApiUndoObject(
   System.Object^ PHandler,
   System.String^ DisplayName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PHandler`: [Undo object](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwUndoAPIHandler.html)
- `DisplayName`: Name to display in the SOLIDWORKS undo list

### Return Value

True if the undo object is implemented, false if not

## VBA Syntax

See [ModelDocExtension::SetApiUndoObject](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~SetApiUndoObject.html).

## Examples

[Automate Add-in's Undo Commands (VBA)](Automate_Add-in_s_Undo_Commands_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

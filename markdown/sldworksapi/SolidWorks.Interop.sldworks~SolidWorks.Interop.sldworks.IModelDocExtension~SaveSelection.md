---
title: "SaveSelection Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SaveSelection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveSelection.html"
---

# SaveSelection Method (IModelDocExtension)

Creates a new selection set containing the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveSelection( _
   ByRef Status As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Status As System.Integer
Dim value As System.Object

value = instance.SaveSelection(Status)
```

### C#

```csharp
System.object SaveSelection(
   out System.int Status
)
```

### C++/CLI

```cpp
System.Object^ SaveSelection(
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Status`: 1 if a selection set is created, 0 if not

### Return Value

[Selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html)

## VBA Syntax

See [ModelDocExtension::SaveSelection](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SaveSelection.html).

## Examples

[Create and Delete Selection Sets (C#)](Create_and_Delete_Selection_Sets_Example_CSharp.htm)
[Create and Delete Selection Sets (VB.NET)](Create_and_Delete_Selection_Sets_Example_VBNET.htm)
[Create and Delete Selection Sets (VBA)](Create_and_Delete_Selection_Sets_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[ISelectionSetFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.html)
[ISelectionSetItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem.html)
[ISelectionSet::RemoveSelectionSet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~RemoveSelectionSet.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

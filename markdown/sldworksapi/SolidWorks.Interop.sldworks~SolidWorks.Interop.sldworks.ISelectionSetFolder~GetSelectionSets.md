---
title: "GetSelectionSets Method (ISelectionSetFolder)"
project: "SOLIDWORKS API Help"
interface: "ISelectionSetFolder"
member: "GetSelectionSets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder~GetSelectionSets.html"
---

# GetSelectionSets Method (ISelectionSetFolder)

Gets the selection sets in the Selection Sets folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionSets() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionSetFolder
Dim value As System.Object

value = instance.GetSelectionSets()
```

### C#

```csharp
System.object GetSelectionSets()
```

### C++/CLI

```cpp
System.Object^ GetSelectionSets();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [selection sets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html)

## VBA Syntax

See [SelectionSetFolder::GetSelectionSets](ms-its:sldworksapivb6.chm::/sldworks~SelectionSetFolder~GetSelectionSets.html).

## Examples

[Create and Delete Selection Sets (C#)](Create_and_Delete_Selection_Sets_Example_CSharp.htm)
[Create and Delete Selection Sets (VB.NET)](Create_and_Delete_Selection_Sets_Example_VBNET.htm)
[Create and Delete Selection Sets (VBA)](Create_and_Delete_Selection_Sets_Example_VB.htm)
[Get Dispatch Objects for Selection Set Items (C#)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_CSharp.htm)
[Get Dispatch Objects for Selection Set Items (VB.NET)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VBNET.htm)
[Get Dispatch Objects for Selection Set Items (VBA)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VB.htm)

## See Also

[ISelectionSetFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.html)
[ISelectionSetFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder_members.html)
[ISelectionSetFolder::GetSelectionSetByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder~GetSelectionSetByName.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

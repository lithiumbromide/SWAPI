---
title: "GetSelectionSetByName Method (ISelectionSetFolder)"
project: "SOLIDWORKS API Help"
interface: "ISelectionSetFolder"
member: "GetSelectionSetByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder~GetSelectionSetByName.html"
---

# GetSelectionSetByName Method (ISelectionSetFolder)

Gets the specified selection set.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionSetByName( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionSetFolder
Dim Name As System.String
Dim value As System.Object

value = instance.GetSelectionSetByName(Name)
```

### C#

```csharp
System.object GetSelectionSetByName(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ GetSelectionSetByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the selection set

### Return Value

[Selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html)

## VBA Syntax

See [SelectionSetFolder::GetSelectionSetByName](ms-its:sldworksapivb6.chm::/sldworks~SelectionSetFolder~GetSelectionSetByName.html).

## Examples

[Get Objects in Selection Set (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)
[Get Objects in Selection Set (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)
[Get Objects in Selection Set (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

## Remarks

To get the name of a selection folder to pass to this method, you can traverse [items in the FeatureManager design tree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html). See the examples.

## See Also

[ISelectionSetFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.html)
[ISelectionSetFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder_members.html)
[ISelectionSetFolder::GetSelectionSets Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder~GetSelectionSets.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

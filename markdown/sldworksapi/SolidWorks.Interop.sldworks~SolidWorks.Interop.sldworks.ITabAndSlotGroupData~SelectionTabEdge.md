---
title: "SelectionTabEdge Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "SelectionTabEdge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionTabEdge.html"
---

# SelectionTabEdge Property (ITabAndSlotGroupData)

Gets or sets the tab edge of this Tab and Slot group.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionTabEdge As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Object

instance.SelectionTabEdge = value

value = instance.SelectionTabEdge
```

### C#

```csharp
System.object SelectionTabEdge {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectionTabEdge {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

## VBA Syntax

See [TabAndSlotGroupData::SelectionTabEdge](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~SelectionTabEdge.html).

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)
[ITabAndSlotGroupData::TabFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabFace.html)
[ITabAndSlotGroupData::TabThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabThickness.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

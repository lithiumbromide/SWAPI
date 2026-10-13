---
title: "SelectionEndReferencePoint Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "SelectionEndReferencePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionEndReferencePoint.html"
---

# SelectionEndReferencePoint Property (ITabAndSlotGroupData)

Gets or sets the end location of this Tab and Slot group.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionEndReferencePoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Object

instance.SelectionEndReferencePoint = value

value = instance.SelectionEndReferencePoint
```

### C#

```csharp
System.object SelectionEndReferencePoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectionEndReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [TabAndSlotGroupData::SelectionEndReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~SelectionEndReferencePoint.html).

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)
[ITabAndSlotGroupData::SelectionStartReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionStartReferencePoint.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

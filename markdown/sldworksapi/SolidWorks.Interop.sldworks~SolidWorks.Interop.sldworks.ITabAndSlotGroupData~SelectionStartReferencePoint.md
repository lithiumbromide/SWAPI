---
title: "SelectionStartReferencePoint Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "SelectionStartReferencePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionStartReferencePoint.html"
---

# SelectionStartReferencePoint Property (ITabAndSlotGroupData)

Gets or sets the start location of this Tab and Slot group.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionStartReferencePoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Object

instance.SelectionStartReferencePoint = value

value = instance.SelectionStartReferencePoint
```

### C#

```csharp
System.object SelectionStartReferencePoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectionStartReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [TabAndSlotGroupData::SelectionStartReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~SelectionStartReferencePoint.html).

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)
[ITabAndSlotGroupData::SelectionEndReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionEndReferencePoint.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

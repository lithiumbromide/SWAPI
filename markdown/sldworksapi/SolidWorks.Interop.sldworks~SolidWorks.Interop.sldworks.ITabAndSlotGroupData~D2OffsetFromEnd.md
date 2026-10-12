---
title: "D2OffsetFromEnd Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "D2OffsetFromEnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D2OffsetFromEnd.html"
---

# D2OffsetFromEnd Property (ITabAndSlotGroupData)

Gets or sets the ending offset of the tabs/slots in this group.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2OffsetFromEnd As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.D2OffsetFromEnd = value

value = instance.D2OffsetFromEnd
```

### C#

```csharp
System.double D2OffsetFromEnd {get; set;}
```

### C++/CLI

```cpp
property System.double D2OffsetFromEnd {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance from the edge where to end the tabs and slots

## VBA Syntax

See [TabAndSlotGroupData::D2OffsetFromEnd](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~D2OffsetFromEnd.html).

## Remarks

This method is valid only if [ITabAndSlotGroupData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~Offset.html) is set to true.

If you want the tabs/slots to span the entire edge of the model, set both this property and [ITabAndSlotGroupData::D2OffsetFromStart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D1OffsetFromStart.html) to zero.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

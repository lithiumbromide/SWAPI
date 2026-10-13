---
title: "SpacingType Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "SpacingType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingType.html"
---

# SpacingType Property (ITabAndSlotGroupData)

Gets or sets the type of spacing of tabs/slots in this group.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpacingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Integer

instance.SpacingType = value

value = instance.SpacingType
```

### C#

```csharp
System.int SpacingType {get; set;}
```

### C++/CLI

```cpp
property System.int SpacingType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Spacing type as defined in [swTabSlotFeatureSpacingType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureSpacingType_e.html)

## VBA Syntax

See [TabAndSlotGroupData::SpacingType](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~SpacingType.html).

## Examples

See the [ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.html) example.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

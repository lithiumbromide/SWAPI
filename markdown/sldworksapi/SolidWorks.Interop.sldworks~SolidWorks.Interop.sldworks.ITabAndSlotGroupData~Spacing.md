---
title: "Spacing Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~Spacing.html"
---

# Spacing Property (ITabAndSlotGroupData)

Gets or sets the spacing between tabs/slots.

## Syntax

### Visual Basic (Declaration)

```vb
Property Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Double

instance.Spacing = value

value = instance.Spacing
```

### C#

```csharp
System.double Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Spacing between tabs

## VBA Syntax

See [TabAndSlotGroupData::Spacing](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~Spacing.html).

## Remarks

This property is valid only if [ITabAndSlotGroupData::SpacingType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingType.html) is set to [swTabSlotFeatureSpacingType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureSpacingType_e.html).SpacingLength.

The value of this property drives the number of instances.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

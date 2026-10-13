---
title: "SpacingNumberOfInstances Property (ITabAndSlotGroupData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotGroupData"
member: "SpacingNumberOfInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingNumberOfInstances.html"
---

# SpacingNumberOfInstances Property (ITabAndSlotGroupData)

Gets or sets the number of instances of equally spaced tabs/slots in this group.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpacingNumberOfInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotGroupData
Dim value As System.Integer

instance.SpacingNumberOfInstances = value

value = instance.SpacingNumberOfInstances
```

### C#

```csharp
System.int SpacingNumberOfInstances {get; set;}
```

### C++/CLI

```cpp
property System.int SpacingNumberOfInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of instances

## VBA Syntax

See [TabAndSlotGroupData::SpacingNumberOfInstances](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotGroupData~SpacingNumberOfInstances.html).

## Examples

See the [ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.html) example.

## Remarks

This property is valid only if [ITabAndSlotGroupData::SpacingType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingType.html) is set to [swTabSlotFeatureSpacingType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureSpacingType_e.html).EqualSpacing.

## See Also

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.html)
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

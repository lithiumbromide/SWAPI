---
title: "Distance Property (ISlotMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISlotMateFeatureData"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Distance.html"
---

# Distance Property (ISlotMateFeatureData)

Gets or sets the distance from the end of the slot where to place the component axis in this slot mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISlotMateFeatureData
Dim value As System.Double

instance.Distance = value

value = instance.Distance
```

### C#

```csharp
System.double Distance {get; set;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance from the end of the slot

## VBA Syntax

See [SlotMateFeatureData::Distance](ms-its:sldworksapivb6.chm::/sldworks~SlotMateFeatureData~Distance.html).

## Remarks

This property is valid only if [ISlotMateFeatureData::Constraint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Constraint.html) is set to [swSlotMateConstraintOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlotMateConstraintOptions_e.html).swSlotMateConstraintOption_Distance.

To change the endpoint from which the distance is measured, set [ISlotMateFeatureData::FlipDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~FlipDirection.html) to true.

## See Also

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html)
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

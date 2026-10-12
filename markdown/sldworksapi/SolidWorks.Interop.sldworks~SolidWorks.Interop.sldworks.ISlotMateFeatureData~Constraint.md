---
title: "Constraint Property (ISlotMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISlotMateFeatureData"
member: "Constraint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Constraint.html"
---

# Constraint Property (ISlotMateFeatureData)

Gets or sets how to constrain the component in the slot of this slot mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property Constraint As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISlotMateFeatureData
Dim value As System.Integer

instance.Constraint = value

value = instance.Constraint
```

### C#

```csharp
System.int Constraint {get; set;}
```

### C++/CLI

```cpp
property System.int Constraint {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Constraint option as defined in [swSlotMateConstraintOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlotMateConstraintOptions_e.html)

## VBA Syntax

See [SlotMateFeatureData::Constraint](ms-its:sldworksapivb6.chm::/sldworks~SlotMateFeatureData~Constraint.html).

## Examples

See the [ISlotMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html) example.

## Remarks

If this property is set to swSlotMateConstraintOptions_e:

- swSlotMateConstraintOption_Distance, specify the [ISlotMateFeatureData::Distance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Distance.html) from the end of the slot where to place the component axis.
- swSlotMateConstraintOption_Percent, specify the distance as a [ISlotMateFeatureData::Percent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Percent.html) of the slot length where to place the component axis.

If this is a slot-to-slot mate, the only valid constraints are:

- swSlotMateConstraintOptions_e.swSlotMateConstraintOption_Free
- swSlotMateConstraintOptions_e.swSlotMateConstraintOption_Centered

To change the endpoint from which the distance is measured, set [ISlotMateFeatureData::FlipDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~FlipDirection.html) to true.

## See Also

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html)
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

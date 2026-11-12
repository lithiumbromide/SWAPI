---
title: "WallStiffnessUnit Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "WallStiffnessUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallStiffnessUnit.html"
---

# WallStiffnessUnit Property (ICWContactSet)

Gets or sets the wall stiffness units of this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property WallStiffnessUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.WallStiffnessUnit = value

value = instance.WallStiffnessUnit
```

### C#

```csharp
System.int WallStiffnessUnit {get; set;}
```

### C++/CLI

```cpp
property System.int WallStiffnessUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWContactSet::WallStiffnessUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~WallStiffnessUnit.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall and [ICWContactSet::WallType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallType.html) is set to [swsWallType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWallType_e.html).swsWallTypeFlexible.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::AxialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~AxialStiffnessValue.html)
[ICWContactSet::WallFriction Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallFriction.html)
[ICWContactSet::WallType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallType.html)
[ICWContactSet::TangentialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TangentialStiffnessValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

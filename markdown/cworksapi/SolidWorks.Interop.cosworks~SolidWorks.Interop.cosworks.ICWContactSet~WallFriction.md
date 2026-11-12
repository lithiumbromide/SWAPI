---
title: "WallFriction Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "WallFriction"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallFriction.html"
---

# WallFriction Property (ICWContactSet)

Gets or sets the coefficient of friction for this contact set with a rigid virtual wall.

## Syntax

### Visual Basic (Declaration)

```vb
Property WallFriction As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Double

instance.WallFriction = value

value = instance.WallFriction
```

### C#

```csharp
System.double WallFriction {get; set;}
```

### C++/CLI

```cpp
property System.double WallFriction {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= Coefficient of friction for rigid wall types <= 1.0

## VBA Syntax

See [CWContactSet::WallFriction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~WallFriction.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall, and [ICWContactSet::WallType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallType.html) is set to [swsWallType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWallType_e.html).swsWallTypeRigid.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::WallStiffnessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallStiffnessUnit.html)
[ICWContactSet::AxialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~AxialStiffnessValue.html)
[ICWContactSet::TangentialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TangentialStiffnessValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

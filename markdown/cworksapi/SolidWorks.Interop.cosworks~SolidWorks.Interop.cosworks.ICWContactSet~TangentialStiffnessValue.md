---
title: "TangentialStiffnessValue Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "TangentialStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TangentialStiffnessValue.html"
---

# TangentialStiffnessValue Property (ICWContactSet)

Gets or sets the wall shear stiffness value for this flexible virtual wall contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentialStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Double

instance.TangentialStiffnessValue = value

value = instance.TangentialStiffnessValue
```

### C#

```csharp
System.double TangentialStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double TangentialStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Wall shear stiffness value

## VBA Syntax

See [CWContactSet::TangentialStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~TangentialStiffnessValue.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall and [ICWContactSet::WallType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallType.html) is set to [swsWallType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWallType_e.html).swsWallTypeFlexible.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::WallStiffnessUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallStiffnessUnit.html)
[ICWContactSet::AxialStiffnessValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~AxialStiffnessValue.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

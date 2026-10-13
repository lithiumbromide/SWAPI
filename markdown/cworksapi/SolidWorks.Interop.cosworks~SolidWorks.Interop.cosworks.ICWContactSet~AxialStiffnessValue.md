---
title: "AxialStiffnessValue Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "AxialStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~AxialStiffnessValue.html"
---

# AxialStiffnessValue Property (ICWContactSet)

Gets or sets the wall axial stiffness value for this flexible virtual wall contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property AxialStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Double

instance.AxialStiffnessValue = value

value = instance.AxialStiffnessValue
```

### C#

```csharp
System.double AxialStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double AxialStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Wall axial stiffness value

## VBA Syntax

See [CWContactSet::AxialStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~AxialStiffnessValue.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall and [ICWContactSet::WallType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallType.html) is set to [swsWallType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWallType_e.html).swsWallTypeFlexible.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::WallStiffnessUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallStiffnessUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

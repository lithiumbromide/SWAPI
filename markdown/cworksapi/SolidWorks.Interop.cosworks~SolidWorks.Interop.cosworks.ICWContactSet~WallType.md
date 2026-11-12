---
title: "WallType Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "WallType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallType.html"
---

# WallType Property (ICWContactSet)

Gets or sets the wall type of this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property WallType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.WallType = value

value = instance.WallType
```

### C#

```csharp
System.int WallType {get; set;}
```

### C++/CLI

```cpp
property System.int WallType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Virtual wall type as defined in [swsWallType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWallType_e.html)

## VBA Syntax

See [CWContactSet::WallType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~WallType.html).

## Remarks

This property is valid only if [ICWContactSet::ContactSetType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~ContactSetType.html) is set to [swsContactSetTypeStaticNonLinear_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html).swsContactSetTypeStaticNonLinearVirtualWall.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::AxialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~AxialStiffnessValue.html)
[ICWContactSet::WallFriction Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallFriction.html)
[ICWContactSet::WallStiffnessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~WallStiffnessUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

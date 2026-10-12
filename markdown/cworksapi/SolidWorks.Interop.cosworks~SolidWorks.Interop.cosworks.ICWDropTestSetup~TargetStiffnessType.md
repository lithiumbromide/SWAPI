---
title: "TargetStiffnessType Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "TargetStiffnessType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetStiffnessType.html"
---

# TargetStiffnessType Property (ICWDropTestSetup)

Gets or sets the stiffness type of the impact plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property TargetStiffnessType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.TargetStiffnessType = value

value = instance.TargetStiffnessType
```

### C#

```csharp
System.int TargetStiffnessType {get; set;}
```

### C++/CLI

```cpp
property System.int TargetStiffnessType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Stiffness type as defined in [swsDropTargetStiffnessType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropTargetStiffnessType_e.html)

## VBA Syntax

See [CWDropTestSetup::TargetStiffnessType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~TargetStiffnessType.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForTargetOrientation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForTargetOrientation.html)
[ICWDropTestSetup::FrictionCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FrictionCoefficient.html)
[ICWDropTestSetup::MassDensity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~MassDensity.html)
[ICWDropTestSetup::NormalStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~NormalStiffness.html)
[ICWDropTestSetup::StiffnessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~StiffnessUnit.html)
[ICWDropTestSetup::TangentialStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TangentialStiffness.html)
[ICWDropTestSetup::TargetOrientationType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetOrientationType.html)
[ICWDropTestSetup::TargetThickness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetThickness.html)
[ICWDropTestSetup::ThicknessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~ThicknessUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

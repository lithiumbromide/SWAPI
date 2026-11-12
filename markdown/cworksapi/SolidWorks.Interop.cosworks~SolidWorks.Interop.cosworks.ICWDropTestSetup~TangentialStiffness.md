---
title: "TangentialStiffness Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "TangentialStiffness"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TangentialStiffness.html"
---

# TangentialStiffness Property (ICWDropTestSetup)

Gets or sets the stiffness per unit area that is parallel to the impact plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentialStiffness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.TangentialStiffness = value

value = instance.TangentialStiffness
```

### C#

```csharp
System.double TangentialStiffness {get; set;}
```

### C++/CLI

```cpp
property System.double TangentialStiffness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Stiffness per unit area that is parallel to the impact plane (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::TangentialStiffness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~TangentialStiffness.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This property is valid only if [ICWDropTestSetup::TargetStiffnessType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~TargetStiffnessType.html) = swsDropTargetStiffnessType_e.swsDropTargetStiffnessType_FlexibleTarget.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForTargetOrientation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForTargetOrientation.html)
[ICWDropTestSetup::FrictionCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FrictionCoefficient.html)
[ICWDropTestSetup::MassDensity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~MassDensity.html)
[ICWDropTestSetup::NormalStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~NormalStiffness.html)
[ICWDropTestSetup::StiffnessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~StiffnessUnit.html)
[ICWDropTestSetup::TargetOrientationType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetOrientationType.html)
[ICWDropTestSetup::TargetThickness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetThickness.html)
[ICWDropTestSetup::ThicknessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~ThicknessUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

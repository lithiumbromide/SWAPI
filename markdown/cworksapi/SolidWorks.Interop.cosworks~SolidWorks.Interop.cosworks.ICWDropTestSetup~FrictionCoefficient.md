---
title: "FrictionCoefficient Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "FrictionCoefficient"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FrictionCoefficient.html"
---

# FrictionCoefficient Property (ICWDropTestSetup)

Gets or sets the coefficient of friction between the model and the impact plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrictionCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.FrictionCoefficient = value

value = instance.FrictionCoefficient
```

### C#

```csharp
System.double FrictionCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.double FrictionCoefficient {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Coefficient of friction

## VBA Syntax

See [CWDropTestSetup::FrictionCoefficient](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~FrictionCoefficient.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForTargetOrientation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForTargetOrientation.html)
[ICWDropTestSetup::MassDensity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~MassDensity.html)
[ICWDropTestSetup::NormalStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~NormalStiffness.html)
[ICWDropTestSetup::StiffnessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~StiffnessUnit.html)
[ICWDropTestSetup::TangentialStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TangentialStiffness.html)
[ICWDropTestSetup::TargetOrientationType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetOrientationType.html)
[ICWDropTestSetup::TargetStiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetStiffnessType.html)
[ICWDropTestSetup::TargetThickness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetThickness.html)
[ICWDropTestSetup::ThicknessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~ThicknessUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

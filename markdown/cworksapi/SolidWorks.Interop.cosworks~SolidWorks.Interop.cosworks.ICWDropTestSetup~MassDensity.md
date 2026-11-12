---
title: "MassDensity Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "MassDensity"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~MassDensity.html"
---

# MassDensity Property (ICWDropTestSetup)

Gets or sets the mass density of the impact layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property MassDensity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.MassDensity = value

value = instance.MassDensity
```

### C#

```csharp
System.double MassDensity {get; set;}
```

### C++/CLI

```cpp
property System.double MassDensity {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Mass density of the impact layer (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::MassDensity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~MassDensity.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This property is valid only if [ICWDropTestSetup::TargetStiffnessType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~TargetStiffnessType.html) = swsDropTargetStiffnessType_e.swsDropTargetStiffnessType_FlexibleTarget.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForTargetOrientation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForTargetOrientation.html)
[ICWDropTestSetup::FrictionCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FrictionCoefficient.html)
[ICWDropTestSetup::NormalStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~NormalStiffness.html)
[ICWDropTestSetup::StiffnessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~StiffnessUnit.html)
[ICWDropTestSetup::TangentialStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TangentialStiffness.html)
[ICWDropTestSetup::TargetOrientationType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetOrientationType.html)
[ICWDropTestSetup::TargetThickness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetThickness.html)
[ICWDropTestSetup::ThicknessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~ThicknessUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

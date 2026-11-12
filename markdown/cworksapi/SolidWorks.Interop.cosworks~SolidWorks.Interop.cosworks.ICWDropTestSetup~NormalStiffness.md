---
title: "NormalStiffness Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "NormalStiffness"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~NormalStiffness.html"
---

# NormalStiffness Property (ICWDropTestSetup)

Gets or sets the stiffness per unit area that is normal to the impact plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalStiffness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.NormalStiffness = value

value = instance.NormalStiffness
```

### C#

```csharp
System.double NormalStiffness {get; set;}
```

### C++/CLI

```cpp
property System.double NormalStiffness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Stiffness per unit area that is normal to the impact plane (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::NormalStiffness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~NormalStiffness.html).

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
[ICWDropTestSetup::TangentialStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TangentialStiffness.html)
[ICWDropTestSetup::TargetOrientationType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetOrientationType.html)
[ICWDropTestSetup::TargetThickness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetThickness.html)
[ICWDropTestSetup::ThicknessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~ThicknessUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

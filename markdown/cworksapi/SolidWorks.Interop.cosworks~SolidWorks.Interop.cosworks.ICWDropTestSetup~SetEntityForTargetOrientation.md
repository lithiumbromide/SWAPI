---
title: "SetEntityForTargetOrientation Method (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "SetEntityForTargetOrientation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForTargetOrientation.html"
---

# SetEntityForTargetOrientation Method (ICWDropTestSetup)

Obsolete. Superseded by [ICWDropTestSetup::SetEntityForTargetOrientation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForTargetOrientation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEntityForTargetOrientation( _
   ByVal DispEntity As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim DispEntity As System.Object
Dim value As System.Integer

value = instance.SetEntityForTargetOrientation(DispEntity)
```

### C#

```csharp
System.int SetEntityForTargetOrientation(
   System.object DispEntity
)
```

### C++/CLI

```cpp
System.int SetEntityForTargetOrientation(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Reference plane

### Return Value

Error code as defined in [swsDropTestSetUpError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropTestSetUpError_e.html) (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::SetEntityForTargetOrientation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~SetEntityForTargetOrientation.html).

## Remarks

This method is valid only if [ICWDropTestSetup::TargetOrientationType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~TargetOrientationType.html) = swsDropTargetOrientationType_e.swsDropTargetOrientationType_ParallelToRefPlane.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::FrictionCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FrictionCoefficient.html)
[ICWDropTestSetup::TargetStiffnessType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetStiffnessType.html)
[ICWDropTestSetup::MassDensity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~MassDensity.html)
[ICWDropTestSetup::NormalStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~NormalStiffness.html)
[ICWDropTestSetup::StiffnessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~StiffnessUnit.html)
[ICWDropTestSetup::TangentialStiffness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TangentialStiffness.html)
[ICWDropTestSetup::TargetThickness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~TargetThickness.html)
[ICWDropTestSetup::ThicknessUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~ThicknessUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0

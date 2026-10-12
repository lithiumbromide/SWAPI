---
title: "SetDisplacementControlOptions Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SetDisplacementControlOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetDisplacementControlOptions.html"
---

# SetDisplacementControlOptions Method (ICWNonLinearStudyOptions)

Sets displacement control options for this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDisplacementControlOptions( _
   ByVal DispEntity As System.Object, _
   ByVal NDisplacementComponent As System.Integer, _
   ByVal NUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim DispEntity As System.Object
Dim NDisplacementComponent As System.Integer
Dim NUnit As System.Integer
Dim value As System.Integer

value = instance.SetDisplacementControlOptions(DispEntity, NDisplacementComponent, NUnit)
```

### C#

```csharp
System.int SetDisplacementControlOptions(
   System.object DispEntity,
   System.int NDisplacementComponent,
   System.int NUnit
)
```

### C++/CLI

```cpp
System.int SetDisplacementControlOptions(
   System.Object^ DispEntity,
   System.int NDisplacementComponent,
   System.int NUnit
)
```

### Parameters

- `DispEntity`: Vertex or reference point to control the analysis
- `NDisplacementComponent`: Displacement component for the selected location (see **Remarks**)
- `NUnit`: Units as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

### Return Value

Status as defined in [swsNonLinearStudyOptionsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonLinearStudyOptionsError_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::SetDisplacementControlOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SetDisplacementControlOptions.html).

## Remarks

[ICWNonLinearStudyOptions::ControlMethodType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ControlMethodType.html) must be set to [swsNonLinearOptionControlMethodType_e.swsNonLinearControl_Displacement](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonLinearOptionControlMethodType_e.html) to set displacement control options.

Valid displacement components are:

UX: X Translation. displacement in the Global X-direction

UY: Y Translation. displacement in the Global Y-direction

UZ: Z Translation. displacement in the Global Z-direction

RX: X Rotation. rotation about the Global X-direction for shell studies only

RY: Y Rotation. rotation about the Global Y-direction for shell studies only

RZ: Z Rotation. rotation about the Global Z-direction for shell studies only

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetDisplacementControlOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetDisplacementControlOptions.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3.0

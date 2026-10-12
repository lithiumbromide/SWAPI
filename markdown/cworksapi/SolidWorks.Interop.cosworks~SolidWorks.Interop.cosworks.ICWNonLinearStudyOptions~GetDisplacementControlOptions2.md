---
title: "GetDisplacementControlOptions2 Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "GetDisplacementControlOptions2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetDisplacementControlOptions2.html"
---

# GetDisplacementControlOptions2 Method (ICWNonLinearStudyOptions)

Gets displacement control options for this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetDisplacementControlOptions2( _
   ByRef NDisplacementComponent As System.Integer, _
   ByRef NUnit As System.Integer, _
   ByRef Dispatch As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim NDisplacementComponent As System.Integer
Dim NUnit As System.Integer
Dim Dispatch As System.Object

instance.GetDisplacementControlOptions2(NDisplacementComponent, NUnit, Dispatch)
```

### C#

```csharp
void GetDisplacementControlOptions2(
   out System.int NDisplacementComponent,
   out System.int NUnit,
   out System.object Dispatch
)
```

### C++/CLI

```cpp
void GetDisplacementControlOptions2(
   [Out] System.int NDisplacementComponent,
   [Out] System.int NUnit,
   [Out] System.Object^ Dispatch
)
```

### Parameters

- `NDisplacementComponent`: Displacement component for the selected location
- `NUnit`: Unit as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `Dispatch`: Selected vertex or reference point to control the analysis

## VBA Syntax

See [CWNonLinearStudyOptions::GetDisplacementControlOptions2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~GetDisplacementControlOptions2.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::SetDisplacementControlOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetDisplacementControlOptions.html)
[ICWNonLinearStudyOptions::ControlMethodType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ControlMethodType.html)

## Availability

SOLIDWORKS Simulation API 2010 SP5.0 and SOLIDWORKS Simulation 2011 SP1.0

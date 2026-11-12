---
title: "GetDisplacementControlOptions Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "GetDisplacementControlOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetDisplacementControlOptions.html"
---

# GetDisplacementControlOptions Method (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::GetDisplacementControlOptions2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions~GetDisplacementControlOptions2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetDisplacementControlOptions( _
   ByRef NDisplacementComponent As System.Integer, _
   ByRef NUnit As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim NDisplacementComponent As System.Integer
Dim NUnit As System.Integer

instance.GetDisplacementControlOptions(NDisplacementComponent, NUnit)
```

### C#

```csharp
void GetDisplacementControlOptions(
   out System.int NDisplacementComponent,
   out System.int NUnit
)
```

### C++/CLI

```cpp
void GetDisplacementControlOptions(
   [Out] System.int NDisplacementComponent,
   [Out] System.int NUnit
)
```

### Parameters

- `NDisplacementComponent`: Displacement component for the selected location
- `NUnit`: Unit as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::GetDisplacementControlOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~GetDisplacementControlOptions.html).

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP3.0

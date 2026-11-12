---
title: "AnalysisType Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "AnalysisType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~AnalysisType.html"
---

# AnalysisType Property (ICWStudy)

Gets the type of the analysis of the active study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AnalysisType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.AnalysisType
```

### C#

```csharp
System.int AnalysisType {get;}
```

### C++/CLI

```cpp
property System.int AnalysisType {
   System.int get();
}
```

### Property Value

Type of study as defined in [swsAnalysisStudyType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAnalysisStudyType_e.html)

## VBA Syntax

See [CWStudy::AnalysisType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~AnalysisType.html).

## Remarks

The proper license must be available to create the specified type of analysis. Only static, frequency, buckling, thermal, and nonlinear studies are currently supported. Fatigue, optimization, and pressure vessel studies are not currently supported.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::RunAnalysis Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~RunAnalysis.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

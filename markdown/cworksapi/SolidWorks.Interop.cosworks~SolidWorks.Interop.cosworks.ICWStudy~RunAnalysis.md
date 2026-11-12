---
title: "RunAnalysis Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "RunAnalysis"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~RunAnalysis.html"
---

# RunAnalysis Method (ICWStudy)

Runs this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunAnalysis() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.RunAnalysis()
```

### C#

```csharp
System.int RunAnalysis()
```

### C++/CLI

```cpp
System.int RunAnalysis();
```

### Return Value

Error as defined in [swsRunAnalysisError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRunAnalysisError_e.html)

## VBA Syntax

See [CWStudy::RunAnalysis](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~RunAnalysis.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## Remarks

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::AnalysisType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~AnalysisType.html)
[ICWStudy::MeshAndRun Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshAndRun.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

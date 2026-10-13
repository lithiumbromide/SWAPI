---
title: "Results Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "Results"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~Results.html"
---

# Results Property (ICWStudy)

Gets the results of this study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Results As CWResults
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWResults

value = instance.Results
```

### C#

```csharp
CWResults Results {get;}
```

### C++/CLI

```cpp
property CWResults^ Results {
   CWResults^ get();
}
```

### Property Value

[Results](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults.html)

## VBA Syntax

See [CWStudy::Results](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~Results.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analzye Part (VBA)](Analyze_Part_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

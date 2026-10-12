---
title: "DynamicAnalysisSubType Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "DynamicAnalysisSubType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DynamicAnalysisSubType.html"
---

# DynamicAnalysisSubType Property (ICWStudy)

Gets the type of this linear dynamic analysis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DynamicAnalysisSubType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.DynamicAnalysisSubType
```

### C#

```csharp
System.int DynamicAnalysisSubType {get;}
```

### C++/CLI

```cpp
property System.int DynamicAnalysisSubType {
   System.int get();
}
```

### Property Value

Type of linear dynamic analysis as defined in [swsDynamicAnalysisSubType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDynamicAnalysisSubType_e.html)

## VBA Syntax

See [CWStudy::DynamicAnalysisSubType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~DynamicAnalysisSubType.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0

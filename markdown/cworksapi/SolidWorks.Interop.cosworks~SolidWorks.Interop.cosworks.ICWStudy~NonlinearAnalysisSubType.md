---
title: "NonlinearAnalysisSubType Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "NonlinearAnalysisSubType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~NonlinearAnalysisSubType.html"
---

# NonlinearAnalysisSubType Property (ICWStudy)

Gets the subtype of this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NonlinearAnalysisSubType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.NonlinearAnalysisSubType
```

### C#

```csharp
System.int NonlinearAnalysisSubType {get;}
```

### C++/CLI

```cpp
property System.int NonlinearAnalysisSubType {
   System.int get();
}
```

### Property Value

Nonlinear subtype as defined in [swsNonlinearAnalysisSubType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNonlinearAnalysisSubType_e.html)

## VBA Syntax

See [CWStudy::NonlinearAnalysisSubType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~NonlinearAnalysisSubType.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::NonLinearStudyOptions Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~NonLinearStudyOptions.html)

## Availability

SOLIDWORKS Simulation API 2017 SP3

---
title: "NonLinearStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "NonLinearStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~NonLinearStudyOptions.html"
---

# NonLinearStudyOptions Property (ICWStudy)

Gets the options for this nonlinear study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NonLinearStudyOptions As CWNonLinearStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWNonLinearStudyOptions

value = instance.NonLinearStudyOptions
```

### C#

```csharp
CWNonLinearStudyOptions NonLinearStudyOptions {get;}
```

### C++/CLI

```cpp
property CWNonLinearStudyOptions^ NonLinearStudyOptions {
   CWNonLinearStudyOptions^ get();
}
```

### Property Value

[Nonlinear study options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html)

## VBA Syntax

See [CWStudy::NonLinearStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~NonLinearStudyOptions.html).

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICStudy::SetNonLinearStudyOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~SetNonLinearStudyOptions.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

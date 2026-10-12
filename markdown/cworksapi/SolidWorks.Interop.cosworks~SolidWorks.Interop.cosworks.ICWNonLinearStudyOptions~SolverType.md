---
title: "SolverType Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SolverType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SolverType.html"
---

# SolverType Property (ICWNonLinearStudyOptions)

Gets or sets the solver type associated with the study.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolverType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.SolverType = value

value = instance.SolverType
```

### C#

```csharp
System.int SolverType {get; set;}
```

### C++/CLI

```cpp
property System.int SolverType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Solver type as defined in [swsSolverType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSolverType_e.html) (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::SolverType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SolverType.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

The automatic solver is not supported for nonlinear studies; it supports static, frequency, and buckling studies only.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

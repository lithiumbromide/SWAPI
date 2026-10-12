---
title: "SolverType Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "SolverType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~SolverType.html"
---

# SolverType Property (ICWFrequencyStudyOptions)

Gets or sets the solver type associated with this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolverType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
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

Solver type as defined in [swsSolverType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSolverType_e.html)

## VBA Syntax

See [CWFrequencyStudyOptions::SolverType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~SolverType.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

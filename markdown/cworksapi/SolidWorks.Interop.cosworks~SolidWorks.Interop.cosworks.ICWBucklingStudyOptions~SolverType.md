---
title: "SolverType Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "SolverType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~SolverType.html"
---

# SolverType Property (ICWBucklingStudyOptions)

Gets or sets the solver type.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolverType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::SolverType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~SolverType.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

The automatic solver supports static, frequency, and buckling studies only.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

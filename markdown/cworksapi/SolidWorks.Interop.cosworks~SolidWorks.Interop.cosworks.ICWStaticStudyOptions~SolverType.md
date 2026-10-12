---
title: "SolverType Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "SolverType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~SolverType.html"
---

# SolverType Property (ICWStaticStudyOptions)

Gets or sets the solver type associated with the study.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolverType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::SolverType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~SolverType.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

The automatic solver supports static, frequency, and buckling studies only.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::UseInertialRelief Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInertialRelief.html)
[ICWStaticStudyOptions::UseInPlaneEffect Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInPlaneEffect.html)
[ICWStaticStudyOptions::UseSoftSpring Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseSoftSpring.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0

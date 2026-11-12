---
title: "MaxIterations Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "MaxIterations"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~MaxIterations.html"
---

# MaxIterations Property (ICosmosMotionStudyProperties)

Gets or sets the maximum number of times the numeric integrator iterates in the search for a solution for a given step.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxIterations As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Integer

instance.MaxIterations = value

value = instance.MaxIterations
```

### C#

```csharp
System.int MaxIterations {get; set;}
```

### C++/CLI

```cpp
property System.int MaxIterations {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Maximum number of times the numeric integrator iterates in the search for a solution for a given step

## VBA Syntax

See [CosmosMotionStudyProperties::MaxIterations](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~MaxIterations.html).

## Remarks

If the solver exceeds this limit, a convergence failure is recorded. The solver then quarters the last time step taken and integrates again. If four consecutive failures are recorded, there solver stops and displays information on the probable cause. The default is 25 and should not be changed.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

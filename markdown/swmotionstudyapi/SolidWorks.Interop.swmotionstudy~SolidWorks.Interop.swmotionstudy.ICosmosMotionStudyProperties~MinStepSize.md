---
title: "MinStepSize Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "MinStepSize"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~MinStepSize.html"
---

# MinStepSize Property (ICosmosMotionStudyProperties)

Gets or sets the lower bound of the integration time step.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinStepSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Double

instance.MinStepSize = value

value = instance.MinStepSize
```

### C#

```csharp
System.double MinStepSize {get; set;}
```

### C++/CLI

```cpp
property System.double MinStepSize {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Lower bound of the integration time step

## VBA Syntax

See [CosmosMotionStudyProperties::MinStepSize](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~MinStepSize.html).

## Remarks

This property is only important if the model has a locked position that the solver is needlessly trying to locate to a very high precision. Setting the parameter to a larger value causes the solver to stop sooner after a locked position is found.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)
[ICosmosMotionStudyProperties::MaxStepSize Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~MaxStepSize.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

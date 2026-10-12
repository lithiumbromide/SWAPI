---
title: "MaxStepSize Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "MaxStepSize"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~MaxStepSize.html"
---

# MaxStepSize Property (ICosmosMotionStudyProperties)

Gets or sets the upper bound of the integration time step.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxStepSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Double

instance.MaxStepSize = value

value = instance.MaxStepSize
```

### C#

```csharp
System.double MaxStepSize {get; set;}
```

### C++/CLI

```cpp
property System.double MaxStepSize {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Upper bound of the integration time step

## VBA Syntax

See [CosmosMotionStudyProperties::MaxStepSize](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~MaxStepSize.html).

## Remarks

This property is only important if the solver is missing short-lived events, such as impacts. It should be set to the same order as the short-lived events. Integration time can be much longer because the solver cannot move forward as fast.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)
[ICosmosMotionStudyProperties::MinStepSize Property](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~MinStepSize.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

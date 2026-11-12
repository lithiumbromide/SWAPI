---
title: "JacobianEval Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "JacobianEval"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~JacobianEval.html"
---

# JacobianEval Property (ICosmosMotionStudyProperties)

Gets or sets how often the simulation engine's Jacobian matrix is updated.

## Syntax

### Visual Basic (Declaration)

```vb
Property JacobianEval As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Integer

instance.JacobianEval = value

value = instance.JacobianEval
```

### C#

```csharp
System.int JacobianEval {get; set;}
```

### C++/CLI

```cpp
property System.int JacobianEval {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

How often, in percent, the simulation engine's Jacobian matrix is updated

## VBA Syntax

See [CosmosMotionStudyProperties::JacobianEval](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~JacobianEval.html).

## Remarks

At 100%, the Jacobian is updated at every integration time step. At 50% the Jacobian is updated at every other integration time step. This value impacts models that contain intermittent curve/curve contact. The higher the value, the better the simulation accuracy. However, the higher the value, the greater the impact in the overall simulation time.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

---
title: "IntegratorAdaptivity Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "IntegratorAdaptivity"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~IntegratorAdaptivity.html"
---

# IntegratorAdaptivity Property (ICosmosMotionStudyProperties)

Gets or sets the value to control intermittent curve/curve problems.

## Syntax

### Visual Basic (Declaration)

```vb
Property IntegratorAdaptivity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Double

instance.IntegratorAdaptivity = value

value = instance.IntegratorAdaptivity
```

### C#

```csharp
System.double IntegratorAdaptivity {get; set;}
```

### C++/CLI

```cpp
property System.double IntegratorAdaptivity {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Value to control intermittent curve/curve problems

## VBA Syntax

See [CosmosMotionStudyProperties::IntegratorAdaptivity](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~IntegratorAdaptivity.html).

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

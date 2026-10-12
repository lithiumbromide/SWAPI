---
title: "IntegratorType Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "IntegratorType"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~IntegratorType.html"
---

# IntegratorType Property (ICosmosMotionStudyProperties)

Gets or sets the type of integrator.

## Syntax

### Visual Basic (Declaration)

```vb
Property IntegratorType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Integer

instance.IntegratorType = value

value = instance.IntegratorType
```

### C#

```csharp
System.int IntegratorType {get; set;}
```

### C++/CLI

```cpp
property System.int IntegratorType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of integrator as defined by [swMotionIntegratorType_e](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionIntegratorType_e.html)

## VBA Syntax

See [CosmosMotionStudyProperties::IntegratorType](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~IntegratorType.html).

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

---
title: "DeleteRedundantConstraints Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "DeleteRedundantConstraints"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~DeleteRedundantConstraints.html"
---

# DeleteRedundantConstraints Property (ICosmosMotionStudyProperties)

Gets or sets whether to delete redundant constraints.

## Syntax

### Visual Basic (Declaration)

```vb
Property DeleteRedundantConstraints As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Boolean

instance.DeleteRedundantConstraints = value

value = instance.DeleteRedundantConstraints
```

### C#

```csharp
System.bool DeleteRedundantConstraints {get; set;}
```

### C++/CLI

```cpp
property System.bool DeleteRedundantConstraints {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to automatically delete redundant constraints, false to not

## VBA Syntax

See [CosmosMotionStudyProperties::DeleteRedundantConstraints](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~DeleteRedundantConstraints.html).

## Remarks

This property deletes all redundant constraints, leaving a fully constrained assembly. The remaining constraints support the loads in the system.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

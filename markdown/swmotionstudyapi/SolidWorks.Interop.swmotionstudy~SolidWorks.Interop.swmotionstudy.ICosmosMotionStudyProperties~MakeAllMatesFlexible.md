---
title: "MakeAllMatesFlexible Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "MakeAllMatesFlexible"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~MakeAllMatesFlexible.html"
---

# MakeAllMatesFlexible Property (ICosmosMotionStudyProperties)

Gets or sets whether to make all mates flexible.

## Syntax

### Visual Basic (Declaration)

```vb
Property MakeAllMatesFlexible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Boolean

instance.MakeAllMatesFlexible = value

value = instance.MakeAllMatesFlexible
```

### C#

```csharp
System.bool MakeAllMatesFlexible {get; set;}
```

### C++/CLI

```cpp
property System.bool MakeAllMatesFlexible {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to make all mates flexible, false to not

## VBA Syntax

See [CosmosMotionStudyProperties::MakeAllMatesFlexible](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~MakeAllMatesFlexible.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)

## Remarks

Setting this property to true turns all mates in the assembly into bushings (spring and damper systems containing some slop). In most cases, turning mates into bushings increases the calculation time.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

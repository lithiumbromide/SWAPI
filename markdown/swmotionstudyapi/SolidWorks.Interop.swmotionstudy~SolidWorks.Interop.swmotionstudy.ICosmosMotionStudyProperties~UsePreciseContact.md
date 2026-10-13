---
title: "UsePreciseContact Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "UsePreciseContact"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~UsePreciseContact.html"
---

# UsePreciseContact Property (ICosmosMotionStudyProperties)

Gets or sets whether to use precise contact.

## Syntax

### Visual Basic (Declaration)

```vb
Property UsePreciseContact As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Boolean

instance.UsePreciseContact = value

value = instance.UsePreciseContact
```

### C#

```csharp
System.bool UsePreciseContact {get; set;}
```

### C++/CLI

```cpp
property System.bool UsePreciseContact {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to use precise contact, false to not

## VBA Syntax

See [CosmosMotionStudyProperties::UsePreciseContact](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~UsePreciseContact.html).

## Remarks

Select to calculate contact by using the equations that represent the solid bodies, instead of many-sided polygons. This results in analytically correct contact, but takes the longest to calculate.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

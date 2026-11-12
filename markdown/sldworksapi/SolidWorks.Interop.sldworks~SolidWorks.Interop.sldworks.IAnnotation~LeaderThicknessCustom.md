---
title: "LeaderThicknessCustom Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "LeaderThicknessCustom"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.html"
---

# LeaderThicknessCustom Property (IAnnotation)

Gets or sets the leader's custom line thickness for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderThicknessCustom As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Double

instance.LeaderThicknessCustom = value

value = instance.LeaderThicknessCustom
```

### C#

```csharp
System.double LeaderThicknessCustom {get; set;}
```

### C++/CLI

```cpp
property System.double LeaderThicknessCustom {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for leader's custom line thickness

## VBA Syntax

See [Annotation::LeaderThicknessCustom](ms-its:sldworksapivb6.chm::/sldworks~Annotation~LeaderThicknessCustom.html).

## Remarks

IAnnotation::UseDocDispLeader must be false for this property to have any effect.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetDashedLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.html)
[IAnnotation::GetLeaderAllAround Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.html)
[IAnnotation::GetLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.html)
[IAnnotation::GetLeaderPerpendicular Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.html)
[IAnnotation::GetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.html)
[IAnnotation::GetLeaderSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.html)
[IAnnotation::GetLeaderStyle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderStyle.html)
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.html)
[IAnnotation::GetMultiJogLeaders ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)
[IAnnotation::SetLeader3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.html)
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.html)
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.html)
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

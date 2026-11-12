---
title: "BentLeaderLength Property (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "BentLeaderLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.html"
---

# BentLeaderLength Property (IAnnotation)

Gets or sets the length of the bent leader for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property BentLeaderLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Double

instance.BentLeaderLength = value

value = instance.BentLeaderLength
```

### C#

```csharp
System.double BentLeaderLength {get; set;}
```

### C++/CLI

```cpp
property System.double BentLeaderLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of the bent leader or -1 (see **Remarks**)

## VBA Syntax

See [Annotation::BentLeaderLength](ms-its:sldworksapivb6.chm::/sldworks~Annotation~BentLeaderLength.html).

## Examples

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

## Remarks

This property returns -1 if:

- this [type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.html) of annotation does not support bent leaders,
- this annotation does not have a bent leader, or
- the length of the bent leader is set by a [document property](sldworksAPIProgGuide.chm::/overview/System_Options_and_Document_Properties.htm).

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
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)
[IAnnotation::SetLeader3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.html)
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.html)
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.html)
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.html)
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

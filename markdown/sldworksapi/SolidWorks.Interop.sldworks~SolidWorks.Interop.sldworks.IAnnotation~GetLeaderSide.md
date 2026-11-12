---
title: "GetLeaderSide Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetLeaderSide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.html"
---

# GetLeaderSide Method (IAnnotation)

Gets the leader attachment side setting for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderSide() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Integer

value = instance.GetLeaderSide()
```

### C#

```csharp
System.int GetLeaderSide()
```

### C++/CLI

```cpp
System.int GetLeaderSide();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Leader side as define in [swLeaderSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderSide_e.html)

## VBA Syntax

See [Annotation::GetLeaderSide](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetLeaderSide.html).

## Remarks

The leader attachment side setting is a characteristic of the annotation, not of individual leaders. Therefore, you can get or set it regardless of whether leaders are currently displayed.

| Use... | To... |
| --- | --- |
| IAnnotation::GetLeaderStyle | Get leader characteristics |
| IAnnotation::SetLeader3 | Set leader characteristics |

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetDashedLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.html)
[IAnnotation::GetLeaderAllAround Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.html)
[IAnnotation::GetLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.html)
[IAnnotation::GetLeaderPerpendicular Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.html)
[IAnnotation::GetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.html)
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.html)
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.html)
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.html)
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.html)
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.html)
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.html)

## Availability

SOLIDWORKS 99, datecode 1999207

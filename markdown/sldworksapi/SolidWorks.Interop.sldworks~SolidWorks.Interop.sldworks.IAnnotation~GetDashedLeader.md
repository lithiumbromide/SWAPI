---
title: "GetDashedLeader Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetDashedLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.html"
---

# GetDashedLeader Method (IAnnotation)

Gets whether this leader is a dashed line or a solid line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDashedLeader() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.GetDashedLeader()
```

### C#

```csharp
System.bool GetDashedLeader()
```

### C++/CLI

```cpp
System.bool GetDashedLeader();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if leader is dashed line, false if it is solid line

## VBA Syntax

See [Annotation::GetDashedLeader](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetDashedLeader.html).

## Remarks

A datum target symbol is the only type of annotation that uses dashed leaders. For all other types of annotations, this method returns false, which indicates that the leader is a solid line.

| Use... | To... |
| --- | --- |
| IAnnotation::GetLeaderStyle | Get leader characteristics |
| IAnnotation::SetLeader3 | Set leader characteristics |

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetLeaderAllAround Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.html)
[IAnnotation::GetLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.html)
[IAnnotation::GetLeaderPerpendicular Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.html)
[IAnnotation::GetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.html)
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.html)
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)
[IAnnotation::GetLeaderSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.html)
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.html)
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.html)
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.html)
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.html)
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14

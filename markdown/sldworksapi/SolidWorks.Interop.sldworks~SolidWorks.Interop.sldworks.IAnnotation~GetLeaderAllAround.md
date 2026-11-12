---
title: "GetLeaderAllAround Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetLeaderAllAround"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.html"
---

# GetLeaderAllAround Method (IAnnotation)

Gets the setting for all-around symbol display of this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderAllAround() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.GetLeaderAllAround()
```

### C#

```csharp
System.bool GetLeaderAllAround()
```

### C++/CLI

```cpp
System.bool GetLeaderAllAround();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this annotation has the all-around symbol enabled, false if this annotation has the all-around symbol disabled

## VBA Syntax

See [Annotation::GetLeaderAllAround](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetLeaderAllAround.html).

## Remarks

The all-around display flag is a characteristic of the annotation, not of individual leaders. You can get or set it whether leaders are displayed.

If bent leaders are disabled for this annotation, you can still get or set the all-around display flag. However, SOLIDWORKS does not use it to display the annotation.

The all-around symbol applies only to geometric tolerances and weld symbols. For all other types of annotations, this method returns false.

| Use... | To... |
| --- | --- |
| IAnnotation::GetLeaderStyle | Get leader characteristics |
| IAnnotation::SetLeader3 | Set leader characteristics |

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetDashedLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.html)
[IAnnotation::GetLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.html)
[IAnnotation::GetLeaderPerpendicular Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.html)
[IAnnotation::GetLeaderSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.html)
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.html)
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.html)
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.html)
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.html)
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.html)
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.html)
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.html)

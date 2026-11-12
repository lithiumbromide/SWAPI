---
title: "GetCMPosition Method (IMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyResults"
member: "GetCMPosition"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults~GetCMPosition.html"
---

# GetCMPosition Method (IMotionStudyResults)

Gets the position of the specified component's center of mass at the specified time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCMPosition( _
   ByVal Time As System.Double, _
   ByVal Component As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyResults
Dim Time As System.Double
Dim Component As System.Object
Dim value As System.Object

value = instance.GetCMPosition(Time, Component)
```

### C#

```csharp
System.object GetCMPosition(
   System.double Time,
   System.object Component
)
```

### C++/CLI

```cpp
System.Object^ GetCMPosition(
   System.double Time,
   System.Object^ Component
)
```

### Parameters

- `Time`: Time
- `Component`: [Component](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IComponent2.html)

### Return Value

[Position of the component's center of mass](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [MotionStudyResults::GetCMPosition](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyResults~GetCMPosition.html).

## See Also

[IMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults.html)
[IMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

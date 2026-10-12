---
title: "GetAngularVelocity Method (IMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyResults"
member: "GetAngularVelocity"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults~GetAngularVelocity.html"
---

# GetAngularVelocity Method (IMotionStudyResults)

Gets the angular velocity for the specified component's at the specified time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAngularVelocity( _
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

value = instance.GetAngularVelocity(Time, Component)
```

### C#

```csharp
System.object GetAngularVelocity(
   System.double Time,
   System.object Component
)
```

### C++/CLI

```cpp
System.Object^ GetAngularVelocity(
   System.double Time,
   System.Object^ Component
)
```

### Parameters

- `Time`: Time
- `Component`: [Component](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IComponent2.html)

### Return Value

Angular velocity [vector](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [MotionStudyResults::GetAngularVelocity](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyResults~GetAngularVelocity.html).

## See Also

[IMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults.html)
[IMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

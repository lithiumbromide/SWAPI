---
title: "GetAngularAcceleration Method (IMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyResults"
member: "GetAngularAcceleration"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults~GetAngularAcceleration.html"
---

# GetAngularAcceleration Method (IMotionStudyResults)

Gets the angular acceleration for the specified component at the specified time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAngularAcceleration( _
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

value = instance.GetAngularAcceleration(Time, Component)
```

### C#

```csharp
System.object GetAngularAcceleration(
   System.double Time,
   System.object Component
)
```

### C++/CLI

```cpp
System.Object^ GetAngularAcceleration(
   System.double Time,
   System.Object^ Component
)
```

### Parameters

- `Time`: Time
- `Component`: [Component](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IComponent2.html)

### Return Value

Angular acceleration [vector](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [MotionStudyResults::GetAngularAcceleration](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyResults~GetAngularAcceleration.html).

## See Also

[IMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults.html)
[IMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

---
title: "GetLinearAcceleration Method (IMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyResults"
member: "GetLinearAcceleration"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults~GetLinearAcceleration.html"
---

# GetLinearAcceleration Method (IMotionStudyResults)

Gets the linear acceleration for the specified component at the specified time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinearAcceleration( _
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

value = instance.GetLinearAcceleration(Time, Component)
```

### C#

```csharp
System.object GetLinearAcceleration(
   System.double Time,
   System.object Component
)
```

### C++/CLI

```cpp
System.Object^ GetLinearAcceleration(
   System.double Time,
   System.Object^ Component
)
```

### Parameters

- `Time`: Time
- `Component`: [Component](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IComponent2.html)

### Return Value

Linear acceleeration [vector](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [MotionStudyResults::GetLinearAcceleration](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyResults~GetLinearAcceleration.html).

## See Also

[IMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults.html)
[IMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

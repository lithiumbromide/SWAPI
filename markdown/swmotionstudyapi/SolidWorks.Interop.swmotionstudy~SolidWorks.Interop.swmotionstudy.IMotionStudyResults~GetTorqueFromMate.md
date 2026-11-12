---
title: "GetTorqueFromMate Method (IMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyResults"
member: "GetTorqueFromMate"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults~GetTorqueFromMate.html"
---

# GetTorqueFromMate Method (IMotionStudyResults)

Gets the torque about the specified mate at the specified time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTorqueFromMate( _
   ByVal Time As System.Double, _
   ByVal Mate As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyResults
Dim Time As System.Double
Dim Mate As System.Object
Dim value As System.Object

value = instance.GetTorqueFromMate(Time, Mate)
```

### C#

```csharp
System.object GetTorqueFromMate(
   System.double Time,
   System.object Mate
)
```

### C++/CLI

```cpp
System.Object^ GetTorqueFromMate(
   System.double Time,
   System.Object^ Mate
)
```

### Parameters

- `Time`: Time
- `Mate`: [Mate](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IComponent2.html)

### Return Value

[Torgue about the mate](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) (see **Remarks**)

## VBA Syntax

See [MotionStudyResults::GetTorqueFromMate](ms-its:swmotionstudyapivb6.chm::/swmotionstudy~MotionStudyResults~GetTorqueFromMate.html).

## Remarks

If the mate is purely linear, then the return value is [0. 0. 0].

## See Also

[IMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults.html)
[IMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

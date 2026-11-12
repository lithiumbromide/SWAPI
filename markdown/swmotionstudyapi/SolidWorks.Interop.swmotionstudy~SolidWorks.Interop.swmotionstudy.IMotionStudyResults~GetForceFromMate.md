---
title: "GetForceFromMate Method (IMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyResults"
member: "GetForceFromMate"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults~GetForceFromMate.html"
---

# GetForceFromMate Method (IMotionStudyResults)

Gets the force about the specified mate at the specified time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetForceFromMate( _
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

value = instance.GetForceFromMate(Time, Mate)
```

### C#

```csharp
System.object GetForceFromMate(
   System.double Time,
   System.object Mate
)
```

### C++/CLI

```cpp
System.Object^ GetForceFromMate(
   System.double Time,
   System.Object^ Mate
)
```

### Parameters

- `Time`: Time
- `Mate`: [Mate](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~Solidworks.Interop.sldworks.IComponent2.html)

### Return Value

[Force about the mate](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) (see **Remarks**)

## VBA Syntax

See [MotionStudyResults::GetForceFromMate](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyResults~GetForceFromMate.html).

## Remarks

If the mate is purely angular, then the return value is [0, 0, 0].

## See Also

[IMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults.html)
[IMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

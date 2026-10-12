---
title: "SetLeader2 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetLeader2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader2.html"
---

# SetLeader2 Method (IAnnotation)

Obsolete. Superseded by [IAnnotation::SetLeader3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetLeader3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLeader2( _
   ByVal Leader As System.Boolean, _
   ByVal LeaderSide As System.Integer, _
   ByVal SmartArrowHeadStyle As System.Boolean, _
   ByVal BentLeader As System.Boolean, _
   ByVal Perpendicular As System.Boolean, _
   ByVal AllAround As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Leader As System.Boolean
Dim LeaderSide As System.Integer
Dim SmartArrowHeadStyle As System.Boolean
Dim BentLeader As System.Boolean
Dim Perpendicular As System.Boolean
Dim AllAround As System.Boolean
Dim value As System.Integer

value = instance.SetLeader2(Leader, LeaderSide, SmartArrowHeadStyle, BentLeader, Perpendicular, AllAround)
```

### C#

```csharp
System.int SetLeader2(
   System.bool Leader,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool BentLeader,
   System.bool Perpendicular,
   System.bool AllAround
)
```

### C++/CLI

```cpp
System.int SetLeader2(
   System.bool Leader,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool BentLeader,
   System.bool Perpendicular,
   System.bool AllAround
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Leader`:
- `LeaderSide`:
- `SmartArrowHeadStyle`:
- `BentLeader`:
- `Perpendicular`:
- `AllAround`:

## VBA Syntax

See [Annotation::SetLeader2](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetLeader2.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

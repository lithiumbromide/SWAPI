---
title: "SetLeader Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader.html"
---

# SetLeader Method (IAnnotation)

Obsolete. Superseded by [IAnnotation::SetLeader3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetLeader3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLeader( _
   ByVal Leader As System.Boolean, _
   ByVal LeaderSide As System.Integer, _
   ByVal SmartArrowHeadStyle As System.Boolean, _
   ByVal BentLeader As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Leader As System.Boolean
Dim LeaderSide As System.Integer
Dim SmartArrowHeadStyle As System.Boolean
Dim BentLeader As System.Boolean
Dim value As System.Integer

value = instance.SetLeader(Leader, LeaderSide, SmartArrowHeadStyle, BentLeader)
```

### C#

```csharp
System.int SetLeader(
   System.bool Leader,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool BentLeader
)
```

### C++/CLI

```cpp
System.int SetLeader(
   System.bool Leader,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool BentLeader
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Leader`:
- `LeaderSide`:
- `SmartArrowHeadStyle`:
- `BentLeader`:

## VBA Syntax

See [Annotation::SetLeader](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetLeader.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

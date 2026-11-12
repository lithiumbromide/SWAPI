---
title: "SelectByRay Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "SelectByRay"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SelectByRay.html"
---

# SelectByRay Method (IEModelViewControl)

Selects the first component intersected by a ray that starts at the specified point in the specified direction vector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectByRay( _
   ByVal StartX As System.Single, _
   ByVal StartY As System.Single, _
   ByVal StartZ As System.Single, _
   ByVal DirectionX As System.Single, _
   ByVal DirectionY As System.Single, _
   ByVal DirectionZ As System.Single _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim StartX As System.Single
Dim StartY As System.Single
Dim StartZ As System.Single
Dim DirectionX As System.Single
Dim DirectionY As System.Single
Dim DirectionZ As System.Single

instance.SelectByRay(StartX, StartY, StartZ, DirectionX, DirectionY, DirectionZ)
```

### C#

```csharp
void SelectByRay(
   System.float StartX,
   System.float StartY,
   System.float StartZ,
   System.float DirectionX,
   System.float DirectionY,
   System.float DirectionZ
)
```

### C++/CLI

```cpp
void SelectByRay(
   System.float StartX,
   System.float StartY,
   System.float StartZ,
   System.float DirectionX,
   System.float DirectionY,
   System.float DirectionZ
)
```

### Parameters

- `StartX`: x coordinate of start point
- `StartY`: y coordinate of start point
- `StartZ`: z coordinate of start point
- `DirectionX`: x coordinate of direction vector
- `DirectionY`: y coordinate of direction vector
- `DirectionZ`: y coordinate of direction vector

## VBA Syntax

See [EModelViewControl::SelectByRay](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~SelectByRay.html).

## Remarks

Call this method before calling [IEModelViewControl::GetSelectedComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~GetSelectedComponentName.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2014 SP0

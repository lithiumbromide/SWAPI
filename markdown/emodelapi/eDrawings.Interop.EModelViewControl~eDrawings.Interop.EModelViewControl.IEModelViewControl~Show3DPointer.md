---
title: "Show3DPointer Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Show3DPointer"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Show3DPointer.html"
---

# Show3DPointer Method (IEModelViewControl)

Shows or hides a 3D pointer in the active view in the graphics area.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Show3DPointer( _
   ByVal show As System.Boolean, _
   ByVal StartX As System.Single, _
   ByVal StartY As System.Single, _
   ByVal StartZ As System.Single, _
   ByVal EndX As System.Single, _
   ByVal EndY As System.Single, _
   ByVal EndZ As System.Single _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim show As System.Boolean
Dim StartX As System.Single
Dim StartY As System.Single
Dim StartZ As System.Single
Dim EndX As System.Single
Dim EndY As System.Single
Dim EndZ As System.Single

instance.Show3DPointer(show, StartX, StartY, StartZ, EndX, EndY, EndZ)
```

### C#

```csharp
void Show3DPointer(
   System.bool show,
   System.float StartX,
   System.float StartY,
   System.float StartZ,
   System.float EndX,
   System.float EndY,
   System.float EndZ
)
```

### C++/CLI

```cpp
void Show3DPointer(
   System.bool show,
   System.float StartX,
   System.float StartY,
   System.float StartZ,
   System.float EndX,
   System.float EndY,
   System.float EndZ
)
```

### Parameters

- `show`: True to show the 3D Pointer, false to hide it
- `StartX`: x coordinate of the position of the sphere and the start point of the line
- `StartY`: y coordinate of the position of the sphere and the start point of the line
- `StartZ`: z coordinate of the position of the sphere and the start point of the line
- `EndX`: x coordinate of the end point of the line
- `EndY`: y coordinate of the end point of the line
- `EndZ`: z coordinate of the end point of the line

## VBA Syntax

See [EModelViewControl::Show3DPointer](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Show3DPointer.html).

## Remarks

The [3D pointer](3DPointer.gif) shown by this method is not the same 3D pointer available in the eDrawings user interface.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2014 SP0

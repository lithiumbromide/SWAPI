---
title: "AddStamp Method (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "AddStamp"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~AddStamp.html"
---

# AddStamp Method (IEModelMarkupControl)

Adds the specified rubber stamp to an eDrawings document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddStamp( _
   ByVal Filename As System.String, _
   ByVal X As System.Single, _
   ByVal Y As System.Single, _
   ByVal Width As System.Single, _
   ByVal Height As System.Single _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim Filename As System.String
Dim X As System.Single
Dim Y As System.Single
Dim Width As System.Single
Dim Height As System.Single

instance.AddStamp(Filename, X, Y, Width, Height)
```

### C#

```csharp
void AddStamp(
   System.string Filename,
   System.float X,
   System.float Y,
   System.float Width,
   System.float Height
)
```

### C++/CLI

```cpp
void AddStamp(
   System.String^ Filename,
   System.float X,
   System.float Y,
   System.float Width,
   System.float Height
)
```

### Parameters

- `Filename`: Path and name of the file containing an image of a rubber stamp
- `X`: - Parts and assemblies: x screen coordinate
    - or -
  - Drawings: x drawing coordinate
- `Y`: - Parts and assemblies: y screen coordinate
    - or -

  Drawings: y drawing coordinate
- `Width`: - Parts and assemblies: not applicable; no meaning
    - or -
  - Drawings: width of the stamp in drawing coordinates
- `Height`: - Parts and assemblies: not applicable; no meaning
    - or -

  Drawings: height of the stamp in drawing coordinates

## VBA Syntax

See [EModelMarkupControl::AddStamp](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~AddStamp.html).

## Examples

See the [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl.html) examples.

## Remarks

The stamp is inserted into the scene using screen coordinates. The lower-left corner is -1,-1, and the upper-right corner is 1,1, making the insertion hardware-independent.

When the stamp is inserted on a second sheet, it is in drawing coordinates. The lower-left corner of the drawing sheet is 0,0. X and Y are in meters. The optional Height and Width are also in meters.

The position is the center of the stamp.

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)

## Availability

eDrawings API 2007 SP0

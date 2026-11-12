---
title: "Print4 Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Print4"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print4.html"
---

# Print4 Method (IEModelViewControl)

Obsolete. Superseded by [IEModelViewControl::Print5](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Print4( _
   ByVal ShowDialog As System.Boolean, _
   ByVal FileName As System.String, _
   ByVal Shaded As System.Boolean, _
   ByVal DraftQuality As System.Boolean, _
   ByVal Color As System.Boolean, _
   ByVal printType As EMVPrintType, _
   ByVal scale As System.Double, _
   ByVal centerOffsetX As System.Integer, _
   ByVal centerOffsetY As System.Integer, _
   ByVal printAll As System.Boolean, _
   ByVal pageFirst As System.Integer, _
   ByVal pageLast As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim ShowDialog As System.Boolean
Dim FileName As System.String
Dim Shaded As System.Boolean
Dim DraftQuality As System.Boolean
Dim Color As System.Boolean
Dim printType As EMVPrintType
Dim scale As System.Double
Dim centerOffsetX As System.Integer
Dim centerOffsetY As System.Integer
Dim printAll As System.Boolean
Dim pageFirst As System.Integer
Dim pageLast As System.Integer

instance.Print4(ShowDialog, FileName, Shaded, DraftQuality, Color, printType, scale, centerOffsetX, centerOffsetY, printAll, pageFirst, pageLast)
```

### C#

```csharp
void Print4(
   System.bool ShowDialog,
   System.string FileName,
   System.bool Shaded,
   System.bool DraftQuality,
   System.bool Color,
   EMVPrintType printType,
   System.double scale,
   System.int centerOffsetX,
   System.int centerOffsetY,
   System.bool printAll,
   System.int pageFirst,
   System.int pageLast
)
```

### C++/CLI

```cpp
void Print4(
   System.bool ShowDialog,
   System.String^ FileName,
   System.bool Shaded,
   System.bool DraftQuality,
   System.bool Color,
   EMVPrintType printType,
   System.double scale,
   System.int centerOffsetX,
   System.int centerOffsetY,
   System.bool printAll,
   System.int pageFirst,
   System.int pageLast
)
```

### Parameters

- `ShowDialog`: True to show the Print dialog, false to not
- `FileName`: Document name to show in the printer queue for this eDrawings file (see Remarks)
- `Shaded`: True to print shaded, false to not print shaded
- `DraftQuality`: True to print draft quality, false to print regular quality
- `Color`: True to print in grayscale on black-and-white printers, false to print black and white (lines, edges, and text are black, and shaded data is grayscale)
- `printType`: Scale the eDrawings file as defined in [EMVPrintType](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVPrintType.html) (see Remarks)
- `scale`: Scaling factor; this argument is valid only when printType is set to eScaled
- `centerOffsetX`: Offset in thousands of an inch; this argument is valid only when printType is set to eScaled
- `centerOffsetY`: Offset in thousands of an inch; this argument is valid only when printType is set to eScaled
- `printAll`: True to print all pages, false to not
- `pageFirst`: Page number of first page to print
- `pageLast`: Page number of last page to print

## VBA Syntax

See [EModelViewControl::Print4](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Print4.html).

## Remarks

Set [IEModelViewControl::SetPageSetupOptions](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SetPageSetupOptions.html) before calling this method.

You can use the FileName argument to describe the eDrawings file so that it is easily recognizable in the printer queue.

The printType argument must be set to eWYSIWYG for parts and assemblies. eWYSIWYG is also valid for drawings as are the other [EMVPrintType](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVPrintType.html) enumerations.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings 2010 SP0

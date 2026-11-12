---
title: "SetPageSetupOptions Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "SetPageSetupOptions"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SetPageSetupOptions.html"
---

# SetPageSetupOptions Method (IEModelViewControl)

Sets the Page Setup parameters for printing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPageSetupOptions( _
   ByVal Orientation As EMVPrintOrientation, _
   ByVal PaperSize As System.Integer, _
   ByVal PaperLength As System.Integer, _
   ByVal PaperWidth As System.Integer, _
   ByVal Copies As System.Integer, _
   ByVal Source As System.Integer, _
   ByVal Printer As System.String, _
   ByVal TopMargin As System.Integer, _
   ByVal BottomMargin As System.Integer, _
   ByVal LeftMargin As System.Integer, _
   ByVal RightMargin As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim Orientation As EMVPrintOrientation
Dim PaperSize As System.Integer
Dim PaperLength As System.Integer
Dim PaperWidth As System.Integer
Dim Copies As System.Integer
Dim Source As System.Integer
Dim Printer As System.String
Dim TopMargin As System.Integer
Dim BottomMargin As System.Integer
Dim LeftMargin As System.Integer
Dim RightMargin As System.Integer

instance.SetPageSetupOptions(Orientation, PaperSize, PaperLength, PaperWidth, Copies, Source, Printer, TopMargin, BottomMargin, LeftMargin, RightMargin)
```

### C#

```csharp
void SetPageSetupOptions(
   EMVPrintOrientation Orientation,
   System.int PaperSize,
   System.int PaperLength,
   System.int PaperWidth,
   System.int Copies,
   System.int Source,
   System.string Printer,
   System.int TopMargin,
   System.int BottomMargin,
   System.int LeftMargin,
   System.int RightMargin
)
```

### C++/CLI

```cpp
void SetPageSetupOptions(
   EMVPrintOrientation Orientation,
   System.int PaperSize,
   System.int PaperLength,
   System.int PaperWidth,
   System.int Copies,
   System.int Source,
   System.String^ Printer,
   System.int TopMargin,
   System.int BottomMargin,
   System.int LeftMargin,
   System.int RightMargin
)
```

### Parameters

- `Orientation`: Page orientation as defined in [EMVPrintOrientation](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVPrintOrientation.html)
- `PaperSize`: Use Windows printer constants (see Remarks)
- `PaperLength`: Custom size in thousandths of an inch, if you are not using a standard paper size
- `PaperWidth`: Custom size in thousandths of an inch
- `Copies`: Number of copies
- `Source`: Paper tray source; use Windows printer constants
- `Printer`: Printer name
- `TopMargin`: Top margin in thousandths of an inch or 0 to use printer's margin
- `BottomMargin`: Bottom margin in thousandths of an inch or 0 to use printer's margin
- `LeftMargin`: Left margin in thousandths of an inch or 0 to use printer's margin
- `RightMargin`: Right margin in thousandths of an inch or 0 to use printer's margin

## VBA Syntax

See [EModelViewControl::SetPageSetupOptions](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~SetPageSetupOptions.html).

## Remarks

Call this method before calling [IEModelViewControl::Print5](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print5.html).

You can find a list of Windows printer constants in wingdi.h or in the .NET enumerations Printing.PaperKind or Printing.PaperSource. Some common settings include:

- Paper Size

  - Letter (letter 8 1/2 x 11 in) = 1
  - C-sheet (C size sheet = 24
  - D-sheet (D size sheet) = 25
  - E-sheet (E size sheet) = 26
- Paper Source (paper tray)

  - Upper tray = 1
  - Lower tray = 2
  - Middle tray =3
  - Manual = 4
  - Auto (recommended default) = 7

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0

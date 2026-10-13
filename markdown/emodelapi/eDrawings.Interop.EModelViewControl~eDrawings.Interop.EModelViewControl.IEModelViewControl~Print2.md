---
title: "Print2 Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Print2"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print2.html"
---

# Print2 Method (IEModelViewControl)

Obsolete. Superseded by [IEModelViewControl::Print3](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Print2( _
   ByVal ShowDialog As System.Boolean, _
   ByVal FileName As System.String, _
   ByVal Shaded As System.Boolean, _
   ByVal DraftQuality As System.Boolean, _
   ByVal Color As System.Boolean, _
   ByVal ScaleToFit As EMVPrintType _
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
Dim ScaleToFit As EMVPrintType

instance.Print2(ShowDialog, FileName, Shaded, DraftQuality, Color, ScaleToFit)
```

### C#

```csharp
void Print2(
   System.bool ShowDialog,
   System.string FileName,
   System.bool Shaded,
   System.bool DraftQuality,
   System.bool Color,
   EMVPrintType ScaleToFit
)
```

### C++/CLI

```cpp
void Print2(
   System.bool ShowDialog,
   System.String^ FileName,
   System.bool Shaded,
   System.bool DraftQuality,
   System.bool Color,
   EMVPrintType ScaleToFit
)
```

### Parameters

- `ShowDialog`: True to show the Print dialog, false to not
- `FileName`: Document name to show in the printer queue for this eDrawings file (see Remarks)
- `Shaded`: True to print shaded, false to print not shaded
- `DraftQuality`: True to print draft quality, false to print regular quality
- `Color`: True to print color, false to print black and white
- `ScaleToFit`: Scale the eDrawings file as defined in [EMVPrintType](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVPrintType.html) (see Remarks)

## VBA Syntax

See [EModelViewControl::Print2](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Print2.html).

## Remarks

Set [IEModelViewControl::SetPageSetupOptions](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SetPageSetupOptions.html) before calling this method.

You can use the FileName argument to describe the eDrawings file so that it is easily recognizable in the printer queue. This argument is optional.

The ScaleToFit argument must be set to eWYSIWYG for parts and assemblies; the other two options are only appropriate for drawings.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[_IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler.html)

## Availability

eDrawings API 2005 SP0

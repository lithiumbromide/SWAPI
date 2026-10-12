---
title: "Print5 Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Print5"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print5.html"
---

# Print5 Method (IEModelViewControl)

Prints the eDrawings file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Print5( _
   ByVal ShowDialog As System.Boolean, _
   ByVal FileNameInPrintQueue As System.String, _
   ByVal Shaded As System.Boolean, _
   ByVal DraftQuality As System.Boolean, _
   ByVal Color As System.Boolean, _
   ByVal printType As EMVPrintType, _
   ByVal scale As System.Double, _
   ByVal centerOffsetX As System.Integer, _
   ByVal centerOffsetY As System.Integer, _
   ByVal printAll As System.Boolean, _
   ByVal pageFirst As System.Integer, _
   ByVal pageLast As System.Integer, _
   ByVal PrintToFileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim ShowDialog As System.Boolean
Dim FileNameInPrintQueue As System.String
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
Dim PrintToFileName As System.String

instance.Print5(ShowDialog, FileNameInPrintQueue, Shaded, DraftQuality, Color, printType, scale, centerOffsetX, centerOffsetY, printAll, pageFirst, pageLast, PrintToFileName)
```

### C#

```csharp
void Print5(
   System.bool ShowDialog,
   System.string FileNameInPrintQueue,
   System.bool Shaded,
   System.bool DraftQuality,
   System.bool Color,
   EMVPrintType printType,
   System.double scale,
   System.int centerOffsetX,
   System.int centerOffsetY,
   System.bool printAll,
   System.int pageFirst,
   System.int pageLast,
   System.string PrintToFileName
)
```

### C++/CLI

```cpp
void Print5(
   System.bool ShowDialog,
   System.String^ FileNameInPrintQueue,
   System.bool Shaded,
   System.bool DraftQuality,
   System.bool Color,
   EMVPrintType printType,
   System.double scale,
   System.int centerOffsetX,
   System.int centerOffsetY,
   System.bool printAll,
   System.int pageFirst,
   System.int pageLast,
   System.String^ PrintToFileName
)
```

### Parameters

- `ShowDialog`: True to show the Print dialog, false to not
- `FileNameInPrintQueue`: Document name to show in the printer queue for this eDrawings file (see Remarks)
- `Shaded`: True to print shaded, false to not print shaded
- `DraftQuality`: True to print draft quality, false to print regular quality
- `Color`: True to print in grayscale on black-and-white printers, false to print black and white (lines, edges, and text are black, and shaded data is grayscale)
- `printType`: Scale the eDrawings file as defined in [EMVPrintType](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVPrintType.html) (see Remarks)
- `scale`: Scaling factor; this argument is valid only when printType is set to eScaled
- `centerOffsetX`: Offset in thousands of an inch; this argument is valid only when printType is set to eScaled
- `centerOffsetY`: Offset in thousands of an inch; this argument is valid only when printType is set to eScaled
- `printAll`: True to print all pages, false to not
- `pageFirst`: Page number of first page to print; this argument is valid only when printAll is set to false
- `pageLast`: Page number of last page to print; this argument is valid only when printAll is set to false
- `PrintToFileName`: File name to which to print the eDrawings file (see **Remarks**)

## VBA Syntax

See [EModelViewControl::Print5](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Print5.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Set [IEModelViewControl::SetPageSetupOptions](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SetPageSetupOptions.html) before calling this method.

You can use the FileNameInPrintQueue argument to describe the eDrawings document to print so that it is easily recognizable in the printer queue.

The printType argument must be set to eWYSIWYG for parts and assemblies. eWYSIWYG is also valid for drawings as are the other [EMVPrintType](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVPrintType.html) enumerations.

| To print an eDrawings document to a... | Specify... |
| --- | --- |
| Printer | An empty string for the PrintToFileName argument. |
| File | A file name for the PrintToFileName argument that is different than the file name of the eDrawings document. NOTE: If you specify the same file name as the eDrawings document's file name, then an error occurs and the eDrawings document is not printed to another file. |

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[_IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler.html)

## Availability

eDrawings API 2011 SP04

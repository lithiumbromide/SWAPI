---
title: "GetPrinterComment Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetPrinterComment"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html"
---

# GetPrinterComment Method (ISw3DPrinter)

Gets a general-purpose string, possibly one that the user specified during installation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrinterComment() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As System.String

value = instance.GetPrinterComment()
```

### C#

```csharp
System.string GetPrinterComment()
```

### C++/CLI

```cpp
System.String^ GetPrinterComment();
```

### Return Value

General-purpose string

## VBA Syntax

See [Sw3DPrinter::GetPrinterComment](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetPrinterComment.html).

## Remarks

This method is called at startup.

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCurrentPrinterName Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentPrinterName.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::GetDefaultPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html)
[ISw3DPrinter::GetDialogConfiguration Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDialogConfiguration.html)
[ISw3DPrinter::GetOutputOptions Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOptions.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterStatus Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterStatus.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)
[ISw3DPrinter::OnStartup Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnStartup.html)
[ISw3DPrinter::SetCurrentPrinterName Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetCurrentPrinterName.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

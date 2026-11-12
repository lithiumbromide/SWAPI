---
title: "GetDefaultPrintQuality Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetDefaultPrintQuality"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html"
---

# GetDefaultPrintQuality Method (ISw3DPrinter)

Gets the default setting for print quality.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefaultPrintQuality() As swPrintQuality_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As swPrintQuality_e

value = instance.GetDefaultPrintQuality()
```

### C#

```csharp
swPrintQuality_e GetDefaultPrintQuality()
```

### C++/CLI

```cpp
swPrintQuality_e GetDefaultPrintQuality();
```

### Return Value

Default setting for print quality as defined in [swPrintQuality_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swPrintQuality_e.html)

## VBA Syntax

See [Sw3DPrinter::GetDefaultPrintQuality](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetDefaultPrintQuality.html).

## Remarks

This method is called at startup.

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::GetDialogConfiguration Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDialogConfiguration.html)
[ISw3DPrinter::GetOutputOptions Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOptions.html)
[ISw3DPrinter::GetPrinterComment Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)
[ISw3DPrinter::GetPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrintQuality.html)
[ISw3DPrinter::OnStartup Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnStartup.html)
[ISw3DPrinter::SetPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetPrintQuality.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

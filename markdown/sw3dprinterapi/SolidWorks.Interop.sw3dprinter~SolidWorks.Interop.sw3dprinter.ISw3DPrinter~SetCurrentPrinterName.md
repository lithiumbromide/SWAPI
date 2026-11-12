---
title: "SetCurrentPrinterName Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetCurrentPrinterName"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetCurrentPrinterName.html"
---

# SetCurrentPrinterName Method (ISw3DPrinter)

Sets the name of the current printer.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCurrentPrinterName( _
   ByVal Material As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim Material As System.String

instance.SetCurrentPrinterName(Material)
```

### C#

```csharp
void SetCurrentPrinterName(
   System.string Material
)
```

### C++/CLI

```cpp
void SetCurrentPrinterName(
   System.String^ Material
)
```

### Parameters

- `Material`: Name of current printer

## VBA Syntax

See [Sw3DPrinter::SetCurrentPrinterName](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetCurrentPrinterName.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCurrentPrinterName Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentPrinterName.html)
[ISw3DPrinter::GetPrinterComment Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterStatus Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterStatus.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

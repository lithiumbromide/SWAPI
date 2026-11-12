---
title: "GetPrintQuality Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetPrintQuality"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrintQuality.html"
---

# GetPrintQuality Method (ISw3DPrinter)

Gets the current print quality setting of the printer.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrintQuality() As swPrintQuality_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As swPrintQuality_e

value = instance.GetPrintQuality()
```

### C#

```csharp
swPrintQuality_e GetPrintQuality()
```

### C++/CLI

```cpp
swPrintQuality_e GetPrintQuality();
```

### Return Value

Print quality setting as defined in [swPrintQuality_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swPrintQuality_e.html)

## VBA Syntax

See [Sw3DPrinter::GetPrintQuality](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetPrintQuality.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetDefaultPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html)
[ISw3DPrinter::SetPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetPrintQuality.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

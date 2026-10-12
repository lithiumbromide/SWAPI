---
title: "GetPrinterStatus Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetPrinterStatus"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterStatus.html"
---

# GetPrinterStatus Method (ISw3DPrinter)

Gets the current state of the printer.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPrinterStatus( _
   ByRef StatusMessage As System.String _
) As swPrinterStatus_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim StatusMessage As System.String
Dim value As swPrinterStatus_e

value = instance.GetPrinterStatus(StatusMessage)
```

### C#

```csharp
swPrinterStatus_e GetPrinterStatus(
   out System.string StatusMessage
)
```

### C++/CLI

```cpp
swPrinterStatus_e GetPrinterStatus(
   [Out] System.String^ StatusMessage
)
```

### Parameters

- `StatusMessage`: Comment about printer's current state

### Return Value

Code indicating printer's current state as defined in [swPrinterStatus_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swPrinterStatus_e.html)

## VBA Syntax

See [Sw3DPrinter::GetPrinterStatus](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetPrinterStatus.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCurrentPrinterName Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentPrinterName.html)
[ISw3DPrinter::GetPrinterComment Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)
[ISw3DPrinter::SetCurrentPrinterName Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetCurrentPrinterName.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

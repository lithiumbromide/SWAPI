---
title: "SetPrintQuality Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetPrintQuality"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetPrintQuality.html"
---

# SetPrintQuality Method (ISw3DPrinter)

Called when a user selects a print quality setting on the 3D Printer tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPrintQuality( _
   ByVal Quality As swPrintQuality_e _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim Quality As swPrintQuality_e

instance.SetPrintQuality(Quality)
```

### C#

```csharp
void SetPrintQuality(
   swPrintQuality_e Quality
)
```

### C++/CLI

```cpp
void SetPrintQuality(
   swPrintQuality_e Quality
)
```

### Parameters

- `Quality`: Print quality setting as defined in [swPrintQuality_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swPrintQuality_e.html)

## VBA Syntax

See [Sw3DPrinter::SetPrintQuality](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetPrintQuality.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetDefaultPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html)
[ISw3DPrinter::GetPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrintQuality.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

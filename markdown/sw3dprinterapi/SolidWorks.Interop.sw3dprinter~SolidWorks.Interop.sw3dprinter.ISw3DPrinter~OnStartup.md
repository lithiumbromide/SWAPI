---
title: "OnStartup Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "OnStartup"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnStartup.html"
---

# OnStartup Method (ISw3DPrinter)

Called when the user selects the vendor's printer from the Name box on the 3D Printer tab.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnStartup( _
   ByVal ActiveModel As System.Object _
) As swStartupResult_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim ActiveModel As System.Object
Dim value As swStartupResult_e

value = instance.OnStartup(ActiveModel)
```

### C#

```csharp
swStartupResult_e OnStartup(
   System.object ActiveModel
)
```

### C++/CLI

```cpp
swStartupResult_e OnStartup(
   System.Object^ ActiveModel
)
```

### Parameters

- `ActiveModel`: Printer that corresponds to user's selection

### Return Value

Status of start up as defined in [swStartupResult_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swStartupResult_e.html)

## VBA Syntax

See [Sw3DPrinter::OnStartup](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~OnStartup.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::GetDefaultPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html)
[ISw3DPrinter::GetDialogConfiguration Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDialogConfiguration.html)
[ISw3DPrinter::GetOutputOptions Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOptions.html)
[ISw3DPrinter::GetPrinterComment Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

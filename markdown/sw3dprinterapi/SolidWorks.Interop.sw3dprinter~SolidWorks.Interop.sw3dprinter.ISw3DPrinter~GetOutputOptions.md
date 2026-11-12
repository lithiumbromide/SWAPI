---
title: "GetOutputOptions Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetOutputOptions"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOptions.html"
---

# GetOutputOptions Method (ISw3DPrinter)

Gets an array of strings that specify how to create the rapid prototype, e.g. "Print directly to machine", "Print to queue", "Create data file", etc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOutputOptions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As System.Object

value = instance.GetOutputOptions()
```

### C#

```csharp
System.object GetOutputOptions()
```

### C++/CLI

```cpp
System.Object^ GetOutputOptions();
```

### Return Value

Array of strings that specify how to create the rapid prototype

## VBA Syntax

See [Sw3DPrinter::GetOutputOptions](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetOutputOptions.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::GetDefaultPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html)
[ISw3DPrinter::GetDialogConfiguration Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDialogConfiguration.html)
[ISw3DPrinter::GetOutputOption Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOption.html)
[ISw3DPrinter::GetPrinterComment Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)
[ISw3DPrinter::OnStartup Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnStartup.html)
[ISw3DPrinter::SetOutputOption Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetOutputOption.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

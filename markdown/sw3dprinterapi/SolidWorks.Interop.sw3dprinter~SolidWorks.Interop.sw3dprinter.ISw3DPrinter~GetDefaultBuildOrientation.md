---
title: "GetDefaultBuildOrientation Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetDefaultBuildOrientation"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html"
---

# GetDefaultBuildOrientation Method (ISw3DPrinter)

Gets the default build orientation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefaultBuildOrientation() As swBuildOrientation_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As swBuildOrientation_e

value = instance.GetDefaultBuildOrientation()
```

### C#

```csharp
swBuildOrientation_e GetDefaultBuildOrientation()
```

### C++/CLI

```cpp
swBuildOrientation_e GetDefaultBuildOrientation();
```

### Return Value

Default build orientation as defined in [swBuildOrientation_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swBuildOrientation_e.html)

## VBA Syntax

See [Sw3DPrinter::GetDefaultBuildOrientation](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetDefaultBuildOrientation.html).

## Remarks

This method is called on startup.

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetBuildOrientation.html)
[ISw3DPrinter::GetCurrentOrientationTransform Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentOrientationTransform.html)
[ISw3DPrinter::GetDefaultPrintQuality Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultPrintQuality.html)
[ISw3DPrinter::GetDialogConfiguration Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDialogConfiguration.html)
[ISw3DPrinter::GetOutputOptions Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetOutputOptions.html)
[ISw3DPrinter::GetPrinterComment Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterComment.html)
[ISw3DPrinter::GetPrinterImageBitmap Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterImageBitmap.html)
[ISw3DPrinter::GetPrinterLocation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterLocation.html)
[ISw3DPrinter::GetPrinterNames Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterNames.html)
[ISw3DPrinter::GetPrinterType Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetPrinterType.html)
[ISw3DPrinter::OnStartup Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnStartup.html)
[ISw3DPrinter::SetBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetBuildOrientation.html)
[ISw3DPrinter::SetOrientationTransform Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetOrientationTransform.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

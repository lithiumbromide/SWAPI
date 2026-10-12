---
title: "GetBuildOrientation Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetBuildOrientation"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetBuildOrientation.html"
---

# GetBuildOrientation Method (ISw3DPrinter)

Gets the selected build orientation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBuildOrientation() As swBuildOrientation_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As swBuildOrientation_e

value = instance.GetBuildOrientation()
```

### C#

```csharp
swBuildOrientation_e GetBuildOrientation()
```

### C++/CLI

```cpp
swBuildOrientation_e GetBuildOrientation();
```

### Return Value

Build orientation as defined in [swBuildOrientation_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swBuildOrientation_e.html)

## VBA Syntax

See [Sw3DPrinter::GetBuildOrientation](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetBuildOrientation.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCurrentOrientationTransform Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentOrientationTransform.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::SetBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetBuildOrientation.html)
[ISw3DPrinter::SetOrientationTransform Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetOrientationTransform.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

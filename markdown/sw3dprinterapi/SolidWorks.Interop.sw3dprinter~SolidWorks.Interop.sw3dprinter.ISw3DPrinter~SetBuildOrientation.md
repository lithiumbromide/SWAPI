---
title: "SetBuildOrientation Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetBuildOrientation"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetBuildOrientation.html"
---

# SetBuildOrientation Method (ISw3DPrinter)

Called when a user changes a build orientation on the Build Orientation tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetBuildOrientation( _
   ByVal BuildOrientation As swBuildOrientation_e _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim BuildOrientation As swBuildOrientation_e

instance.SetBuildOrientation(BuildOrientation)
```

### C#

```csharp
void SetBuildOrientation(
   swBuildOrientation_e BuildOrientation
)
```

### C++/CLI

```cpp
void SetBuildOrientation(
   swBuildOrientation_e BuildOrientation
)
```

### Parameters

- `BuildOrientation`: Build orientation as defined in [swBuildOrientation_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swBuildOrientation_e.html)

## VBA Syntax

See [Sw3DPrinter::SetBuildOrientation](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetBuildOrientation.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetBuildOrientation.html)
[ISw3DPrinter::GetCurrentOrientationTransform Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentOrientationTransform.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::SetOrientationTransform Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetOrientationTransform.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

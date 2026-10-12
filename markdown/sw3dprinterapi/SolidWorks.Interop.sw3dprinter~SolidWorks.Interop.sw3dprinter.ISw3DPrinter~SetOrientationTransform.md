---
title: "SetOrientationTransform Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetOrientationTransform"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetOrientationTransform.html"
---

# SetOrientationTransform Method (ISw3DPrinter)

Called when a user changes a preset orthogonal orientation or Z rotation value on the Build Orientation tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetOrientationTransform( _
   ByVal ModelOrientation As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim ModelOrientation As System.Object

instance.SetOrientationTransform(ModelOrientation)
```

### C#

```csharp
void SetOrientationTransform(
   System.object ModelOrientation
)
```

### C++/CLI

```cpp
void SetOrientationTransform(
   System.Object^ ModelOrientation
)
```

### Parameters

- `ModelOrientation`: Orientation transform

## VBA Syntax

See [Sw3DPrinter::SetOrientationTransform](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetOrientationTransform.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetBuildOrientation.html)
[ISw3DPrinter::GetCurrentOrientationTransform Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentOrientationTransform.html)
[ISw3DPrinter::GetDefaultBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetDefaultBuildOrientation.html)
[ISw3DPrinter::SetBuildOrientation Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetBuildOrientation.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

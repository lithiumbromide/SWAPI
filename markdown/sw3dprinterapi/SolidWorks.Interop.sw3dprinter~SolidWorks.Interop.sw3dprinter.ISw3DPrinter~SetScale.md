---
title: "SetScale Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetScale"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetScale.html"
---

# SetScale Method (ISw3DPrinter)

Called when a user sets the value by which to scale the document in the Scale box on the 3D Printer tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetScale( _
   ByVal Scale As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim Scale As System.Integer

instance.SetScale(Scale)
```

### C#

```csharp
void SetScale(
   System.int Scale
)
```

### C++/CLI

```cpp
void SetScale(
   System.int Scale
)
```

### Parameters

- `Scale`: Value by which to scale the document

## VBA Syntax

See [Sw3DPrinter::SetScale](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetScale.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetScale Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetScale.html)
[ISw3DPrinter::GetScaleParametersForActiveDocument Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetScaleParametersForActiveDocument.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

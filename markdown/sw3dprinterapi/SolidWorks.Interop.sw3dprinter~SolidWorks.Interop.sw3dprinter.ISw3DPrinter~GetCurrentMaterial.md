---
title: "GetCurrentMaterial Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetCurrentMaterial"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentMaterial.html"
---

# GetCurrentMaterial Method (ISw3DPrinter)

Gets the name of the selected material.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentMaterial() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As System.String

value = instance.GetCurrentMaterial()
```

### C#

```csharp
System.string GetCurrentMaterial()
```

### C++/CLI

```cpp
System.String^ GetCurrentMaterial();
```

### Return Value

Name of selected material

## VBA Syntax

See [Sw3DPrinter::GetCurrentMaterial](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetCurrentMaterial.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetAvailableMaterials Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetAvailableMaterials.html)
[ISw3DPrinter::SetCurrentMaterial Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetCurrentMaterial.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

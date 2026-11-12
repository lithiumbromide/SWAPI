---
title: "SetCurrentMaterial Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "SetCurrentMaterial"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetCurrentMaterial.html"
---

# SetCurrentMaterial Method (ISw3DPrinter)

Called when a user selects the name of a material in the Material box on the 3D Printer tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCurrentMaterial( _
   ByVal Material As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim Material As System.String

instance.SetCurrentMaterial(Material)
```

### C#

```csharp
void SetCurrentMaterial(
   System.string Material
)
```

### C++/CLI

```cpp
void SetCurrentMaterial(
   System.String^ Material
)
```

### Parameters

- `Material`: Name of material

## VBA Syntax

See [Sw3DPrinter::SetCurrentMaterial](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~SetCurrentMaterial.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetAvailableMaterials Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetAvailableMaterials.html)
[ISw3DPrinter::GetCurrentMaterial Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentMaterial.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

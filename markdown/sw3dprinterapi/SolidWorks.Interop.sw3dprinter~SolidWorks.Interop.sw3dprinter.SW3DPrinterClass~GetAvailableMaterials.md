---
title: "GetAvailableMaterials Method (SW3DPrinterClass)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "SW3DPrinterClass"
member: "GetAvailableMaterials"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass~GetAvailableMaterials.html"
---

# GetAvailableMaterials Method (SW3DPrinterClass)

See [ISw3DPrinter](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.ISw3DPrinter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetAvailableMaterials( _
   ByRef DefaultIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As SW3DPrinterClass
Dim DefaultIndex As System.Integer
Dim value As System.Object

value = instance.GetAvailableMaterials(DefaultIndex)
```

### C#

```csharp
public virtual System.object GetAvailableMaterials(
   out System.int DefaultIndex
)
```

### C++/CLI

```cpp
public:
virtual System.Object^ GetAvailableMaterials(
   [Out] System.int DefaultIndex
)
```

### Parameters

- `DefaultIndex`:

## See Also

[SW3DPrinterClass Class](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass.html)
[SW3DPrinterClass Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass_members.html)

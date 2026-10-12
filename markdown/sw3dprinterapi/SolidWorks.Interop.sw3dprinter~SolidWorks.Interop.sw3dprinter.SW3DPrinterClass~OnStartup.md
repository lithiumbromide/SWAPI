---
title: "OnStartup Method (SW3DPrinterClass)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "SW3DPrinterClass"
member: "OnStartup"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass~OnStartup.html"
---

# OnStartup Method (SW3DPrinterClass)

See [ISw3DPrinter](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.ISw3DPrinter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function OnStartup( _
   ByVal ActiveModel As System.Object _
) As swStartupResult_e
```

### Visual Basic (Usage)

```vb
Dim instance As SW3DPrinterClass
Dim ActiveModel As System.Object
Dim value As swStartupResult_e

value = instance.OnStartup(ActiveModel)
```

### C#

```csharp
public virtual swStartupResult_e OnStartup(
   System.object ActiveModel
)
```

### C++/CLI

```cpp
public:
virtual swStartupResult_e OnStartup(
   System.Object^ ActiveModel
)
```

### Parameters

- `ActiveModel`:

## See Also

[SW3DPrinterClass Class](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass.html)
[SW3DPrinterClass Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.SW3DPrinterClass_members.html)

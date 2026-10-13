---
title: "GetAvailableMaterials Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetAvailableMaterials"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetAvailableMaterials.html"
---

# GetAvailableMaterials Method (ISw3DPrinter)

Gets an array of strings that contain available material names, such as plastic, composite, etc., that the device can use.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAvailableMaterials( _
   ByRef DefaultIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim DefaultIndex As System.Integer
Dim value As System.Object

value = instance.GetAvailableMaterials(DefaultIndex)
```

### C#

```csharp
System.object GetAvailableMaterials(
   out System.int DefaultIndex
)
```

### C++/CLI

```cpp
System.Object^ GetAvailableMaterials(
   [Out] System.int DefaultIndex
)
```

### Parameters

- `DefaultIndex`: Index of default material

### Return Value

Array of strings that contains available material names

## VBA Syntax

See [Sw3DPrinter::GetAvailableMaterials](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetAvailableMaterials.html).

## Remarks

This method also returns the index of the default material.

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCurrentMaterial Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCurrentMaterial.html)
[ISw3DPrinter::SetCurrentMaterial Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~SetCurrentMaterial.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

---
title: "GetCalculatedVolume Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetCalculatedVolume"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedVolume.html"
---

# GetCalculatedVolume Method (ISw3DPrinter)

Gets the calculated volume of the current document in current document units, taking into account scale and other parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCalculatedVolume() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As System.String

value = instance.GetCalculatedVolume()
```

### C#

```csharp
System.string GetCalculatedVolume()
```

### C++/CLI

```cpp
System.String^ GetCalculatedVolume();
```

### Return Value

Calculated volume of the current document in current document units

## VBA Syntax

See [Sw3DPrinter::GetCalculatedVolume](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetCalculatedVolume.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCalculatedBoundingVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBoundingVolume.html)
[ISw3DPrinter::GetCalculatedBuildTime Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBuildTime.html)
[ISw3DPrinter::GetCalculatedCost Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedCost.html)
[ISw3DPrinter::GetCalculatedSurfaceArea Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedSurfaceArea.html)
[ISw3DPrinter::OnUpdateStatistics Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnUpdateStatistics.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

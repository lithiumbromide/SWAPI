---
title: "OnUpdateStatistics Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "OnUpdateStatistics"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnUpdateStatistics.html"
---

# OnUpdateStatistics Method (ISw3DPrinter)

Called when a user clicks the Update Statistics button on the 3D Printer tab and changes the build statistics.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnUpdateStatistics() As swDataChangeResult_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As swDataChangeResult_e

value = instance.OnUpdateStatistics()
```

### C#

```csharp
swDataChangeResult_e OnUpdateStatistics()
```

### C++/CLI

```cpp
swDataChangeResult_e OnUpdateStatistics();
```

### Return Value

Status of update as defined in [swDataChangeResult_e](SOLIDWORKS.Interop.sw3dprinter~SOLIDWORKS.Interop.sw3dprinter.swDataChangeResult_e.html)

## VBA Syntax

See [Sw3DPrinter::OnUpdateStatistics](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~OnUpdateStatistics.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCalculatedBoundingVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBoundingVolume.html)
[ISw3DPrinter::GetCalculatedBuildTime Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBuildTime.html)
[ISw3DPrinter::GetCalculatedCost Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedCost.html)
[ISw3DPrinter::GetCalculatedSurfaceArea Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedSurfaceArea.html)
[ISw3DPrinter::GetCalculatedVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedVolume.html)
[ISw3DPrinter::OnAdvancedSettings Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnAdvancedSettings.html)
[ISw3DPrinter::OnCancel Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnCancel.html)
[ISw3DPrinter::OnOk Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnOk.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

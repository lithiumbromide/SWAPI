---
title: "GetCalculatedBoundingVolume Method (ISw3DPrinter)"
project: "SOLIDWORKS 3D Printer API Help"
interface: "ISw3DPrinter"
member: "GetCalculatedBoundingVolume"
kind: "method"
source: "sw3dprinterapi/SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBoundingVolume.html"
---

# GetCalculatedBoundingVolume Method (ISw3DPrinter)

Gets the dimension of the calculated bounding volume in document units.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCalculatedBoundingVolume() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISw3DPrinter
Dim value As System.String

value = instance.GetCalculatedBoundingVolume()
```

### C#

```csharp
System.string GetCalculatedBoundingVolume()
```

### C++/CLI

```cpp
System.String^ GetCalculatedBoundingVolume();
```

### Return Value

Dimension of calculated bounding volume

## VBA Syntax

See [Sw3DPrinter::GetCalculatedBoundingVolume](ms-its:sw3dprinterapivb6.chm::/sw3dprinter~Sw3DPrinter~GetCalculatedBoundingVolume.html).

## See Also

[ISw3DPrinter Interface](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter.html)
[ISw3DPrinter Members](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter_members.html)
[ISw3DPrinter::GetCalculatedBuildTime Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedBuildTime.html)
[ISw3DPrinter::GetCalculatedCost Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedCost.html)
[ISw3DPrinter::GetCalculatedSurfaceArea Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedSurfaceArea.html)
[ISw3DPrinter::GetCalculatedVolume Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~GetCalculatedVolume.html)
[ISw3DPrinter::OnUpdateStatistics Method](SolidWorks.Interop.sw3dprinter~SolidWorks.Interop.sw3dprinter.ISw3DPrinter~OnUpdateStatistics.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

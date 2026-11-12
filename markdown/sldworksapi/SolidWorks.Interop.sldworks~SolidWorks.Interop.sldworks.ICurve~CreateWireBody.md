---
title: "CreateWireBody Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "CreateWireBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateWireBody.html"
---

# CreateWireBody Method (ICurve)

Creates a wire body from this curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateWireBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As Body2

value = instance.CreateWireBody()
```

### C#

```csharp
Body2 CreateWireBody()
```

### C++/CLI

```cpp
Body2^ CreateWireBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the newly [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Curve::CreateWireBody](ms-its:sldworksapivb6.chm::/sldworks~Curve~CreateWireBody.html).

## Remarks

Wire bodies contain wires, loops, coedges, edges, and vertices. Wires typically represent profiles, construction lines, and center lines of swept shapes. Wires can also represent wire frames that, when surfaced, form shells.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[IEdge::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~CreateWireBody.html)
[IImportedCurveFeatureData::SetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~SetBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

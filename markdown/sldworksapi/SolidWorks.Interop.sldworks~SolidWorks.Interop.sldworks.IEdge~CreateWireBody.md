---
title: "CreateWireBody Method (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "CreateWireBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~CreateWireBody.html"
---

# CreateWireBody Method (IEdge)

Creates a wire body from this edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateWireBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
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

Pointer to the newly created [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

## VBA Syntax

See [Edge::CreateWireBody](ms-its:sldworksapivb6.chm::/sldworks~Edge~CreateWireBody.html).

## Remarks

Wire bodies contain wires, loops, coedges, edges, and vertices. Wires typically represent profiles, construction lines, and center lines of swept shapes. Wires can also represent wire frames that, when surfaced, form shells.

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[ICurve::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateWireBody.html)
[IImportedCurveFeatureData::SetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~SetBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

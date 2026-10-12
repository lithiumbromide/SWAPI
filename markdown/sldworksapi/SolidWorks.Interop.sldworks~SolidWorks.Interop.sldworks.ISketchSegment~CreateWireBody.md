---
title: "CreateWireBody Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "CreateWireBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~CreateWireBody.html"
---

# CreateWireBody Method (ISketchSegment)

Creates a wire body using the selected sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateWireBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
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

[Body2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [SketchSegment::CreateWireBody](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~CreateWireBody.html).

## Remarks

Wire bodies contain wires, loops, coedges, edges, and vertices. Wires typically represent profiles, construction lines, and center lines of swept shapes. Wires can also represent wire frames that, when surfaced, form shells.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

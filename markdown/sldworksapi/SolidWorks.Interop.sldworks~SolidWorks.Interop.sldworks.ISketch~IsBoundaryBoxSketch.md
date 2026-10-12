---
title: "IsBoundaryBoxSketch Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IsBoundaryBoxSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IsBoundaryBoxSketch.html"
---

# IsBoundaryBoxSketch Method (ISketch)

Determines whether the sketch is a boundary box.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBoundaryBoxSketch() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Boolean

value = instance.IsBoundaryBoxSketch()
```

### C#

```csharp
System.bool IsBoundaryBoxSketch()
```

### C++/CLI

```cpp
System.bool IsBoundaryBoxSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sketch is a boundary box, false if not

## VBA Syntax

See [Sketch::IsBoundaryBoxSketch](ms-its:sldworksapivb6.chm::/sldworks~Sketch~IsBoundaryBoxSketch.html).

## Examples

[Is Selected Feature a Boundary Box Sketch (C#)](Is_Selected_Feature_a_Boundary_Box_Sketch_Example_CSharp.htm)
[Is Selected Feature a Boundary Box Sektch (VB.NET)](Is_Selected_Feature_a_Boundary_Box_Sketch_Example_VBNET.htm)
[Is Selected Feature a Boundary Box Sketch (VBA)](Is_Selected_Feature_a_Boundary_Box_Sketch_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0

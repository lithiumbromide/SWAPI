---
title: "GetRadius Method (ISketchArc)"
project: "SOLIDWORKS API Help"
interface: "ISketchArc"
member: "GetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetRadius.html"
---

# GetRadius Method (ISketchArc)

Gets the radius of the arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRadius() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchArc
Dim value As System.Double

value = instance.GetRadius()
```

### C#

```csharp
System.double GetRadius()
```

### C++/CLI

```cpp
System.double GetRadius();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Radius in meters of the arc

## VBA Syntax

See [SketchArc::GetRadius](ms-its:sldworksapivb6.chm::/sldworks~SketchArc~GetRadius.html).

## Examples

See the [ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html) examples.

## Examples

[Create Imported Surface Body From Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

## See Also

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html)
[ISketchArc::SetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~SetRadius.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

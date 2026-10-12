---
title: "GetNormalVector Method (ISketchArc)"
project: "SOLIDWORKS API Help"
interface: "ISketchArc"
member: "GetNormalVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetNormalVector.html"
---

# GetNormalVector Method (ISketchArc)

Gets the normal to the arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNormalVector() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchArc
Dim value As System.Object

value = instance.GetNormalVector()
```

### C#

```csharp
System.object GetNormalVector()
```

### C++/CLI

```cpp
System.Object^ GetNormalVector();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 3 doubles (x,y,z), which represents the unit vector normal to the arc

## VBA Syntax

See [SketchArc::GetNormalVector](ms-its:sldworksapivb6.chm::/sldworks~SketchArc~GetNormalVector.html).

## Examples

See the [ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html) examples.

## Examples

[Create Imported Surface Body From Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

## See Also

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html)
[ISketchArc::IGetNormalVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IGetNormalVector.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0

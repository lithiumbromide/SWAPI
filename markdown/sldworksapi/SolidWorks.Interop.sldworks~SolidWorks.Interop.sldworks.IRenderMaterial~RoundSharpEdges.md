---
title: "RoundSharpEdges Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "RoundSharpEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RoundSharpEdges.html"
---

# RoundSharpEdges Property (IRenderMaterial)

Gets or sets the value by which to round sharp edges when rendering a model using a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoundSharpEdges As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.RoundSharpEdges = value

value = instance.RoundSharpEdges
```

### C#

```csharp
System.double RoundSharpEdges {get; set;}
```

### C++/CLI

```cpp
property System.double RoundSharpEdges {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value by which to round sharp edges

## VBA Syntax

See [RenderMaterial::RouundSharpEdges](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~RoundSharpEdges.html).

## Examples

[Get Surface-finish Image Path and File Name (C#)](Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm)
[Get Surface-finish Image Path and File Name (VB.NET)](Get_Surface-finish_Image_Path_and_Filename_Example_VBNET.htm)
[Get Surface-finish Image Path and File Name (VBA)](Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm)

## Remarks

This method:

- is only available when a ray-trace rendering engine is loaded.
- does not change model geometry.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0

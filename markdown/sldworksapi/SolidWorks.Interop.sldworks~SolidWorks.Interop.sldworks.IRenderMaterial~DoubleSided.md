---
title: "DoubleSided Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "DoubleSided"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~DoubleSided.html"
---

# DoubleSided Property (IRenderMaterial)

Gets or sets whether to enable shading from both sides of a surface when rendering a model using a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Property DoubleSided As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.DoubleSided = value

value = instance.DoubleSided
```

### C#

```csharp
System.bool DoubleSided {get; set;}
```

### C++/CLI

```cpp
property System.bool DoubleSided {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable shading from both sides, false to not

## VBA Syntax

See [RenderMaterial::DoubleSided](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~DoubleSided.html).

## Examples

[Get Surface-finish Image Path and File Name (C#)](Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm)
[Get Surface-finish Image Path and File Name (VB.NET)](Get_Surface-finish_Image_Path_and_Filename_Example_VBNET.htm)
[Get Surface-finish Image Path and File Name (VBA)](Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm)

## Remarks

This method is only available when a ray-trace rendering engine is loaded.

**NOTES:**

- When this property is disabled, surfaces that do not face the camera seem invisible.
- Double-sided surfaces can cause rendering errors. Use sparingly.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0

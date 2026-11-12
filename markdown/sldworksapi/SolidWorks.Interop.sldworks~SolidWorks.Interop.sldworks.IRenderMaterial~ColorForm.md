---
title: "ColorForm Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "ColorForm"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ColorForm.html"
---

# ColorForm Property (IRenderMaterial)

Gets or sets the number of colors required to describe the appearance .

## Syntax

### Visual Basic (Declaration)

```vb
Property ColorForm As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.ColorForm = value

value = instance.ColorForm
```

### C#

```csharp
System.int ColorForm {get; set;}
```

### C++/CLI

```cpp
property System.int ColorForm {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of colors as defined by [swRenderMaterialColorForms_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRenderMaterialColorForms_e.html)

## VBA Syntax

See [RenderMaterial::ColorForm](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~ColorForm.html).

## Remarks

For example, blue glass is defined by two colors. To see the corresponding user-interface controls, open a model to which the blue glass appearance has been applied. Edit the blue glass appearance to open the Appearances PropertyManager page. Two color controls, Current Color1 and Current Color2, are displayed under Color.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

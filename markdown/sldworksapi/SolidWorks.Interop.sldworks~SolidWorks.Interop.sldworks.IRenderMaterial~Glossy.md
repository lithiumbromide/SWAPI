---
title: "Glossy Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Glossy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Glossy.html"
---

# Glossy Property (IRenderMaterial)

Gets or sets the specular factor of the lights reflected by the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Glossy As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Glossy = value

value = instance.Glossy
```

### C#

```csharp
System.double Glossy {get; set;}
```

### C++/CLI

```cpp
property System.double Glossy {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Specular factor of the lights reflected by the appearance

## VBA Syntax

See [RenderMaterial::Glossy](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Glossy.html).

## Remarks

Increasing Glossy makes reflections more visible.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

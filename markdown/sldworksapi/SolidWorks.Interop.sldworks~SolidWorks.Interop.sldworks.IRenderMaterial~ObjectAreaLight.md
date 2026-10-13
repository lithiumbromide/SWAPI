---
title: "ObjectAreaLight Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "ObjectAreaLight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ObjectAreaLight.html"
---

# ObjectAreaLight Property (IRenderMaterial)

Gets or sets whether the appearance is an object area light or whether it has realistic falloff, or both.

## Syntax

### Visual Basic (Declaration)

```vb
Property ObjectAreaLight As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.ObjectAreaLight = value

value = instance.ObjectAreaLight
```

### C#

```csharp
System.int ObjectAreaLight {get; set;}
```

### C++/CLI

```cpp
property System.int ObjectAreaLight {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the appearance has an object area light or it has realistic falloff, or both; false if it does not

## VBA Syntax

See [RenderMaterial::ObjectAreaLight](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~ObjectAreaLight.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

---
title: "AccurateReflections Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "AccurateReflections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AccurateReflections.html"
---

# AccurateReflections Property (IRenderMaterial)

Selects or clears the Accurate reflections (slower) setting, which controls the level of surface reflections, for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property AccurateReflections As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.AccurateReflections = value

value = instance.AccurateReflections
```

### C#

```csharp
System.bool AccurateReflections {get; set;}
```

### C++/CLI

```cpp
property System.bool AccurateReflections {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to select the Accurate reflections (slower) setting, false to clear it

## VBA Syntax

See [RenderMaterial::AccurateReflections](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~AccurateReflections.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

---
title: "SetUDirection2 Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SetUDirection2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection2.html"
---

# SetUDirection2 Method (IRenderMaterial)

Sets the U direction of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUDirection2( _
   ByVal UDir_X As System.Double, _
   ByVal UDir_Y As System.Double, _
   ByVal UDir_Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim UDir_X As System.Double
Dim UDir_Y As System.Double
Dim UDir_Z As System.Double

instance.SetUDirection2(UDir_X, UDir_Y, UDir_Z)
```

### C#

```csharp
void SetUDirection2(
   System.double UDir_X,
   System.double UDir_Y,
   System.double UDir_Z
)
```

### C++/CLI

```cpp
void SetUDirection2(
   System.double UDir_X,
   System.double UDir_Y,
   System.double UDir_Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UDir_X`: X coordinate of the U direction
- `UDir_Y`: Y coordinate of the U direction
- `UDir_Z`: Z coordinate of the U direction

## VBA Syntax

See [RenderMaterial::SetUDirection2](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SetUDirection2.html).

## Remarks

To specify the U direction in the X direction, set:

1. UDir_X to 1.0.
2. UDir_Y to 0.0.
3. UDir_Z to 0.0.

Call [IRenderMaterial::SetVDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SetVDirection2.html) to set the V direction of the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetUDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2.html)
[IRenderMaterial::GetVDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetVDirection2.html)

## Availability

SOLIDWORKS 2013 SP05, Revision 21.5

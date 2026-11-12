---
title: "GetUDirection2 Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetUDirection2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetUDirection2.html"
---

# GetUDirection2 Method (IRenderMaterial)

Gets the U direction of the texture-based appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetUDirection2( _
   ByRef UDir_X As System.Double, _
   ByRef UDir_Y As System.Double, _
   ByRef UDir_Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim UDir_X As System.Double
Dim UDir_Y As System.Double
Dim UDir_Z As System.Double

instance.GetUDirection2(UDir_X, UDir_Y, UDir_Z)
```

### C#

```csharp
void GetUDirection2(
   out System.double UDir_X,
   out System.double UDir_Y,
   out System.double UDir_Z
)
```

### C++/CLI

```cpp
void GetUDirection2(
   [Out] System.double UDir_X,
   [Out] System.double UDir_Y,
   [Out] System.double UDir_Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UDir_X`: X coordinate of the U direction
- `UDir_Y`: Y coordinate of the U direction
- `UDir_Z`: Z coordinate of the U direction

## VBA Syntax

See [RenderMaterial::GetUDirection2](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetUDirection2.html).

## Examples

See [IRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) examples.

## Remarks

Call [IRenderMaterial::GetVDirection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetVDirection2.html) to get the V direction of the appearance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::SetUDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetUDirection2.html)
[IRenderMaterial::SetVDirection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetVDirection2.html)

## Availability

SOLIDWORKS 2013 SP05, Revision 21.5

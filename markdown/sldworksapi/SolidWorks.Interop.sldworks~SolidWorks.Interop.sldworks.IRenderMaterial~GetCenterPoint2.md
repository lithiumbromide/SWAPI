---
title: "GetCenterPoint2 Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetCenterPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint2.html"
---

# GetCenterPoint2 Method (IRenderMaterial)

Gets the center point of the mapping for texture-based appearances.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetCenterPoint2( _
   ByRef CenterPt_X As System.Double, _
   ByRef CenterPt_Y As System.Double, _
   ByRef CenterPt_Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim CenterPt_X As System.Double
Dim CenterPt_Y As System.Double
Dim CenterPt_Z As System.Double

instance.GetCenterPoint2(CenterPt_X, CenterPt_Y, CenterPt_Z)
```

### C#

```csharp
void GetCenterPoint2(
   out System.double CenterPt_X,
   out System.double CenterPt_Y,
   out System.double CenterPt_Z
)
```

### C++/CLI

```cpp
void GetCenterPoint2(
   [Out] System.double CenterPt_X,
   [Out] System.double CenterPt_Y,
   [Out] System.double CenterPt_Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterPt_X`: X coordinate of the center point
- `CenterPt_Y`: Y coordinate of the center point
- `CenterPt_Z`: Z coordinate of the center point

## VBA Syntax

See [RenderMaterial::GetCenterPoint2](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetCenterPoint2.html).

## Examples

See [IRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) examples.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::SetCenterPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint2.html)

## Availability

SOLIDWORKS 2013 SP05, Revision 21.5

---
title: "SetCenterPoint2 Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SetCenterPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint2.html"
---

# SetCenterPoint2 Method (IRenderMaterial)

Sets the center point of the mapping for texture-based appearances.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCenterPoint2( _
   ByVal CenterPt_X As System.Double, _
   ByVal CenterPt_Y As System.Double, _
   ByVal CenterPt_Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim CenterPt_X As System.Double
Dim CenterPt_Y As System.Double
Dim CenterPt_Z As System.Double

instance.SetCenterPoint2(CenterPt_X, CenterPt_Y, CenterPt_Z)
```

### C#

```csharp
void SetCenterPoint2(
   System.double CenterPt_X,
   System.double CenterPt_Y,
   System.double CenterPt_Z
)
```

### C++/CLI

```cpp
void SetCenterPoint2(
   System.double CenterPt_X,
   System.double CenterPt_Y,
   System.double CenterPt_Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterPt_X`: X coordinate of the center point
- `CenterPt_Y`: Y coordinate of the center point
- `CenterPt_Z`: Z coordinate of the center point

## VBA Syntax

See [RenderMaterial::SetCenterPoint2](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SetCenterPoint2.html).

## Remarks

This method is required to properly position a texture-based appearance (e.g., if you need a specific corner of a face to have the black square of a checkered-pattern appearance).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetCenterPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint2.html)

## Availability

SOLIDWORKS 2013 SP05, Revision 21.5

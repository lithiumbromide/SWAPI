---
title: "MoldUndercutDetect2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "MoldUndercutDetect2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoldUndercutDetect2.html"
---

# MoldUndercutDetect2 Method (IFeatureManager)

Detects trapped, also called undercut, areas in a model that cannot be ejected from the mold.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MoldUndercutDetect2( _
   ByVal ColUndercut1 As System.Integer, _
   ByVal ColUndercut2 As System.Integer, _
   ByVal ColOccluded As System.Integer, _
   ByVal ColStraddle As System.Integer, _
   ByVal ColBase As System.Integer, _
   ByVal BCoordInput As System.Boolean, _
   ByVal Dx As System.Double, _
   ByVal Dy As System.Double, _
   ByVal Dz As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim ColUndercut1 As System.Integer
Dim ColUndercut2 As System.Integer
Dim ColOccluded As System.Integer
Dim ColStraddle As System.Integer
Dim ColBase As System.Integer
Dim BCoordInput As System.Boolean
Dim Dx As System.Double
Dim Dy As System.Double
Dim Dz As System.Double

instance.MoldUndercutDetect2(ColUndercut1, ColUndercut2, ColOccluded, ColStraddle, ColBase, BCoordInput, Dx, Dy, Dz)
```

### C#

```csharp
void MoldUndercutDetect2(
   System.int ColUndercut1,
   System.int ColUndercut2,
   System.int ColOccluded,
   System.int ColStraddle,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
)
```

### C++/CLI

```cpp
void MoldUndercutDetect2(
   System.int ColUndercut1,
   System.int ColUndercut2,
   System.int ColOccluded,
   System.int ColStraddle,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColUndercut1`: Value (COLORREF type) that specifies the color for the faces invisible from one direction that form an undercut
- `ColUndercut2`: Value (COLORREF type) that specifies the color for the faces invisible from a second direction that form an undercut
- `ColOccluded`: Value (COLORREF type) that specifies the color for the faces invisible from both directions that form an undercut
- `ColStraddle`: Value (COLORREF type) that specifies the color for the faces with draft in both directions that form an undercut
- `ColBase`: Value (COLORREF type) that specifies the color for the faces that do not form undercuts; that is, all faces except the undercut faces
- `BCoordInput`: True to enable coordinate input to control the direction of pull, false to not
- `Dx`: x coordinate to control the direction of pull
- `Dy`: y coordinate to control the direction of pull
- `Dz`: z coordinate to control the direction of pull

## VBA Syntax

See [FeatureManager::MoldUndercutDetect2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~MoldUndercutDetect2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

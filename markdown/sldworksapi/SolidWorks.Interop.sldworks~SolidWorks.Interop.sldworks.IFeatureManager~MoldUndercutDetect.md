---
title: "MoldUndercutDetect Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "MoldUndercutDetect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoldUndercutDetect.html"
---

# MoldUndercutDetect Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::MoldUndercutDetect2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~MoldUndercutDetect2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub MoldUndercutDetect( _
   ByVal ColUndercut As System.Integer, _
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
Dim ColUndercut As System.Integer
Dim ColBase As System.Integer
Dim BCoordInput As System.Boolean
Dim Dx As System.Double
Dim Dy As System.Double
Dim Dz As System.Double

instance.MoldUndercutDetect(ColUndercut, ColBase, BCoordInput, Dx, Dy, Dz)
```

### C#

```csharp
void MoldUndercutDetect(
   System.int ColUndercut,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
)
```

### C++/CLI

```cpp
void MoldUndercutDetect(
   System.int ColUndercut,
   System.int ColBase,
   System.bool BCoordInput,
   System.double Dx,
   System.double Dy,
   System.double Dz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColUndercut`:
- `ColBase`:
- `BCoordInput`:
- `Dx`:
- `Dy`:
- `Dz`:

## VBA Syntax

See [FeatureManager::MoldUndercutDetect](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~MoldUndercutDetect.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

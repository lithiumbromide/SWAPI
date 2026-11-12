---
title: "MakeStyledCurves Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "MakeStyledCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MakeStyledCurves.html"
---

# MakeStyledCurves Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::MakeStyledCurves2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~MakeStyledCurves2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub MakeStyledCurves( _
   ByVal Tol As System.Double, _
   ByVal Mode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Tol As System.Double
Dim Mode As System.Integer

instance.MakeStyledCurves(Tol, Mode)
```

### C#

```csharp
void MakeStyledCurves(
   System.double Tol,
   System.int Mode
)
```

### C++/CLI

```cpp
void MakeStyledCurves(
   System.double Tol,
   System.int Mode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Tol`:
- `Mode`:

## VBA Syntax

See [FeatureManager::MakeStyledCurves](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~MakeStyledCurves.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

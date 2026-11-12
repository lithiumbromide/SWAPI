---
title: "FeatureCircularPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureCircularPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern.html"
---

# FeatureCircularPattern Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCircularPattern2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureCircularPattern( _
   ByVal Num As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal DName As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Num As System.Integer
Dim Spacing As System.Double
Dim FlipDir As System.Boolean
Dim DName As System.String
Dim value As Feature

value = instance.FeatureCircularPattern(Num, Spacing, FlipDir, DName)
```

### C#

```csharp
Feature FeatureCircularPattern(
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.string DName
)
```

### C++/CLI

```cpp
Feature^ FeatureCircularPattern(
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.String^ DName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Num`:
- `Spacing`:
- `FlipDir`:
- `DName`:

## VBA Syntax

See [FeatureManager::FeatureCircularPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureCircularPattern.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

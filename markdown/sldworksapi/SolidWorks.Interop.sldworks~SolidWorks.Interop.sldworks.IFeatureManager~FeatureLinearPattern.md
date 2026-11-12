---
title: "FeatureLinearPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureLinearPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLinearPattern.html"
---

# FeatureLinearPattern Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::FeatureLinearPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLinearPattern2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureLinearPattern( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal FlipDir1 As System.Boolean, _
   ByVal FlipDir2 As System.Boolean, _
   ByVal DName1 As System.String, _
   ByVal DName2 As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Num1 As System.Integer
Dim Spacing1 As System.Double
Dim Num2 As System.Integer
Dim Spacing2 As System.Double
Dim FlipDir1 As System.Boolean
Dim FlipDir2 As System.Boolean
Dim DName1 As System.String
Dim DName2 As System.String
Dim value As Feature

value = instance.FeatureLinearPattern(Num1, Spacing1, Num2, Spacing2, FlipDir1, FlipDir2, DName1, DName2)
```

### C#

```csharp
Feature FeatureLinearPattern(
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.string DName1,
   System.string DName2
)
```

### C++/CLI

```cpp
Feature^ FeatureLinearPattern(
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.String^ DName1,
   System.String^ DName2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Num1`:
- `Spacing1`:
- `Num2`:
- `Spacing2`:
- `FlipDir1`:
- `FlipDir2`:
- `DName1`:
- `DName2`:

## VBA Syntax

See [FeatureManager::FeatureLinearPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureLinearPattern.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

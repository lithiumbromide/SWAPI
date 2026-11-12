---
title: "FeatureLinearPattern Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureLinearPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureLinearPattern.html"
---

# FeatureLinearPattern Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureLinearPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLinearPattern2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureLinearPattern( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal FlipDir1 As System.Boolean, _
   ByVal FlipDir2 As System.Boolean, _
   ByVal DName1 As System.String, _
   ByVal DName2 As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Num1 As System.Integer
Dim Spacing1 As System.Double
Dim Num2 As System.Integer
Dim Spacing2 As System.Double
Dim FlipDir1 As System.Boolean
Dim FlipDir2 As System.Boolean
Dim DName1 As System.String
Dim DName2 As System.String

instance.FeatureLinearPattern(Num1, Spacing1, Num2, Spacing2, FlipDir1, FlipDir2, DName1, DName2)
```

### C#

```csharp
void FeatureLinearPattern(
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
void FeatureLinearPattern(
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

See [ModelDoc2::FeatureLinearPattern](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureLinearPattern.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

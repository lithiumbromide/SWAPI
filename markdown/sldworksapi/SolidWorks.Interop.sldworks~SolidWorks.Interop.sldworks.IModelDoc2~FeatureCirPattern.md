---
title: "FeatureCirPattern Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureCirPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureCirPattern.html"
---

# FeatureCirPattern Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCircularPattern2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureCirPattern( _
   ByVal Num As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal DName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Num As System.Integer
Dim Spacing As System.Double
Dim FlipDir As System.Boolean
Dim DName As System.String

instance.FeatureCirPattern(Num, Spacing, FlipDir, DName)
```

### C#

```csharp
void FeatureCirPattern(
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.string DName
)
```

### C++/CLI

```cpp
void FeatureCirPattern(
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

See [ModelDoc2::FeatureCirPattern](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureCirPattern.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

---
title: "FeatureCirPattern Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureCirPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureCirPattern.html"
---

# FeatureCirPattern Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureCirPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureCirPattern.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::FeatureCirPattern](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureCirPattern.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)

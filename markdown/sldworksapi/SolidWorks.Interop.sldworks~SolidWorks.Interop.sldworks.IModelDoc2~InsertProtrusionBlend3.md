---
title: "InsertProtrusionBlend3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertProtrusionBlend3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertProtrusionBlend3.html"
---

# InsertProtrusionBlend3 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertProtrusionBlend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionBlend.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertProtrusionBlend3( _
   ByVal Closed As System.Boolean, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal TessToleranceFactor As System.Double, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Closed As System.Boolean
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean
Dim TessToleranceFactor As System.Double
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short

instance.InsertProtrusionBlend3(Closed, KeepTangency, ForceNonRational, TessToleranceFactor, StartMatchingType, EndMatchingType)
```

### C#

```csharp
void InsertProtrusionBlend3(
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.double TessToleranceFactor,
   System.short StartMatchingType,
   System.short EndMatchingType
)
```

### C++/CLI

```cpp
void InsertProtrusionBlend3(
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.double TessToleranceFactor,
   System.short StartMatchingType,
   System.short EndMatchingType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Closed`:
- `KeepTangency`:
- `ForceNonRational`:
- `TessToleranceFactor`:
- `StartMatchingType`:
- `EndMatchingType`:

## VBA Syntax

See [ModelDoc2::InsertProtrusionBlend3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertProtrusionBlend3.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

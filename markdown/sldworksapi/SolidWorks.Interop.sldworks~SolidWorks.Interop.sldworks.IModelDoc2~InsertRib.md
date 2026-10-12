---
title: "InsertRib Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertRib"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRib.html"
---

# InsertRib Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::InsertRib2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertRib2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertRib( _
   ByVal Is2Sided As System.Boolean, _
   ByVal ReverseThicknessDir As System.Boolean, _
   ByVal Thickness As System.Double, _
   ByVal ReferenceEdgeIndex As System.Integer, _
   ByVal ReverseMaterialDir As System.Boolean, _
   ByVal IsDrafted As System.Boolean, _
   ByVal DraftOutward As System.Boolean, _
   ByVal DraftAngle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Is2Sided As System.Boolean
Dim ReverseThicknessDir As System.Boolean
Dim Thickness As System.Double
Dim ReferenceEdgeIndex As System.Integer
Dim ReverseMaterialDir As System.Boolean
Dim IsDrafted As System.Boolean
Dim DraftOutward As System.Boolean
Dim DraftAngle As System.Double

instance.InsertRib(Is2Sided, ReverseThicknessDir, Thickness, ReferenceEdgeIndex, ReverseMaterialDir, IsDrafted, DraftOutward, DraftAngle)
```

### C#

```csharp
void InsertRib(
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle
)
```

### C++/CLI

```cpp
void InsertRib(
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Is2Sided`:
- `ReverseThicknessDir`:
- `Thickness`:
- `ReferenceEdgeIndex`:
- `ReverseMaterialDir`:
- `IsDrafted`:
- `DraftOutward`:
- `DraftAngle`:

## VBA Syntax

See [ModelDoc2::InsertRib](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertRib.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

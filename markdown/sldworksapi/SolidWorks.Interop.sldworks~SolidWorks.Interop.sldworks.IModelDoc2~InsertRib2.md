---
title: "InsertRib2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertRib2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRib2.html"
---

# InsertRib2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertRib](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRib.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertRib2( _
   ByVal Is2Sided As System.Boolean, _
   ByVal ReverseThicknessDir As System.Boolean, _
   ByVal Thickness As System.Double, _
   ByVal ReferenceEdgeIndex As System.Integer, _
   ByVal ReverseMaterialDir As System.Boolean, _
   ByVal IsDrafted As System.Boolean, _
   ByVal DraftOutward As System.Boolean, _
   ByVal DraftAngle As System.Double, _
   ByVal IsNormToSketch As System.Boolean _
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
Dim IsNormToSketch As System.Boolean

instance.InsertRib2(Is2Sided, ReverseThicknessDir, Thickness, ReferenceEdgeIndex, ReverseMaterialDir, IsDrafted, DraftOutward, DraftAngle, IsNormToSketch)
```

### C#

```csharp
void InsertRib2(
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle,
   System.bool IsNormToSketch
)
```

### C++/CLI

```cpp
void InsertRib2(
   System.bool Is2Sided,
   System.bool ReverseThicknessDir,
   System.double Thickness,
   System.int ReferenceEdgeIndex,
   System.bool ReverseMaterialDir,
   System.bool IsDrafted,
   System.bool DraftOutward,
   System.double DraftAngle,
   System.bool IsNormToSketch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Is2Sided`: True if the rib is double-sided rib, false if the rib is single sided; a double-sided rib thickens on both sides of the sketch
- `ReverseThicknessDir`: For single-sided ribs, the direction thickened is the opposite side of the sketch normal
- `Thickness`: Rib thickness
- `ReferenceEdgeIndex`: Edge in the sketch to us to determine the material direction and for draft reference; when the rib is drafted, the mid point of this edge maintains the thickness value; other points on the rib may have a different thickness due to the draft
- `ReverseMaterialDir`: Which direction the rib has material; it is on one side or the order side of the reference edge base on this flag
- `IsDrafted`: True if the rib is drafted, false if not
- `DraftOutward`: True to draft outwards, false to not
- `DraftAngle`: Draft angle to apply to the rib
- `IsNormToSketch`: True if the rib is normal to the sketch, false if the rib is parallel to the sketch

## VBA Syntax

See [ModelDoc2::InsertRib2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertRib2.html).

## Remarks

This method supports multibody parts. You must select the input body by calling [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and setting its Mark argument to 1 before calling this method.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

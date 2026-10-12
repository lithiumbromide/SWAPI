---
title: "AddCornerReliefType Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "AddCornerReliefType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefType.html"
---

# AddCornerReliefType Method (IFeatureManager)

Specifies the type of corner relief to apply to the specified corner of the selected sheet metal body.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCornerReliefType( _
   ByVal CornerIndex As System.Integer, _
   ByVal ReliefType As System.Integer, _
   ByVal Length1 As System.Double, _
   ByVal Length2 As System.Double, _
   ByVal Length3 As System.Double, _
   ByVal CenterOnBendLines As System.Boolean, _
   ByVal RatioToThickness As System.Boolean, _
   ByVal TangentToBend As System.Boolean, _
   ByVal AddFilletedCorners As System.Boolean, _
   ByVal NarrowCorner As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim CornerIndex As System.Integer
Dim ReliefType As System.Integer
Dim Length1 As System.Double
Dim Length2 As System.Double
Dim Length3 As System.Double
Dim CenterOnBendLines As System.Boolean
Dim RatioToThickness As System.Boolean
Dim TangentToBend As System.Boolean
Dim AddFilletedCorners As System.Boolean
Dim NarrowCorner As System.Boolean
Dim value As System.Boolean

value = instance.AddCornerReliefType(CornerIndex, ReliefType, Length1, Length2, Length3, CenterOnBendLines, RatioToThickness, TangentToBend, AddFilletedCorners, NarrowCorner)
```

### C#

```csharp
System.bool AddCornerReliefType(
   System.int CornerIndex,
   System.int ReliefType,
   System.double Length1,
   System.double Length2,
   System.double Length3,
   System.bool CenterOnBendLines,
   System.bool RatioToThickness,
   System.bool TangentToBend,
   System.bool AddFilletedCorners,
   System.bool NarrowCorner
)
```

### C++/CLI

```cpp
System.bool AddCornerReliefType(
   System.int CornerIndex,
   System.int ReliefType,
   System.double Length1,
   System.double Length2,
   System.double Length3,
   System.bool CenterOnBendLines,
   System.bool RatioToThickness,
   System.bool TangentToBend,
   System.bool AddFilletedCorners,
   System.bool NarrowCorner
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CornerIndex`: Index of corner to which to apply the corner relief; -1 to apply it to the corner last added with [IFeatureManager::AddCornerReliefCorner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddCornerReliefCorner.html)
- `ReliefType`: Type of corner relief as defined by [swCornerReliefType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCornerReliefType_e.html)
- `Length1`: Not used
- `Length2`:

  | If ReliefType is swCornerReliefType_e... | Then Length2 is the slot... |
  | --- | --- |
  | swCornerSquareRelief | Length of the corner relief |
  | swCornerObroundRelief | Length of the corner relief |
  | swCornerCircularRelief | Radius of the corner relief |
- `Length3`:

  | If ReliefType is swCornerReliefType_e... | Then Length3 is... |
  | --- | --- |
  | swCornerObroundRelief | Slot width of the corner relief |
  | swCornerSquareRelief and FilletedCorners = true | Radius of filleted corner |
- `CenterOnBendLines`: True to center the corner relief relative to the bend lines, false to not; valid only if ReliefType is one of the following:

  - swCornerReliefType_e.swCornerSquareRelief
  - swCornerReliefType_e.swCornerCircularRelief
  - swCornerReliefType_e.swCornerObroundRelief
- `RatioToThickness`: True to use a ratio value to cut the bend area so that the body can be folded, false to not; the ratios for valid relief types are calculated as follows where t = thickness of sheet metal:

  | If ReliefType is swCornerReliefType_e... | Then ratios are... |
  | --- | --- |
  | swCornerSquareRelief | Length2/t |
  | swCornerCircularRelief | Length2/t |
  | swCornerObroundRelief | Length2/t and Length3/t |
- `TangentToBend`: True to make the corner relief tangent to the inside bend edges, false to not
- `AddFilletedCorners`: True to fillet the corner relief corners, false to not; valid only if ReliefType = swCornerReliefType_e.swCornerSquareRelief
- `NarrowCorner`: True to use the algorithm for large bend radii to narrow the corner relief in the bend area, false to not; valid only if ReliefType is one of the following:

  - swCornerReliefType_e.swCornerSquareRelief
  - swCornerReliefType_e.swCornerCircularRelief
  - swCornerReliefType_e.swCornerObroundRelief

### Return Value

True if successful, false if not

## VBA Syntax

See [FeatureManager::AddCornerReliefType](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~AddCornerReliefType.html).

## Examples

[Create Corner Relief Feature (C#)](Create_Corner_Relief_Feature_Example_CSharp.htm)
[Create Corner Relief Feature (VBA)](Create_Corner_Relief_Feature_Example_VB.htm)
[Create Corner Relief Feature (VB.NET)](Create_Corner_Relief_Feature_Example_VBNET.htm)

## Remarks

To create a corner relief feature:

1. Call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Mark = 0 and Append = true to select the sheet metal body in which to create a corner relief feature.
2. Call IModelDocExtension::SelectByID2 with Mark = 4 and Append = true to select two faces that form a bend corner.
3. Call [IFeatureManager::AddCornerReliefCorner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddCornerReliefCorner.html) to add the corner to the corner relief feature.
4. Call this method to specify the corner relief for the corner.
5. Repeat steps 2 - 4 to add another corner to the corner relief feature.
6. Call [IFeatureManager::FinishCornerRelief](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FinishCornerRelief.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0

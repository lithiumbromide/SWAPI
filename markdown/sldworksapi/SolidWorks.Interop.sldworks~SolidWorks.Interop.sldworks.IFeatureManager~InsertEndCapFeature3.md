---
title: "InsertEndCapFeature3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertEndCapFeature3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature3.html"
---

# InsertEndCapFeature3 Method (IFeatureManager)

Inserts an end cap feature for one or more pre-selected open ends of a structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertEndCapFeature3( _
   ByVal Depth As System.Double, _
   ByVal BIsGivenOffset As System.Boolean, _
   ByVal BIsChamfer As System.Boolean, _
   ByVal OffsetValue As System.Double, _
   ByVal WallThicknessRatio As System.Double, _
   ByVal ChamferValue As System.Double, _
   ByVal BIsCornerTreatment As System.Boolean, _
   ByVal DepthOffset As System.Double, _
   ByVal BIsReverse As System.Boolean, _
   ByVal BIsEndCapInward As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Depth As System.Double
Dim BIsGivenOffset As System.Boolean
Dim BIsChamfer As System.Boolean
Dim OffsetValue As System.Double
Dim WallThicknessRatio As System.Double
Dim ChamferValue As System.Double
Dim BIsCornerTreatment As System.Boolean
Dim DepthOffset As System.Double
Dim BIsReverse As System.Boolean
Dim BIsEndCapInward As System.Integer
Dim value As Feature

value = instance.InsertEndCapFeature3(Depth, BIsGivenOffset, BIsChamfer, OffsetValue, WallThicknessRatio, ChamferValue, BIsCornerTreatment, DepthOffset, BIsReverse, BIsEndCapInward)
```

### C#

```csharp
Feature InsertEndCapFeature3(
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.bool BIsCornerTreatment,
   System.double DepthOffset,
   System.bool BIsReverse,
   System.int BIsEndCapInward
)
```

### C++/CLI

```cpp
Feature^ InsertEndCapFeature3(
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.bool BIsCornerTreatment,
   System.double DepthOffset,
   System.bool BIsReverse,
   System.int BIsEndCapInward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Depth`: Thickness of the end cap
- `BIsGivenOffset`: True to provide an offset value, false to provide a thickness ratio
- `BIsChamfer`: True if end cap feature is chamfered, false if end cap is filleted
- `OffsetValue`: Edge offset value; valid only if BIsGivenOffset is true
- `WallThicknessRatio`: Wall thickness ratio; valid only if BIsGivenOffset is false
- `ChamferValue`: Chamfer distance if BIsChamfer is true, fillet radius if BIsChamfer is false
- `BIsCornerTreatment`: True to chamfer or fillet the end cap corners, false to not; valid only if BIsGivenOffset is false
- `DepthOffset`: Inset distance; valid only if BIsEndCapInward = 2
- `BIsReverse`: True to reverse the offset or thickness ratio, false to not
- `BIsEndCapInward`: Thickness direction as defined in [swEndCapThicknessDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndCapThicknessDirection_e.html)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertEndCapFeature3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertEndCapFeature3.html).

## Examples

[Insert Weldment End Cap (VBA)](Insert_Weldment_End_Cap_Example_VB.htm)
[Insert Weldment End Cap (VB.NET)](Insert_Weldment_End_Cap_Example_VBNET.htm)
[Insert Weldment End Cap (C#)](Insert_Weldment_End_Cap_Example_CSharp.htm)

## Remarks

Before calling this method, select one or more end [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of a structural member in the graphics area.

Instead of using this method, you can pass the faces in an argument array of [IFeatureManager::InsertEndCapFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertEndCapFeature2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

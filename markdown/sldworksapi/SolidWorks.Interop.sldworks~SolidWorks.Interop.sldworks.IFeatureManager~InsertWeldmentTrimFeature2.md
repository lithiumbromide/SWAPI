---
title: "InsertWeldmentTrimFeature2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertWeldmentTrimFeature2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature2.html"
---

# InsertWeldmentTrimFeature2 Method (IFeatureManager)

Inserts a weldment trim feature for the specified weldment bodies or faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWeldmentTrimFeature2( _
   ByVal EndCond As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal GapValue As System.Double, _
   ByVal BodiesToTrim As System.Object, _
   ByVal BodiesOrFaces As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim EndCond As System.Integer
Dim Options As System.Integer
Dim GapValue As System.Double
Dim BodiesToTrim As System.Object
Dim BodiesOrFaces As System.Object
Dim value As Feature

value = instance.InsertWeldmentTrimFeature2(EndCond, Options, GapValue, BodiesToTrim, BodiesOrFaces)
```

### C#

```csharp
Feature InsertWeldmentTrimFeature2(
   System.int EndCond,
   System.int Options,
   System.double GapValue,
   System.object BodiesToTrim,
   System.object BodiesOrFaces
)
```

### C++/CLI

```cpp
Feature^ InsertWeldmentTrimFeature2(
   System.int EndCond,
   System.int Options,
   System.double GapValue,
   System.Object^ BodiesToTrim,
   System.Object^ BodiesOrFaces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EndCond`: End condition as defined by [swSolidworksWeldmentEndCondOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)
- `Options`: Logical sum of values as defined in [swWeldmentTrimExtendOptionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldmentTrimExtendOptionType_e.html) (see **Remarks**)
- `GapValue`: Length to trim (see **Remarks**)
- `BodiesToTrim`: Array of bodies to trim
- `BodiesOrFaces`: Array of bodies or faces that define the trimming boundaries

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertWeldmentTrimFeature2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertWeldmentTrimFeature2.html).

## Examples

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

## Remarks

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and specify the following marks to select the body, or bodies, to trim and the trimming boundaries:

- 1 = Body or bodies to trim
- 2 = Trimming boundaries (body or face)

If you include swWeldmentTrimExtendOption_WeldGap in the Options parameter, then the GapValue parameter is used. Specify 0 for GapValue to ensure that there is no weld gap.

If you exclude swWeldmentTrimExtendOption_WeldGap from the Options parameter, then the weld gap defaults to the last value specified in the SOLIDWORKS Design user-interface.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertWeldmentTrimFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature.html)
[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

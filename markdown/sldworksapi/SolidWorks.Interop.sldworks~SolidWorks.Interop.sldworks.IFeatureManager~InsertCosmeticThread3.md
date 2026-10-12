---
title: "InsertCosmeticThread3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCosmeticThread3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticThread3.html"
---

# InsertCosmeticThread3 Method (IFeatureManager)

Inserts a cosmetic thread.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCosmeticThread3( _
   ByVal Standard As System.Integer, _
   ByVal StandardType As System.String, _
   ByVal Size As System.String, _
   ByVal Diameter As System.Double, _
   ByVal EndType As System.Integer, _
   ByVal Depth As System.Double, _
   ByVal Note As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Standard As System.Integer
Dim StandardType As System.String
Dim Size As System.String
Dim Diameter As System.Double
Dim EndType As System.Integer
Dim Depth As System.Double
Dim Note As System.String
Dim value As Feature

value = instance.InsertCosmeticThread3(Standard, StandardType, Size, Diameter, EndType, Depth, Note)
```

### C#

```csharp
Feature InsertCosmeticThread3(
   System.int Standard,
   System.string StandardType,
   System.string Size,
   System.double Diameter,
   System.int EndType,
   System.double Depth,
   System.string Note
)
```

### C++/CLI

```cpp
Feature^ InsertCosmeticThread3(
   System.int Standard,
   System.String^ StandardType,
   System.String^ Size,
   System.double Diameter,
   System.int EndType,
   System.double Depth,
   System.String^ Note
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Standard`: Thread standard as defined by [swCosmeticStandardType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticStandardType_e.html)
- `StandardType`: Thread type for Standard
- `Size`: Thread size for the specified Standard
- `Diameter`: Thread diameter
- `EndType`: End condition as defined by [swCosmeticEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticEndConditions_e.html)
- `Depth`: Depth of the cosmetic thread; valid only for EndType = swCosmeticEndConditions_e.swEndConditionBlind or swCosmeticEndConditions_e.swEndConditionBlindUptoNext or swCosmeticEndConditions_e.swEndConditionBlind2Dia
- `Note`: Callout text to display in the drawing document

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCosmeticThread3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCosmeticThread3.html).

## Examples

[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)
[Traverse All Cosmetic Threads (VB.NET)](Traverse_All_Cosmetic_Threads_Example_VBNET.htm)
[Traverse All Cosmetic Threads (C#)](Traverse_All_Cosmetic_Threads_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

---
title: "InsertConvertToSheetMetal Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertConvertToSheetMetal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertConvertToSheetMetal.html"
---

# InsertConvertToSheetMetal Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertConvertToSheetMetal2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertConvertToSheetMetal2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertConvertToSheetMetal( _
   ByVal Thickness As System.Double, _
   ByVal ReverseThickDir As System.Boolean, _
   ByVal FindBends As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal Gap As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal ReliefRatio As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Thickness As System.Double
Dim ReverseThickDir As System.Boolean
Dim FindBends As System.Boolean
Dim Radius As System.Double
Dim Gap As System.Double
Dim ReliefType As System.Integer
Dim ReliefRatio As System.Double
Dim value As System.Boolean

value = instance.InsertConvertToSheetMetal(Thickness, ReverseThickDir, FindBends, Radius, Gap, ReliefType, ReliefRatio)
```

### C#

```csharp
System.bool InsertConvertToSheetMetal(
   System.double Thickness,
   System.bool ReverseThickDir,
   System.bool FindBends,
   System.double Radius,
   System.double Gap,
   System.int ReliefType,
   System.double ReliefRatio
)
```

### C++/CLI

```cpp
System.bool InsertConvertToSheetMetal(
   System.double Thickness,
   System.bool ReverseThickDir,
   System.bool FindBends,
   System.double Radius,
   System.double Gap,
   System.int ReliefType,
   System.double ReliefRatio
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Sheet thickness
- `ReverseThickDir`: True to reverse the direction of the sheet thickness, false to not
- `FindBends`: True to find pre-made bends and part thickness, false to not
- `Radius`: Radius for the bends
- `Gap`: Gap for all rips
- `ReliefType`: Relief type as defined by [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)
- `ReliefRatio`: Relief ratio

### Return Value

True if a Convert-Solid sheet metal feature is created, false if not

## VBA Syntax

See [FeatureManager::InsertConvertToSheetMetal](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertConvertToSheetMetal.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SolidwWorks 2009 FCS, Revision Number 17.0

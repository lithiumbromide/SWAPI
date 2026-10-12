---
title: "InsertSheetMetalCornerTrim Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalCornerTrim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalCornerTrim.html"
---

# InsertSheetMetalCornerTrim Method (IFeatureManager)

Inserts a break corner trim in the sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalCornerTrim( _
   ByVal InternalCornerFlag As System.Integer, _
   ByVal BreakType As System.Integer, _
   ByVal BreakDist As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal Param As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim InternalCornerFlag As System.Integer
Dim BreakType As System.Integer
Dim BreakDist As System.Double
Dim ReliefType As System.Integer
Dim Param As System.Double
Dim value As Feature

value = instance.InsertSheetMetalCornerTrim(InternalCornerFlag, BreakType, BreakDist, ReliefType, Param)
```

### C#

```csharp
Feature InsertSheetMetalCornerTrim(
   System.int InternalCornerFlag,
   System.int BreakType,
   System.double BreakDist,
   System.int ReliefType,
   System.double Param
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetalCornerTrim(
   System.int InternalCornerFlag,
   System.int BreakType,
   System.double BreakDist,
   System.int ReliefType,
   System.double Param
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InternalCornerFlag`: Do internal corners only
- `BreakType`: Type of break as defined in [swBreakCornerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)
- `BreakDist`: Distance to break from corner
- `ReliefType`: Type of relief:

  - 0 = circular
  - 1 = square
  - 2 = bend-waist
- `Param`: ReliefType dependent:

  - circular, its diameter
  - square, its side length
  - bend-waist, its radius

### Return Value

Pointer to the break corner trim [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) in the sheet metal part

## VBA Syntax

See [FeatureManager::InsertSheetMetalCornerTrim](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalCornerTrim.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

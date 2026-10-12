---
title: "InsertSheetMetalHem2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalHem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2.html"
---

# InsertSheetMetalHem2 Method (IFeatureManager)

Inserts a hem of the specified relief type at the selected edges of the current sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalHem2( _
   ByVal Type As System.Integer, _
   ByVal Position As System.Integer, _
   ByVal Reverse As System.Boolean, _
   ByVal DLength As System.Double, _
   ByVal DGap As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal DRad As System.Double, _
   ByVal DMiterGap As System.Double, _
   ByVal PCBA As CustomBendAllowance, _
   ByVal UseDefaultRelief As System.Boolean, _
   ByVal ReliefType As System.Integer, _
   ByVal ReliefTearTypes As System.Integer, _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal ReliefRatio As System.Double, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Position As System.Integer
Dim Reverse As System.Boolean
Dim DLength As System.Double
Dim DGap As System.Double
Dim DAngle As System.Double
Dim DRad As System.Double
Dim DMiterGap As System.Double
Dim PCBA As CustomBendAllowance
Dim UseDefaultRelief As System.Boolean
Dim ReliefType As System.Integer
Dim ReliefTearTypes As System.Integer
Dim UseReliefRatio As System.Boolean
Dim ReliefRatio As System.Double
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double
Dim value As Feature

value = instance.InsertSheetMetalHem2(Type, Position, Reverse, DLength, DGap, DAngle, DRad, DMiterGap, PCBA, UseDefaultRelief, ReliefType, ReliefTearTypes, UseReliefRatio, ReliefRatio, ReliefWidth, ReliefDepth)
```

### C#

```csharp
Feature InsertSheetMetalHem2(
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.int ReliefTearTypes,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetalHem2(
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance^ PCBA,
   System.bool UseDefaultRelief,
   System.int ReliefType,
   System.int ReliefTearTypes,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type as defined in [swHemTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemTypes_e.html)
- `Position`: Position as defined in [swHemPositionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemPositionTypes_e.html)
- `Reverse`: True reverses the direction, false does not
- `DLength`: Hem length; valid only for open or closed hems
- `DGap`: Gap distance; valid only for open hems
- `DAngle`: Hem angle; valid only for tear-drop or rolled hems
- `DRad`: Hem radius; valid only for tear-drop or rolled hems
- `DMiterGap`: Hem miter gap
- `PCBA`:

  | If... | Then... |
  | --- | --- |
  | non-NULL | Pointer to ICustomBendAllowance object for which required values have been set |
  | NULL | Parent bend's bend allowance is used |
- `UseDefaultRelief`: True to use the default relief, false to use the relief specified by ReliefType
- `ReliefType`: Type of relief as defined in [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html); valid only if UseDefaultRelief is false
- `ReliefTearTypes`: Type of relief tear as defined in [swReliefTearTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReliefTearTypes_e.html); valid only when:

  - UseDefaultRelief is false

  - and -

  - ReliefType is [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefTear
- `UseReliefRatio`: True to use ReliefRatio, false to use ReliefWidth/ReliefDepth; valid only when:

  - UseDefaultRelief is false

  - and -

  - ReliefType is either [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular
- `ReliefRatio`: Relief ratio; valid only when:

  - UseDefaultRelief is false

  - and -

  - UseReliefRatio is true

  - and -

  - ReliefType is either [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular
- `ReliefWidth`: Width of the relief; valid only when:

  - UseDefaultRelief is false

  - and -

  - UseReliefRatio is false

  - and -

  - ReliefType is either [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular
- `ReliefDepth`: Depth of the relief; valid only when:

  - UseDefaultRelief is false

  - and -

  - UseReliefRatio is false

  - and -

  - ReliefType is either [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefObround or [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertSheetMetalHem2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalHem2.html).

## Examples

[Insert Sheet Metal Hem (VBA)](Insert_Sheet_Metal_Hem_Example_VB.htm)
[Insert Sheet Metal Hem (VB.NET)](Insert_Sheet_Metal_Hem_Example_VBNET.htm)
[Insert Sheet Metal Hem (C#)](Insert_Sheet_Metal_Hem_Example_CSharp.htm)

## Remarks

Before calling this method:

1. Call [IFeatureManager::CreateCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateCustomBendAllowance.html) to create an instance of ICustomBendAllowance.
2. Initialize the CustomBendAllowance object.
3. Assign PCBA to the initialized CustomBendAllowance object.
4. Select one or more edges in the sheet metal model to which to add the specified hem.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)

## Availability

SOLIDWORKS 2011 SP03, Revision Number 19.3

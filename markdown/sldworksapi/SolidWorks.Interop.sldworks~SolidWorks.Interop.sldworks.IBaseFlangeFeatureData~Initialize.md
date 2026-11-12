---
title: "Initialize Method (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "Initialize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html"
---

# Initialize Method (IBaseFlangeFeatureData)

Initializes a newly created sheet metal base flange feature with the specified data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Initialize( _
   ByVal UseMaterialSheetMetalParameters As System.Boolean, _
   ByVal OverrideDefaultBendAllowance As System.Boolean, _
   ByVal CustomBendAllowance As System.Object, _
   ByVal OverrideDefaultBendRelief As System.Boolean, _
   ByVal ReliefType As System.Integer, _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal ReliefRatio As System.Double, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim UseMaterialSheetMetalParameters As System.Boolean
Dim OverrideDefaultBendAllowance As System.Boolean
Dim CustomBendAllowance As System.Object
Dim OverrideDefaultBendRelief As System.Boolean
Dim ReliefType As System.Integer
Dim UseReliefRatio As System.Boolean
Dim ReliefRatio As System.Double
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double

instance.Initialize(UseMaterialSheetMetalParameters, OverrideDefaultBendAllowance, CustomBendAllowance, OverrideDefaultBendRelief, ReliefType, UseReliefRatio, ReliefRatio, ReliefWidth, ReliefDepth)
```

### C#

```csharp
void Initialize(
   System.bool UseMaterialSheetMetalParameters,
   System.bool OverrideDefaultBendAllowance,
   System.object CustomBendAllowance,
   System.bool OverrideDefaultBendRelief,
   System.int ReliefType,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
)
```

### C++/CLI

```cpp
void Initialize(
   System.bool UseMaterialSheetMetalParameters,
   System.bool OverrideDefaultBendAllowance,
   System.Object^ CustomBendAllowance,
   System.bool OverrideDefaultBendRelief,
   System.int ReliefType,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseMaterialSheetMetalParameters`: True to use the sheet metal properties of the applied material, false to not
- `OverrideDefaultBendAllowance`: True to override the default bend allowance, false to not
- `CustomBendAllowance`: [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html); valid only if OverrideDefaultBendAllowance is true
- `OverrideDefaultBendRelief`: True to override the default bend relief, false to not
- `ReliefType`: Relief type as defined in [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html); valid only if OverrideDefaultBendRelief is true
- `UseReliefRatio`: True to use ReliefRatio, false to use ReliefWidth and ReliefDepth; valid only if OverrideDefaultBendRelief is true
- `ReliefRatio`: Relief ratio; valid only if UseReliefRatio is true
- `ReliefWidth`: Relief width (numerator of relief ratio); valid only if UseReliefRatio is false
- `ReliefDepth`: Relief depth (denominator of relief ratio); valid only if UseReliefRatio is false

## VBA Syntax

See [BaseFlangeFeatureData::Initialize](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~Initialize.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

After you call this method to initialize the base flange feature, you cannot change any of the properties associated with this method's parameters. After initialization you can get, but not set, the following using this interface:

- Whether to use default bend allowance
- Whether to use default bend relief
- Whether to use material sheet metal parameters
- Whether to use relief ratio
- Custom bend allowance
- Relief depth
- Relief ratio
- Relief type
- Relief width

You can, however, change any properties associated with the parent sheet metal after calling this method. For example:

- [ISheetMetalFeatureData::SetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.html)
- [ISheetMetalFeatureData::SetOverrideDefaultParameter2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter2.html)
- [ISheetMetalFeatureData::AutoReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~AutoReliefType.html)
- [ISheetMetalFeatureData::ReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~ReliefRatio.html)
- [ISheetMetalFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseMaterialSheetMetalParameters.html)

See the Examples.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetCustomBendAllowance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetCustomBendAllowance.html)
[IBaseFlangeFeatureData::ReliefDepth Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefDepth.html)
[IBaseFlangeFeatureData::ReliefRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefRatio.html)
[IBaseFlangeFeatureData::ReliefType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefType.html)
[IBaseFlangeFeatureData::ReliefWidth Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefWidth.html)
[IBaseFlangeFeatureData::UseDefaultBendAllowance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseDefaultBendAllowance.html)
[IBaseFlangeFeatureData::UseDefaultBendRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseDefaultBendRelief.html)
[IBaseFlangeFeatureData::UseMaterialSheetMetalParameters Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.html)
[IBaseFlangeFeatureData::UseReliefRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseReliefRatio.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30

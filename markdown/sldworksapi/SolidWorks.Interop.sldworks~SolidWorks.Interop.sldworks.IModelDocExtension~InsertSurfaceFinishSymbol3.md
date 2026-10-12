---
title: "InsertSurfaceFinishSymbol3 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertSurfaceFinishSymbol3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertSurfaceFinishSymbol3.html"
---

# InsertSurfaceFinishSymbol3 Method (IModelDocExtension)

Creates a surface-finish symbol based on the last selection.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSurfaceFinishSymbol3( _
   ByVal SymType As System.Integer, _
   ByVal LeaderType As System.Integer, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double, _
   ByVal LaySymbol As System.Integer, _
   ByVal ArrowType As System.Integer, _
   ByVal MachAllowance As System.String, _
   ByVal OtherVals As System.String, _
   ByVal ProdMethod As System.String, _
   ByVal SampleLen As System.String, _
   ByVal MaxRoughness As System.String, _
   ByVal MinRoughness As System.String, _
   ByVal RoughnessSpacing As System.String _
) As SFSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim SymType As System.Integer
Dim LeaderType As System.Integer
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim LaySymbol As System.Integer
Dim ArrowType As System.Integer
Dim MachAllowance As System.String
Dim OtherVals As System.String
Dim ProdMethod As System.String
Dim SampleLen As System.String
Dim MaxRoughness As System.String
Dim MinRoughness As System.String
Dim RoughnessSpacing As System.String
Dim value As SFSymbol

value = instance.InsertSurfaceFinishSymbol3(SymType, LeaderType, LocX, LocY, LocZ, LaySymbol, ArrowType, MachAllowance, OtherVals, ProdMethod, SampleLen, MaxRoughness, MinRoughness, RoughnessSpacing)
```

### C#

```csharp
SFSymbol InsertSurfaceFinishSymbol3(
   System.int SymType,
   System.int LeaderType,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.int LaySymbol,
   System.int ArrowType,
   System.string MachAllowance,
   System.string OtherVals,
   System.string ProdMethod,
   System.string SampleLen,
   System.string MaxRoughness,
   System.string MinRoughness,
   System.string RoughnessSpacing
)
```

### C++/CLI

```cpp
SFSymbol^ InsertSurfaceFinishSymbol3(
   System.int SymType,
   System.int LeaderType,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.int LaySymbol,
   System.int ArrowType,
   System.String^ MachAllowance,
   System.String^ OtherVals,
   System.String^ ProdMethod,
   System.String^ SampleLen,
   System.String^ MaxRoughness,
   System.String^ MinRoughness,
   System.String^ RoughnessSpacing
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymType`: Type of symbol as defined in [swSFSymType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html)
- `LeaderType`: Type of leader as defined in [swLeaderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)
- `LocX`: x location for symbol
- `LocY`: y location for symbol
- `LocZ`: z location for symbol
- `LaySymbol`: Type of lay direction as defined in [swSFLaySym_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFLaySym_e.html)
- `ArrowType`: Type of arrow head as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `MachAllowance`: Material removal allowance
- `OtherVals`: Other roughness values
- `ProdMethod`: Production method and treatment
- `SampleLen`: Sampling length
- `MaxRoughness`: Maximum roughness
- `MinRoughness`: Minimum roughness
- `RoughnessSpacing`: Roughness spacing

### Return Value

Newly inserted [surface finish symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html)

## VBA Syntax

See [ModelDocExtension::InsertSurfaceFinishSymbol3](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertSurfaceFinishSymbol3.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

The SOLIDWORKS Design software uses the location parameters for this method only if the surface finish symbol has a leader leaderType != swNO_LEADER.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

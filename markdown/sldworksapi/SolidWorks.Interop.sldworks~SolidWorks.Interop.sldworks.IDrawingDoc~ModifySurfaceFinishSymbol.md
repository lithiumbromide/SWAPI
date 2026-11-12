---
title: "ModifySurfaceFinishSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ModifySurfaceFinishSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ModifySurfaceFinishSymbol.html"
---

# ModifySurfaceFinishSymbol Method (IDrawingDoc)

Modifies the selected surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function ModifySurfaceFinishSymbol( _
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
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
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
Dim value As System.Boolean

value = instance.ModifySurfaceFinishSymbol(SymType, LeaderType, LocX, LocY, LocZ, LaySymbol, ArrowType, MachAllowance, OtherVals, ProdMethod, SampleLen, MaxRoughness, MinRoughness, RoughnessSpacing)
```

### C#

```csharp
System.bool ModifySurfaceFinishSymbol(
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
System.bool ModifySurfaceFinishSymbol(
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

- `SymType`: Symbol type as defined in [swSFSymType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html)
- `LeaderType`: Leader type as defined in [swLeaderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)
- `LocX`: X location for symbol
- `LocY`: Y location for symbol
- `LocZ`: Z location for symbol
- `LaySymbol`: Direction of lay as defined in [swSFLaySym_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFLaySym_e.html)
- `ArrowType`: Arrowhead type as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `MachAllowance`: Material removal allowance
- `OtherVals`: Other roughness values
- `ProdMethod`: Production method/treatment
- `SampleLen`: Sampling length
- `MaxRoughness`: Maximum roughness
- `MinRoughness`: Minimum roughness
- `RoughnessSpacing`: Roughness spacing

## VBA Syntax

See [DrawingDoc::ModifySurfaceFinishSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ModifySurfaceFinishSymbol.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IModelDocExtension::InsertSurfaceFinishSymbol3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertSurfaceFinishSymbol3.html)
[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)

---
title: "SetSymbol Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "SetSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetSymbol.html"
---

# SetSymbol Method (ISFSymbol)

Sets the type of symbol for this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSymbol( _
   ByVal Symbol As System.Integer, _
   ByVal SurfaceTexture As System.Integer, _
   ByVal AllAround As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim Symbol As System.Integer
Dim SurfaceTexture As System.Integer
Dim AllAround As System.Boolean
Dim value As System.Boolean

value = instance.SetSymbol(Symbol, SurfaceTexture, AllAround)
```

### C#

```csharp
System.bool SetSymbol(
   System.int Symbol,
   System.int SurfaceTexture,
   System.bool AllAround
)
```

### C++/CLI

```cpp
System.bool SetSymbol(
   System.int Symbol,
   System.int SurfaceTexture,
   System.bool AllAround
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Symbol`: Type of symbol as defined in [swSFSymType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html)
- `SurfaceTexture`: Symbol surface text type as defined in [swSFSymType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html)
- `AllAround`: True if symbol is All Around, false if symbol is Local

### Return Value

True if symbol is set, false if it is not

## VBA Syntax

See [SFSymbol::SetSymbol](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~SetSymbol.html).

## Remarks

The Symbol argument must be one of the following values from the [swSFSymType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html) enumeration: swSFBasic, swSFMachining_Req, swSFDont_Machine, swSFJIS_No_Machining, swSFJIS_Basic, or swSFJIS_Machining_Req.

[ISFSymbol::GetSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetSymbol.html) will get this value.

| If the symbol is... | Then... |
| --- | --- |
| swSFJIS_No_Machining or swSFJIS_Basic | SurfaceTexture argument must be one of these values from the swSFSymType enumeration: swSFJIS_Surface_Texture_1, swSFJIS_Surface_Texture_2, swSFJIS_Surface_Texture_3, or swSFJIS_Surface_Texture_4. For any other symbol types, this argument is ignored, and 0 should be passed in. The ISFSymbol::GetSymbolSurfaceTexture method will get this value. |
| swSFBasic, swSFMachining_Req, or swSFDont_Machine | AllAround argument indicates whether this is an All Around or Local symbol. Use ISFSymbol::GetSymbolAllAround to get this value. |

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

---
title: "GetSymbolSurfaceTexture Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetSymbolSurfaceTexture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolSurfaceTexture.html"
---

# GetSymbolSurfaceTexture Method (ISFSymbol)

Gets the symbol surface texture type for this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymbolSurfaceTexture() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Integer

value = instance.GetSymbolSurfaceTexture()
```

### C#

```csharp
System.int GetSymbolSurfaceTexture()
```

### C++/CLI

```cpp
System.int GetSymbolSurfaceTexture();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Symbol surface texture type as defined in [swSFSymType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html) (see **Remarks**)

## VBA Syntax

See [SFSymbol::GetSymbolSurfaceTexture](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetSymbolSurfaceTexture.html).

## Remarks

[ISFSymbol::GetSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetSymbol.html) returns one of the following values from the [swSFSymType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFSymType_e.html) enumeration: swSFBasic, swSFMachining_Req, swSFDont_Machine, swSFJIS_No_Machining, swSFJIS_Basic, or swSFJIS_Machining_Req.

| If the symbol is... | Then use... |
| --- | --- |
| swSFJIS_No_Machining or swSFJIS_Basic | ISFSymbol::GetSymbolSurfaceTexture to retrieve more information about the symbol. It returns one of these values from the swSFSymType_e enumeration: swSFJIS_Surface_Texture_1, swSFJIS_Surface_Texture_2, swSFJIS_Surface_Texture_3, or swSFJIS_Surface_Texture_4. |
| swSFBasic, swSFMachining_Req, or swSFDont_Machine | ISFSymbol::GetSymbolAllAround to retrieve more information about the symbol. This method returns a Boolean indicating whether this is an All Around or Local symbol. |

To set the symbol type, use [ISFSymbol::SetSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~SetSymbol.html).

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0

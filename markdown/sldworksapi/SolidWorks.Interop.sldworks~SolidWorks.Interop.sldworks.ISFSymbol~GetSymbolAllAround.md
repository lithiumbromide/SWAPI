---
title: "GetSymbolAllAround Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetSymbolAllAround"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolAllAround.html"
---

# GetSymbolAllAround Method (ISFSymbol)

Gets whether this symbol is All Around or Local for this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymbolAllAround() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Boolean

value = instance.GetSymbolAllAround()
```

### C#

```csharp
System.bool GetSymbolAllAround()
```

### C++/CLI

```cpp
System.bool GetSymbolAllAround();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if All Around symbol, false if Local symbol

## VBA Syntax

See [SFSymbol::GetSymbolAllAround](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetSymbolAllAround.html).

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

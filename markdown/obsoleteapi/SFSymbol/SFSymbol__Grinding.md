---
title: "SFSymbol::Grinding"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SFSymbol/SFSymbol__Grinding.htm"
---

# SFSymbol::Grinding

This property is obsolete and has been superseded by [SFSymbol::GetSymbolSurfaceTexture](sldworksAPI.chm::/SFSymbol/SFSymbol__GetSymbolSurfaceTexture.htm).

Description

This property indicates whether or not grinding flag is set on this surface-finish symbol.

Syntax (OLE Automation)

grinding = SFSymbol.Grinding (VB Get property)

SFSymbol.Grinding = grinding (VB Set property)

grinding = SFSymbol.GetGrinding ( ) (C++ Get property)

SFSymbol.SetGrinding ( grinding ) (C++ Set property)

| Property: | (BOOL) grinding | TRUE if grinding flag is enabled, FALSE if disabled |
| --- | --- | --- |

Syntax (COM)

status = SFSymbol->get_Grinding ( &grinding )

status = SFSymbol->put_Grinding ( grinding )

| Property: | (VARIANT_BOOL) grinding | TRUE if grinding flag is enabled, FALSE if disabled |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

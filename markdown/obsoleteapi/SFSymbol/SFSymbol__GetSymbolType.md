---
title: "SFSymbol::GetSymbolType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SFSymbol/SFSymbol__GetSymbolType.htm"
---

# SFSymbol::GetSymbolType

This method is obsolete and has been superseded by [SFSymbol::GetSymbol](sldworksAPI.chm::/SFSymbol/SFSymbol__GetSymbol.htm).

Description

This method gets the symbol type for this surface-finish symbol.

Syntax (OLE Automation)

retval = SFSymbol.GetSymbolType ( )

| Return: | (long) retval | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |

Syntax (COM)

status = SFSymbol->GetSymbolType ( &retval )

| Output: | (long) retval | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To set the symbol type, use SFSymbol::SetSymbolType.

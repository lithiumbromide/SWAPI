---
title: "SFSymbol::SetSymbolType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SFSymbol/SFSymbol__SetSymbolType.htm"
---

# SFSymbol::SetSymbolType

This method is obsolete and has been superseded by [SFSymbol::SetSymbol](sldworksAPI.chm::/SFSymbol/SFSymbol__SetSymbol.htm).

Description

This method sets the symbol type for this surface-finish symbol.

Syntax (OLE Automation)

retval = SFSymbol.SetSymbolType ( symbolType )

| Input: | (long) symbolType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the symbol type is successfully set, FALSE if not |

Syntax (COM)

status = SFSymbol->SetSymbolType ( symbolType, &retval )

| Input: | (long) symbolType | Symbol type as defined in swSFSymType_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the symbol type is successfully set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If an invalid symbol type is specified, the symbol is not changed, and FALSE is returned.

To see the model or drawing changes caused by running this method, you must redraw your window. See ModelDoc2::GraphicsRedraw2 for details.

To get the symbol type, use SFSymbol::GetSymbolType.

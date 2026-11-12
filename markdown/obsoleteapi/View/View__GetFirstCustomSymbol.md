---
title: "View::GetFirstCustomSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstCustomSymbol.htm"
---

# View::GetFirstCustomSymbol

This method is obsolete and has been superseded by [View::GetFirstBlockInstance](View__GetFirstBlockInstance.htm).

Description

This method gets the first custom symbol in the view.

Syntax (OLE Automation)

retval = View.GetFirstCustomSymbol( )

| Return: | (LPDISPATCH) retval | Dispatch object for the first CustomSymbol in the view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstCustomSymbol( &retval )

| Output: | (LPCUSTOMSYMBOL) retval | Pointer to the first CustomSymbol in the view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

---
title: "CustomSymbol::GetNext"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetNext.htm"
---

# CustomSymbol::GetNext

This method is obsolete and has been superseded by [BlockInstance::GetNext](../BlockInstance/BlockInstance__GetNext.htm).

Description

This method gets the next custom symbol in the view.

Syntax (OLE Automation)

retval = CustomSymbol.GetNext ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the next custom symbol |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->IGetNext ( &retval )

| Output: | (LPCUSTOMSYMBOL) retval | Pointer to the next custom symbol |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

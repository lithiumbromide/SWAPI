---
title: "CustomSymbol::GetSketch"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetSketch.htm"
---

# CustomSymbol::GetSketch

This method is obsolete and has been superseded by [BlockDefinition::GetSketch](../BlockDefinition/BlockDefinition__GetSketch.htm).

Description

This method returns the Sketch object for this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetSketch ()

| Return: | (LPDISPATCH) retval | Dispatch object for the sketch |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->IGetSketch ( &retval )

| Output: | (LPSKETCH) retval | Pointer to the sketch |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

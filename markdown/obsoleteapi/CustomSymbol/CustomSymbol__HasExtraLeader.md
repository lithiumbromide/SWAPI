---
title: "CustomSymbol::HasExtraLeader"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__HasExtraLeader.htm"
---

# CustomSymbol::HasExtraLeader

This method is obsolete and has been superseded by [Note::HasExtraLeader](sldworksAPI.chm::/Note/Note__HasExtraLeader.htm).

Description

This method determines if this symbol has a head on the leader.

Syntax (OLE Automation)

retval = CustomSymbol.HasExtraLeader ( )

| Return: | (BOOL)retval | TRUE if extra leader line exists, FALSE if it does not |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->HasExtraLeader ( &retval )

| Output: | (VARIANT_BOOL)retval | TRUE if extra leader line exists, FALSE if it does not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if Successful |

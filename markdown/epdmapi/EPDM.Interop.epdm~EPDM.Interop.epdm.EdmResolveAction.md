---
title: "EdmResolveAction Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmResolveAction"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmResolveAction.html"
---

# EdmResolveAction Enumeration

Types of flags that you return to SOLIDWORKS PDM Professional from [IEdmCallback6::Resolve](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback6~Resolve.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmResolveAction
   Inherits System.Enum
```

### C#

```csharp
public enum EdmResolveAction : System.Enum
```

### C++/CLI

```cpp
public enum class EdmResolveAction : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmra_ClearUnique | 2 = Clear the duplicated unique-constrained values |
| Edmra_CopySerial | 4 = Copy existing serial number values from the source file |
| Edmra_CreateSerial | 8 = Create new serial number values |
| Edmra_ForceGenerateSerial | 128 = Force regeneration of serial numbers when values already exist; without the flag, SOLIDWORKS PDM Professional only generates values that are missing in the file |
| Edmra_KeepExistingSerialNumbers | 32 = Do not replace existing serial numbers with new ones; SOLIDWORKS PDM Professional still creates serial numbers for empty fields; if this flag is not specified, SOLIDWORKS PDM Professional overwrites existing serial numbers with new ones |
| Edmra_Replace | 1 = Replace existing file with the new one |
| Edmra_Skip | 16 = Do not process this file |
| Edmra_UniqueVarDelayCheck | 64 = Delay the unique variable check to next check in |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

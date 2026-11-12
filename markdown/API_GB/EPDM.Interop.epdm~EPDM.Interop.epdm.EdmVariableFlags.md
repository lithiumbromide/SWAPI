---
title: "EdmVariableFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmVariableFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableFlags.html"
---

# EdmVariableFlags Enumeration

Flags that set the style of variables used in file and folder data cards. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmVariableFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmVariableFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmVariableFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmVar_Mandatory | 2 = Missing values are not permitted; only used for files, ignored for folders |
| EdmVar_Unique | 1 = Values of the variable must be unique; only used for files, ignored for folders |
| EdmVar_VerFreeUpdateAll | 4 = Every version and every revision, regardless access, workflow states etc., are affected by the variable update |
| EdmVar_VerFreeUpdateLatest | 8 = Only the latest version is affected by the variable update |

## Remarks

Used in [IEdmVariable5::Flags](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~Flags.html).

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

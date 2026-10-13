---
title: "EdmVariableType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmVariableType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableType.html"
---

# EdmVariableType Enumeration

Constants that identify the data type of a variable.

## Syntax

### Visual Basic

```vb
Public Enum EdmVariableType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmVariableType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmVariableType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmVarType_Bool | 4 = Boolean data (i.e., yes or no values) |
| EdmVarType_Date | 5 = Date and time data |
| EdmVarType_Float | 3 = Floating-point data (64 bit) |
| EdmVarType_Int | 2 = Integer data (32 bit) |
| EdmVarType_None | 0 = Error code; used internally |
| EdmVarType_Text | 1 = String data |

## Remarks

Used in [IEdmVariable5::VariableType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~VariableType.html).

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

---
title: "EdmMBoxType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmMBoxType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMBoxType.html"
---

# EdmMBoxType Enumeration

Types of widget to insert or display in [IEdmVault5::MsgBox](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~MsgBox.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmMBoxType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmMBoxType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmMBoxType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmMbt_AbortRetryIgnore | 2 = Insert Abort , Retry, and Ignore |
| EdmMbt_Icon_Information | 64 = Display the information icon |
| EdmMbt_Icon_Question | 32 = Display the question icon |
| EdmMbt_Icon_Warning | 48 = Display the warning icon |
| EdmMbt_OKCancel | 1 = Insert OK and Cancel |
| EdmMbt_OKOnly | 0 = Insert OK |
| EdmMbt_RetryCancel | 5 = Insert Retry and Cancel |
| EdmMbt_YesNo | 4 = Insert Yes and No |
| EdmMbt_YesNoCancel | 3 = Insert Yes , No , and Cancel |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

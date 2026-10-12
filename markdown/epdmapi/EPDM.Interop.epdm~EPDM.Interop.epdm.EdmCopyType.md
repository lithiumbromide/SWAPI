---
title: "EdmCopyType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCopyType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyType.html"
---

# EdmCopyType Enumeration

Types of file copy operations.

## Syntax

### Visual Basic

```vb
Public Enum EdmCopyType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCopyType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCopyType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCopy_CopyTree | 1 |
| EdmCopy_Normal | 0 |

## Remarks

This enumerator is used by [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).mlLongData1 to store the type of copy operation for PreCopy and PostCopy events.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

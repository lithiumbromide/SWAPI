---
title: "EdmRawRefFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRawRefFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawRefFlags.html"
---

# EdmRawRefFlags Enumeration

Flags used in [EdmRawReference](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmRawRefFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRawRefFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRawRefFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Edmrrf_Ghost | 1 = DWG files can store grandchildren as references; for example, in the file tree: A.dwg=>B.dwg=>C.dwg the file C.dwg can be stored as a ghost reference in A.dwg and as a normal reference in B.dwg; SOLIDWORKS PDM Professional does not show ghost references in check-in dialog boxes but does update them when files are moved |
| Edmrrf_InternalComponent | 2 = Not used |
| Edmrrf_Nothing | 0 = Normal file reference |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

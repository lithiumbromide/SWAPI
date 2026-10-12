---
title: "EdmGetFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGetFlag"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetFlag.html"
---

# EdmGetFlag Enumeration

Options for retrieving files used in calls to [IEdmFile5::GetFileCopy](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFileCopy.html), [IEdmEnumeratorVersion5::GetFileCopy](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFileCopy.html), [IEdmVersion5::GetFileCopy](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetFileCopy.html), and [IEdmRevision5::GetFileCopy](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5~GetFileCopy.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmGetFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmGetFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmGetFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmGet_DisableRefresh | 2 = Do not refresh File Explorer when a file is retrieved |
| EdmGet_ForPreview | 64 = Only retrieve referenced files that are needed by SOLIDWORKS PDM Professional's preview when retrieving the referencing file |
| EdmGet_MakeReadOnly | 1 = Mark the retrieved file as read-only |
| EdmGet_Refs | 4 = Get referenced files |
| EdmGet_RefsOnlyMissing | 8 = Only get referenced files that are not present on the local hard disk; only valid in combination with EdmGet_Refs |
| EdmGet_RefsOverwriteLocked | 32 = Retrieve checked out referenced files and their references; only valid in combination with EdmGet_Refs; Warning: Setting this flag means that any previous modifications to checked out files will be lost. |
| EdmGet_RefsVerLatest | 16 = Retrieve the latest versions of referenced files that you have permission to see instead of attached versions that were used when the file was checked in; only valid in combination with EdmGet_Refs |
| EdmGet_Simple | 0 = Retrieve the file |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

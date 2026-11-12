---
title: "EdmAddAddInFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddAddInFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddAddInFlags.html"
---

# EdmAddAddInFlags Enumeration

Options for adding add-ins. Used by [IEdmAddInMgr5::AddAddIns](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5~AddAddIns.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmAddAddInFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmAddAddInFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmAddAddInFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmAddin_AddAllFilesToOneAddIn | 1 = Add all of the files passed to IEdmAddInMgr5::AddAddIns to the same add-in; this is useful for creating an add-in that has both a 64-bit DLL and a 32-bit DLL |
| EdmAddin_Nothing | 0 = Attempt to create one add-in per file that is passed to IEdmAddInMgr5::AddAddIns |
| EdmAddin_ReplaceDuplicates | 2 = Replace an existing add-in that has the same COM class ID (CLSID) and package name; IEdmAddInMgr5::AddAddIns returns an error if the existing add-in has the same CLSID but a different package name |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

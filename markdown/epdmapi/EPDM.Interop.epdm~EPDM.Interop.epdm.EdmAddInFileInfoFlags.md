---
title: "EdmAddInFileInfoFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddInFileInfoFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfoFlags.html"
---

# EdmAddInFileInfoFlags Enumeration

Types of file in the add-in package used in [EdmAddInFileInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInFileInfo.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmAddInFileInfoFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmAddInFileInfoFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmAddInFileInfoFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmAdfif_AddInObject32 | 2 = File contains the 32-bit IEdmAddIn5 implementation; the code is used only in combination with EdmAdfif_ComDLL32 |
| EdmAdfif_AddInObject64 | 8 = File contains the 64-bit IEdmAddIn5 implementation; the code is used only in combination with EdmAdfif_ComDLL64 |
| EdmAdfif_ComDll32 | 1 = File should be COM-registered in a 32-bit process |
| EdmAdfif_ComDll64 | 4 = File should be COM-registered in a 64-bit process |
| EdmAdfif_DataFile | 0 = Data file that is copied and maintained but not otherwise used by SOLIDWORKS PDM Professional |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

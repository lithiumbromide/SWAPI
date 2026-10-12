---
title: "EdmRefreshFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefreshFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefreshFlag.html"
---

# EdmRefreshFlag Enumeration

Flags that cause SOLIDWORKS PDM Professional to refresh elements of the user interface. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmRefreshFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRefreshFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRefreshFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmRefresh_FileList | 1 = Refresh the file listing in File Explorer; this value should be returned if you add, delete, rename, check out, check in, etc., a file and want the change to be immediately visible to the user |
| EdmRefresh_Hooks | 2 = Force reloading of hooks; this value is normally only returned if your add-in changes the number of registered hooks |
| EdmRefresh_Menu | 4 = Force an update of the Tools menu in the File Explorer; this value is normally only returned if your add-in changes the number of registered menu commands |
| EdmRefresh_Nothing | 0 = No refresh is required |
| EdmRefresh_Toolbar | 8 = Force an update of the toolbar in File Explorer; this value is normally only returned if your add-in changes the number of registered menu commands with toolbar buttons |

## Remarks

You can return a combination of these flags from your add-in's [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) via the [EdmCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html) struct to cause SOLIDWORKS PDM Professional to refresh certain parts of the user interface.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[EdmCmd::mlEdmRefreshFlags Field](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlEdmRefreshFlags.html)

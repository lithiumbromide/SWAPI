---
title: "EdmBrowseFlag Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBrowseFlag"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrowseFlag.html"
---

# EdmBrowseFlag Enumeration

Browse options used in calls to [IEdmVault5::BrowseForFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~BrowseForFile.html). [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmBrowseFlag
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBrowseFlag : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBrowseFlag : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmBws_ForOpen | 0 = Display the Open dialog box |
| EdmBws_ForSave | 1 = Display a Save As dialog box |
| EdmBws_Help | 32 = Display Help in the dialog box |
| EdmBws_PermitExternalFiles | 16 = Permit the user to select files that are outside the file vault folder tree |
| EdmBws_PermitLocalFiles | 4 = Permit the user to select files that are inside the file vault folder tree, but not checked in to the vault |
| EdmBws_PermitMultipleSel | 2 = Permit the user to select more than one file |
| EdmBws_PermitVaultFiles | 8 = Permit the user to select files that are part of the file vault |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

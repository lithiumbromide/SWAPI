---
title: "EdmItemGenerationFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmItemGenerationFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemGenerationFlags.html"
---

# EdmItemGenerationFlags Enumeration

Flags that control the behavior of [IEdmBatchItemGeneration::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~CreateTree.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmItemGenerationFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmItemGenerationFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmItemGenerationFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Eigcf_Nothing | 0 = Default behavior |
| Eigcf_OpenItemsCheckbox | 1 = This flag does not change the behavior of the IEdmBatchItemGeneration::CreateTree method itself, but it does affect a subsequent call to IEdmBatchItemGeneration::ShowDlg ; the dialog box displayed by IEdmBatchItemGeneration::ShowDlg will contain a checkbox to open items after the completion of the item-creation command if this flag is specified |

## Remarks

See also the general note about items in the API.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

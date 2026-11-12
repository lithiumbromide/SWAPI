---
title: "EdmLaunchSearchFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmLaunchSearchFlags"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLaunchSearchFlags.html"
---

# EdmLaunchSearchFlags Enumeration

Flags which control the behavior of [IEdmSearch7::LaunchApp](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7~LaunchApp.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmLaunchSearchFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmLaunchSearchFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmLaunchSearchFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Elsf_DefaultIsAFavorite | 4 = The bsDefault argument to IEdmSearch7::LaunchApp is the name of a favorite, not a form |
| Elsf_HidePreview | 2 = Hides the preview area under the result listing in the search tool |
| Elsf_HideTree | 1 = Hides the tree pane in the search tool |
| Elsf_Nothing | 0 = Default behavior |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

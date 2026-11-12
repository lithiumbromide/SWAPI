---
title: "EdmBomType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomType.html"
---

# EdmBomType Enumeration

Types of BOM passed in [EdmBomInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInfo.html) and [EdmBomLayout2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout2.html) structures.

## Syntax

### Visual Basic

```vb
Public Enum EdmBomType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmBomType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmBomType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Computed | 0 = The BOM is computed (check in/out and workflow are not supported) |
| ComputedActivated | 1 = The BOM is computed, and the Activated checkbox is checked so the BOM appears in File Explorer |
| ItemBOM | 8 |
| Saved | 2 = The user has saved this BOM |
| SWBOM | 3 = SOLIDWORKS BOM |
| SWBOMActivated | 4 = SOLIDWORKS BOM, and the Activated checkbox is checked so the BOM appears in File Explorer |
| SWBOMSaved | 5 = The user has saved this SOLIDWORKS BOM |
| UndefinedBOM | 9 = BOM template |
| WeldmentBOM | 7 = Used as a weldment BOM in the preview |
| WeldmentCutlist | 6 = Used as a weldment cutlist in the preview |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

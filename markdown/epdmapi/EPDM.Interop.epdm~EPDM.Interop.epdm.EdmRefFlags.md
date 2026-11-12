---
title: "EdmRefFlags Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRefFlags"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefFlags.html"
---

# EdmRefFlags Enumeration

Types of item reference. [Bitmask](Bitmasks.htm).

## Syntax

### Visual Basic

```vb
Public Enum EdmRefFlags
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRefFlags : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRefFlags : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmRef_Dynamic | 4 = Auto-update item to file reference |
| EdmRef_File | 1 = Item to file reference |
| EdmRef_Item | 2 = Item to item reference |
| EdmRef_Static | 8 = Attachment-type item to file reference |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[EdmItemRef Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef.html)
[IEdmReference7::EdmRefFlags Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7~EdmRefFlags.html)
[IEdmReference7::GetFirstChildPosition2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7~GetFirstChildPosition2.html)
[IEdmReference7::GetFirstParentPosition2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7~GetFirstParentPosition2.html)
[IEdmBatchItemGeneration2::AddSelection2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2~AddSelection2.html)

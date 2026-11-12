---
title: "EdmDocIDs Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmDocIDs"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDocIDs.html"
---

# EdmDocIDs Structure

Contains information about one document in the vault; used in [IEdmVault20::GetFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault20~GetFiles.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmDocIDs
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmDocIDs : System.ValueType
```

### C++/CLI

```cpp
public value class EdmDocIDs : public System.ValueType
```

## Examples

struct EdmDocIDs

{
integer [mlDocID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDocIDs~mlDocID.html);
integer [mlProjID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDocIDs~mlProjID.html);
};

## See Also

[EdmDocIDs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDocIDs_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

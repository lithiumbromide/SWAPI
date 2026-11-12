---
title: "EdmCmdNodeProp Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCmdNodeProp"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdNodeProp.html"
---

# EdmCmdNodeProp Enumeration

Types of command node property; used in calls to [IEdmCmdNode::GetProperty](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode~GetProperty.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmCmdNodeProp
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCmdNodeProp : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCmdNodeProp : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCmdNode_ChildDocIDs | 2 = File IDs of child files |
| EdmCmdNode_IsTopNode | 1 = True if a top node, false if not |
| EdmCmdNode_ParentDocIDs | 3 = File IDs of parent files |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

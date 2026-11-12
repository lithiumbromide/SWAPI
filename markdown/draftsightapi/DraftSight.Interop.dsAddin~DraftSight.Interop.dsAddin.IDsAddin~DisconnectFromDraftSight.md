---
title: "DisconnectFromDraftSight Method (IDsAddin)"
project: ""
interface: "IDsAddin"
member: "DisconnectFromDraftSight"
kind: "method"
source: "draftsightapi/DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin~DisconnectFromDraftSight.htm"
---

# DisconnectFromDraftSight Method (IDsAddin)

## Syntax

### Visual Basic

```vb
Function DisconnectFromDraftSight() As System.Boolean
```

### C#

```csharp
System.bool DisconnectFromDraftSight()
```

### JavaScript

```
Not supported
```

### COM native C++

```
HRESULT DisconnectFromDraftSight(
   VAIRANT_BOOL* Val
)
```

### C++

```
DSRESULT DisconnectFromDraftSight(
   bool* Val
)
```

##### Return Value

True if the add-in disconnected successfully, false if not

## See Also

[IDsAddin Interface](DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin.htm)
[IDsAddin Members](DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin_members.htm)

[IDsAddin::ConnectToDraftSight](DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin~ConnectToDraftSight.htm)

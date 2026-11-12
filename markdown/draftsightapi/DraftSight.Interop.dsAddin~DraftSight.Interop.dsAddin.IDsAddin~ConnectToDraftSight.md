---
title: "ConnectToDraftSight Method (IDsAddin)"
project: ""
interface: "IDsAddin"
member: "ConnectToDraftSight"
kind: "method"
source: "draftsightapi/DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin~ConnectToDraftSight.htm"
---

# ConnectToDraftSight Method (IDsAddin)

## Syntax

### Visual Basic

```vb
Function ConnectToDraftSight( _
   ByVal DsApp As System.Object, _
   ByVal Cookie As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ConnectToDraftSight(
   System.object DsApp,
   System.int Cookie
)
```

### JavaScript

```
Not supported
```

### COM native C++

```
HRESULT ConnectToDraftSight(
   IDispatch* DsApp,
   LONG Cookie
   VARIANT_BOOL* Val
)
```

### C++

```
DSRESULT ConnectToDraftSight(
    dsObject* DsApp,
    long Cookie
    bool* Val
)
```

### Parameters

- `DsApp`: Pointer to the DraftSight Dispatch object
- `DsApp`:
- `Cookie`: Add-in ID

##### Return Value

True if the add-in connected successfully, false if not

## See Also

[IDsAddin Interface](DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin.htm)
[IDsAddin Members](DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin_members.htm)
[IDsAddin::DisconnectFromDraftSight](DraftSight.Interop.dsAddin~DraftSight.Interop.dsAddin.IDsAddin~DisconnectFromDraftSight.htm)

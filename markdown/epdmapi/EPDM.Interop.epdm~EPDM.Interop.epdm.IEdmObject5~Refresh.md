---
title: "Refresh Method (IEdmObject5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmObject5"
member: "Refresh"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~Refresh.html"
---

# Refresh Method (IEdmObject5)

Re-reads cached properties from the database.

## Syntax

### Visual Basic

```vb
Sub Refresh()
```

### C#

```csharp
void Refresh()
```

### C++/CLI

```cpp
void Refresh();
```

## Remarks

In a multi-user implementation, the object may change as you are working on it. Call this method to ensure that you are seeing the latest state of the object.

For performance reasons, some object properties might be cached in the object itself. This method ensures that cached properties are re-read from the database.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_EDM_DATABASE_ACCESS: General error accessing the database.

## See Also

[IEdmObject5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html)
[IEdmObject5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional

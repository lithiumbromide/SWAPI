---
title: "RemoveAddIn Method (IEdmAddInMgr9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddInMgr9"
member: "RemoveAddIn"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr9~RemoveAddIn.html"
---

# RemoveAddIn Method (IEdmAddInMgr9)

Removes the specified add-in.

## Syntax

### Visual Basic

```vb
Sub RemoveAddIn( _
   ByVal oNameOrID As System.Object _
)
```

### C#

```csharp
void RemoveAddIn(
   System.object oNameOrID
)
```

### C++/CLI

```cpp
void RemoveAddIn(
   System.Object^ oNameOrID
)
```

### Parameters

- `oNameOrID`: ID or name of the add-in to remove

## Examples

See the [IEdmAddInMgr9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr9.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddInMgr9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr9.html)
[IEdmAddInMgr9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr9_members.html)
[IEdmAddInMgr5::AddAddIns Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInMgr5~AddAddIns.html)

## Availability

SOLIDWORKS PDM Professional 2018

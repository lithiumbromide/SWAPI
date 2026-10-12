---
title: "GetParentInfo Method (IEdmCardControl5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl5"
member: "GetParentInfo"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~GetParentInfo.html"
---

# GetParentInfo Method (IEdmCardControl5)

Gets the parent control of this control.

## Syntax

### Visual Basic

```vb
Sub GetParentInfo( _
   ByRef plParentCtrlID As System.Integer, _
   ByRef plPageNo As System.Integer _
)
```

### C#

```csharp
void GetParentInfo(
   out System.int plParentCtrlID,
   out System.int plPageNo
)
```

### C++/CLI

```cpp
void GetParentInfo(
   [Out] System.int plParentCtrlID,
   [Out] System.int plPageNo
)
```

### Parameters

- `plParentCtrlID`: ID of the parent control; 0 if there is no parent control
- `plPageNo`: 0-based index of the tab control on which this control is located

## Examples

See the [IEdmCardControl6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The control does not have a parent.

## See Also

[IEdmCardControl5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html)
[IEdmCardControl5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

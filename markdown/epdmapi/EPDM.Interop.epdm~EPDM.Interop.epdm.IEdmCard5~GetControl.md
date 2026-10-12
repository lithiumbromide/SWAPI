---
title: "GetControl Method (IEdmCard5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard5"
member: "GetControl"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetControl.html"
---

# GetControl Method (IEdmCard5)

Gets a card control with the specified ID.

## Syntax

### Visual Basic

```vb
Function GetControl( _
   ByVal lControlID As System.Integer _
) As IEdmCardControl5
```

### C#

```csharp
IEdmCardControl5 GetControl(
   System.int lControlID
)
```

### C++/CLI

```cpp
IEdmCardControl5^ GetControl(
   System.int lControlID
)
```

### Parameters

- `lControlID`: ID of card control to get

### Return Value

[IEdmCardControl5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_ID: The supplied control is invalid.
- E_EDM_DATABASE_ACCESS: The supplied control ID is invalid.

## See Also

[IEdmCard5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)
[IEdmCard5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5_members.html)
[IEdmCard5::GetControlID Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetControlID.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

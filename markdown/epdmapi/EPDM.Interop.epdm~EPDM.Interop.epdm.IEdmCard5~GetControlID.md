---
title: "GetControlID Method (IEdmCard5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard5"
member: "GetControlID"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetControlID.html"
---

# GetControlID Method (IEdmCard5)

Gets the ID of the control that is connected to the specified variable in this card.

## Syntax

### Visual Basic

```vb
Function GetControlID( _
   ByRef poVariableNameOrID As System.Object _
) As System.Integer
```

### C#

```csharp
System.int GetControlID(
   ref System.object poVariableNameOrID
)
```

### C++/CLI

```cpp
System.int GetControlID(
   System.Object^% poVariableNameOrID
)
```

### Parameters

- `poVariableNameOrID`: ID or name of the variable for which to get the control ID

### Return Value

Control ID; 0 if the variable isn't used by any control in this card

## Remarks

If more than one control is connected to the same variable, there is no way of knowing for which control this method returns an ID.

The returned ID can be passed to [IEdmCard5::GetControl](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetControl.html) or [IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html) in order to obtain [IEdmCardControl5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The variable was not found.

## See Also

[IEdmCard5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)
[IEdmCard5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

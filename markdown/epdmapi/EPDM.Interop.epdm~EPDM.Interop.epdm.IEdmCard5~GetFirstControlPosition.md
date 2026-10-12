---
title: "GetFirstControlPosition Method (IEdmCard5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard5"
member: "GetFirstControlPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetFirstControlPosition.html"
---

# GetFirstControlPosition Method (IEdmCard5)

Starts an enumeration of the controls in this data card.

## Syntax

### Visual Basic

```vb
Function GetFirstControlPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstControlPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstControlPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first control in the list

## Examples

[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)
[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)

## Remarks

After calling this method, pass the returned position of the first control to [IEdmCard5::GetNextControl](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetNextControl.html) to get the first control in the list. Call IEdmCard5::GetNextControl repeatedly to get the rest of the controls in the list.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCard5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)
[IEdmCard5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5_members.html)
[IEdmCard5::GetNextControl Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetNextControl.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

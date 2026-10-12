---
title: "GetNextControl Method (IEdmCard5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard5"
member: "GetNextControl"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetNextControl.html"
---

# GetNextControl Method (IEdmCard5)

Gets the next control in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextControl( _
   ByVal poPos As IEdmPos5 _
) As IEdmCardControl5
```

### C#

```csharp
IEdmCardControl5 GetNextControl(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmCardControl5^ GetNextControl(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next control in the list

### Return Value

[IEdmCardControl5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html)

## Examples

[Get Card Control Information (VB.NET)](Get_Card_Control_Info_Example_VBNET.htm)
[Get Card Control Information (C#)](Get_Card_Control_Info_Example_CSharp.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first control, IEdmPos5. Call [IEdmCard5::GetFirstControlPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetFirstControlPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the controls.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: There are no more controls to get; [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) is true.

## See Also

[IEdmCard5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)
[IEdmCard5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5_members.html)
[IEdmCard5::GetFirstControlPosition Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5~GetFirstControlPosition.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

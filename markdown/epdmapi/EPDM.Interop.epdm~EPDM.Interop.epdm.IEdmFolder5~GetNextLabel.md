---
title: "GetNextLabel Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetNextLabel"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextLabel.html"
---

# GetNextLabel Method (IEdmFolder5)

Gets the next label in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextLabel( _
   ByVal poPos As IEdmPos5 _
) As IEdmLabel5
```

### C#

```csharp
IEdmLabel5 GetNextLabel(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmLabel5^ GetNextLabel(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of label to retrieve (see **Remarks**)

### Return Value

[IEdmLabel5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)

## Examples

[Create Labels on Folders (VB.NET)](Create_Label_Example_VBNET.htm)
[Create Labels on Folders (C#)](Create_Label_Example_CSharp.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first label, IEdmPos5. Call [IEdmFolder5::GetFirstLabelPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstLabelPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the labels.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers not using smart-pointer wrapper functions must release the returned interface.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

---
title: "GetNext Method (IEdmStrLst5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmStrLst5"
member: "GetNext"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5~GetNext.html"
---

# GetNext Method (IEdmStrLst5)

Gets the next string in this list.

## Syntax

### Visual Basic

```vb
Function GetNext( _
   ByVal poPos As IEdmPos5 _
) As System.String
```

### C#

```csharp
System.string GetNext(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
System.String^ GetNext(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next string in this list (see **Remarks**)

### Return Value

Next string in this list

## Examples

See the [IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html) examples.

## Remarks

Before calling this method the first time, you must populate poPosition with the interface to the position of the first string, IEdmPos5. Call [IEdmStrLst5::GetHeadPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5~GetHeadPosition.html) to start an enumeration and obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the strings.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers must free the returned pointer with a call to SysFreeString.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmStrLst5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html)
[IEdmStrLst5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

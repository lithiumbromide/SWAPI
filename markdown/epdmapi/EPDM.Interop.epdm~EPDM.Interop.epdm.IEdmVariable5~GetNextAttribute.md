---
title: "GetNextAttribute Method (IEdmVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariable5"
member: "GetNextAttribute"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~GetNextAttribute.html"
---

# GetNextAttribute Method (IEdmVariable5)

Gets the next attribute in an enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextAttribute( _
   ByVal poPos As IEdmPos5 _
) As IEdmAttribute5
```

### C#

```csharp
IEdmAttribute5 GetNextAttribute(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmAttribute5^ GetNextAttribute(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position in the enumeration of the next attribute

### Return Value

[IEdmAttribute5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAttribute5.html)

## Examples

[Find Data Cards with Description Variable (C#)](Find_Data_Cards_with_Description_Variable_Example_CSharp.htm)
[Find Data Cards with Description Variable (VB.NET)](Find_Data_Cards_with_Description_Variable_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first attribute in the list, IEdmPos5. Call [IEdmVariable5::GetFirstAttributePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5~GetFirstAttributePosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the attributes in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmAttribute5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5.html)
[IEdmVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

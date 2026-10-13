---
title: "GetNextAttribute Method (IEdmVariableValue5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableValue5"
member: "GetNextAttribute"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5~GetNextAttribute.html"
---

# GetNextAttribute Method (IEdmVariableValue5)

Gets the next attribute to which this variable is mapped in an enumeration.

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

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next attribute in the list

### Return Value

[IEdmAttribute5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAttribute5.html)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first attribute in the list, IEdmPos5. Call [IEdmVariableValue5::GetFirstAttributePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5~GetFirstAttributePosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the attributes in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmVariable5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariableValue5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5.html)
[IEdmVariableValue5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

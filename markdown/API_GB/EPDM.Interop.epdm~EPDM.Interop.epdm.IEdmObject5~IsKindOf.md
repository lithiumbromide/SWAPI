---
title: "IsKindOf Method (IEdmObject5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmObject5"
member: "IsKindOf"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~IsKindOf.html"
---

# IsKindOf Method (IEdmObject5)

Checks whether the object is of a certain type.

## Syntax

### Visual Basic

```vb
Function IsKindOf( _
   ByVal __MIDL__IEdmObject50000 As EdmObjectType _
) As System.Boolean
```

### C#

```csharp
System.bool IsKindOf(
   EdmObjectType __MIDL__IEdmObject50000
)
```

### C++/CLI

```cpp
System.bool IsKindOf(
   EdmObjectType __MIDL__IEdmObject50000
)
```

### Parameters

- `__MIDL__IEdmObject50000`: Type of object as defined in [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html)

### Return Value

True if the object is of the specified type, false if not

## Examples

[Get and Set Item References (C#)](Get_and_Set_Item_References_Example_CSharp.htm)
[Get and Set Item References (VB.NET)](Get_and_Set_Item_References_Example_VBNET.htm)

## Remarks

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmObject5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html)
[IEdmObject5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional

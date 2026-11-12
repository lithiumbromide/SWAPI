---
title: "IsKindOf Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "IsKindOf"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~IsKindOf.html"
---

# IsKindOf Method (IEdmFile5)

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

## Remarks

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK indicates that the method successfully executed.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

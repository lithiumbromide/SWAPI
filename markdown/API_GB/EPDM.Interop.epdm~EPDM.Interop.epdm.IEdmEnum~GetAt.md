---
title: "GetAt Method (IEdmEnum)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnum"
member: "GetAt"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~GetAt.html"
---

# GetAt Method (IEdmEnum)

Gets the element at the specified position in the list.

## Syntax

### Visual Basic

```vb
Function GetAt( _
   ByVal lIndex As System.Integer _
) As System.Object
```

### C#

```csharp
System.object GetAt(
   System.int lIndex
)
```

### C++/CLI

```cpp
System.Object^ GetAt(
   System.int lIndex
)
```

### Parameters

- `lIndex`: Zero-based index of the element to retrieve

### Return Value

Element at the specified position

## Remarks

To enumerate a list, call [IEdmEnum::MoveNext](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~MoveNext.html) and [IEdmEnum::Current](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~Current.html), both of which are more efficient than this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_INVALIDARG: The specified index is outside the range of this list.

## See Also

[IEdmEnum Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum.html)
[IEdmEnum Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum_members.html)

## Availability

SOLIDWORKS PDM Professional 2013

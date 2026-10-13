---
title: "GetProperty Method (IEdmRefItem)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRefItem"
member: "GetProperty"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem~GetProperty.html"
---

# GetProperty Method (IEdmRefItem)

Gets the value of the specified property of this item.

## Syntax

### Visual Basic

```vb
Function GetProperty( _
   ByVal eProperty As EdmRefItemProperty, _
   ByRef poValue As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GetProperty(
   EdmRefItemProperty eProperty,
   out System.object poValue
)
```

### C++/CLI

```cpp
System.bool GetProperty(
   EdmRefItemProperty eProperty,
   [Out] System.Object^ poValue
)
```

### Parameters

- `eProperty`: Type of property for which to get a value as defined in [EdmRefItemProperty](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefItemProperty.html)
- `poValue`: Property value

### Return Value

True if this property can be modified, false if not

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_INVALIDARG: One of the arguments is invalid.

## See Also

[IEdmRefItem Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem.html)
[IEdmRefItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4

---
title: "GetDefaultValueComponent Method (IEdmCardViewCallback6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardViewCallback6"
member: "GetDefaultValueComponent"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6~GetDefaultValueComponent.html"
---

# GetDefaultValueComponent Method (IEdmCardViewCallback6)

Called by the serial number generator to get the default value for the specified serial number component.

## Syntax

### Visual Basic

```vb
Function GetDefaultValueComponent( _
   ByVal eValue As EdmDefValComp _
) As System.Object
```

### C#

```csharp
System.object GetDefaultValueComponent(
   EdmDefValComp eValue
)
```

### C++/CLI

```cpp
System.Object^ GetDefaultValueComponent(
   EdmDefValComp eValue
)
```

### Parameters

- `eValue`: Type of component for which to get a value as defined in [EdmDefValComp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDefValComp.html)

### Return Value

Default value

## Examples

See the [IEdmCardViewCallback6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html) examples.

## Remarks

The user can generate a new serial number value in a card by right-clicking in the edit box linked to the serial number and selecting New Serial Number from the context menu. The serial number generator calls this method if it needs additional information in order to create the serial number. Implement this method to override the default behavior.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardViewCallback6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6.html)
[IEdmCardViewCallback6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardViewCallback6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

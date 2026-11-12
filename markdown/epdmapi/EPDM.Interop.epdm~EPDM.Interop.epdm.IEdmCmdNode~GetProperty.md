---
title: "GetProperty Method (IEdmCmdNode)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCmdNode"
member: "GetProperty"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode~GetProperty.html"
---

# GetProperty Method (IEdmCmdNode)

Gets the specified property for the file changing state.

## Syntax

### Visual Basic

```vb
Function GetProperty( _
   ByVal eProperty As EdmCmdNodeProp, _
   Optional ByVal oArg As System.Object _
) As System.Object
```

### C#

```csharp
System.object GetProperty(
   EdmCmdNodeProp eProperty,
   System.object oArg
)
```

### C++/CLI

```cpp
System.Object^ GetProperty(
   EdmCmdNodeProp eProperty,
   System.Object^ oArg
)
```

### Parameters

- `eProperty`: Type of property to retrieve as defined in [EdmCmdNodeProp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdNodeProp.html)
- `oArg`: Null; reserved for future use

### Return Value

Property value

## Examples

See the [IEdmCmdNode](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCmdNode Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode.html)
[IEdmCmdNode Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode_members.html)

## Availability

SOLIDWORKS PDM Professional 2011

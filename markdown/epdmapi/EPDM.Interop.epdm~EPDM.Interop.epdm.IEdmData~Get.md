---
title: "Get Method (IEdmData)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmData"
member: "Get"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData~Get.html"
---

# Get Method (IEdmData)

Gets a data object property value.

## Syntax

### Visual Basic

```vb
Function Get( _
   ByVal eKey As EdmDataPropertyType _
) As System.Object
```

### C#

```csharp
System.object Get(
   EdmDataPropertyType eKey
)
```

### C++/CLI

```cpp
System.Object^ Get(
   EdmDataPropertyType eKey
)
```

### Parameters

- `eKey`: ID of property to retrieve as defined in [EdmDataPropertyType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDataPropertyType.html)

### Return Value

Property value or empty if not found

## Examples

See the [IEdmData](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData.html) examples.

## Remarks

C++ programmers must remember to intialize the VARIANT struct for poValue with a call to VariantInit before calling the routine and release the returned data with a call to VariantClear.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmData Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData.html)
[IEdmData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData_members.html)
[IEdmData::Set Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData~Set.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

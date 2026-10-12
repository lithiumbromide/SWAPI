---
title: "Set Method (IEdmData)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmData"
member: "Set"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData~Set.html"
---

# Set Method (IEdmData)

Sets one of the data object properties to a new value.

## Syntax

### Visual Basic

```vb
Sub Set( _
   ByVal eKey As EdmDataPropertyType, _
   ByRef poValue As System.Object _
)
```

### C#

```csharp
void Set(
   EdmDataPropertyType eKey,
   ref System.object poValue
)
```

### C++/CLI

```cpp
void Set(
   EdmDataPropertyType eKey,
   System.Object^% poValue
)
```

### Parameters

- `eKey`: ID of property to update as defined in [EdmDataPropertyType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDataPropertyType.html)
- `poValue`: New value of property

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmData Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData.html)
[IEdmData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData_members.html)
[IEdmData::Get Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData~Get.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

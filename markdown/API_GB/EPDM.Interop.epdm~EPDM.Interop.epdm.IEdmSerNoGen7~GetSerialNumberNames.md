---
title: "GetSerialNumberNames Method (IEdmSerNoGen7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSerNoGen7"
member: "GetSerialNumberNames"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen7~GetSerialNumberNames.html"
---

# GetSerialNumberNames Method (IEdmSerNoGen7)

Gets the names of all of the serial number generators installed in the vault.

## Syntax

### Visual Basic

```vb
Sub GetSerialNumberNames( _
   ByRef ppoRetNames As System.String() _
)
```

### C#

```csharp
void GetSerialNumberNames(
   out System.string[] ppoRetNames
)
```

### C++/CLI

```cpp
void GetSerialNumberNames(
   [Out] System.array<String^> ppoRetNames
)
```

### Parameters

- `ppoRetNames`: Array of serial number generator names

## Examples

[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)

## See Also

[IEdmSerNoGen7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen7.html)
[IEdmSerNoGen7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen7_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4

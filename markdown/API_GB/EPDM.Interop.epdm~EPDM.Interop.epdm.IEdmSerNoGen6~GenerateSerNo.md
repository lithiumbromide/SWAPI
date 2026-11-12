---
title: "GenerateSerNo Method (IEdmSerNoGen6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSerNoGen6"
member: "GenerateSerNo"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen6~GenerateSerNo.html"
---

# GenerateSerNo Method (IEdmSerNoGen6)

Obsolete. Superseded by [IEdmSerNoGen7::AllocSerNoValue](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen7~AllocSerNoValue.html).

## Syntax

### Visual Basic

```vb
Function GenerateSerNo( _
   ByVal bsSerNoName As System.String, _
   Optional ByVal lParentWnd As System.Integer, _
   Optional ByVal bsFilePath As System.String, _
   Optional ByVal lFolderID As System.Integer, _
   Optional ByVal lFileID As System.Integer, _
   Optional ByVal lCardID As System.Integer, _
   Optional ByVal lCardControlID As System.Integer _
) As System.String
```

### C#

```csharp
System.string GenerateSerNo(
   System.string bsSerNoName,
   System.int lParentWnd,
   System.string bsFilePath,
   System.int lFolderID,
   System.int lFileID,
   System.int lCardID,
   System.int lCardControlID
)
```

### C++/CLI

```cpp
System.String^ GenerateSerNo(
   System.String^ bsSerNoName,
   System.int lParentWnd,
   System.String^ bsFilePath,
   System.int lFolderID,
   System.int lFileID,
   System.int lCardID,
   System.int lCardControlID
)
```

### Parameters

- `bsSerNoName`: Name of the serial number generator to use to generate a new serial number (see **Remarks**)
- `lParentWnd`: Parent window handle; passed to a serial number add-in, if it exists
- `bsFilePath`: Path to the file for which to generate a serial number
- `lFolderID`: ID of the file's parent folder
- `lFileID`: ID of the file for which to generate a serial number
- `lCardID`: ID of the data card in which the serial number is generated
- `lCardControlID`: ID of the control for which to generate a serial number

### Return Value

Serial number value

## Remarks

This method is superseded by [IEdmSerNoGen7:AllocSerNoValue](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen7~AllocSerNoValue.html) which provides the ability to push back serial numbers that you don't need using [IEdmSerNoValue](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoValue.html).

bsSerNoName is the name you specify in the SOLIDWORKS PDM Professional Administration tool when you create a serial number generator.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_INVALID_SERIAL_NUMBER_NAME: The bsSerNoName argument is invalid.

## See Also

[IEdmSerNoGen6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen6.html)
[IEdmSerNoGen6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0

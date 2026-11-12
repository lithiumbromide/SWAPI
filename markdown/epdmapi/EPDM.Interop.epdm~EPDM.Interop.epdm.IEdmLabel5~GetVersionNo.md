---
title: "GetVersionNo Method (IEdmLabel5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel5"
member: "GetVersionNo"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetVersionNo.html"
---

# GetVersionNo Method (IEdmLabel5)

Gets the version of the specified file on which this label is set.

## Syntax

### Visual Basic

```vb
Function GetVersionNo( _
   ByVal lFileID As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetVersionNo(
   System.int lFileID
)
```

### C++/CLI

```cpp
System.int GetVersionNo(
   System.int lFileID
)
```

### Parameters

- `lFileID`: ID of file for which to get the version

### Return Value

Version number

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_INVALIDARG: The label is not set on the specified file.

## See Also

[IEdmLabel5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5.html)
[IEdmLabel5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

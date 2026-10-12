---
title: "SaveBmp Method (IEdmBitmap5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBitmap5"
member: "SaveBmp"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5~SaveBmp.html"
---

# SaveBmp Method (IEdmBitmap5)

Saves this bitmap image as a BMP file.

## Syntax

### Visual Basic

```vb
Sub SaveBmp( _
   ByVal bsBmpPath As System.String _
)
```

### C#

```csharp
void SaveBmp(
   System.string bsBmpPath
)
```

### C++/CLI

```cpp
void SaveBmp(
   System.String^ bsBmpPath
)
```

### Parameters

- `bsBmpPath`: Path and name of the BMP file; if the file already exists, it is overwritten

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_SHARE_ERROR: Error opening the file.
- E_EDM_IO_ERROR: Error writing the file.

## See Also

[IEdmBitmap5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5.html)
[IEdmBitmap5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

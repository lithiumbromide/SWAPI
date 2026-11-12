---
title: "GetThumbnail Method (IEdmEnumeratorVariable5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVariable5"
member: "GetThumbnail"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetThumbnail.html"
---

# GetThumbnail Method (IEdmEnumeratorVariable5)

Gets a preview bitmap of the current file.

## Syntax

### Visual Basic

```vb
Function GetThumbnail() As IEdmBitmap5
```

### C#

```csharp
IEdmBitmap5 GetThumbnail()
```

### C++/CLI

```cpp
IEdmBitmap5^ GetThumbnail();
```

### Return Value

[IEdmBitmap5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5.html); Null if the file does not support bitmap previews

## Examples

[Get Preview Bitmap of File (VB.NET)](Get_Bitmap_Preview_of_File_Example_VBNET.htm)
[Get Preview Bitmap of File (C#)](Get_Bitmap_Preview_of_File_Example_CSharp.htm)

## Remarks

This method supports only DWG files that are cached.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmBitmap5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The file does not support bitmap previews.

## See Also

[IEdmEnumeratorVariable5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)
[IEdmEnumeratorVariable5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

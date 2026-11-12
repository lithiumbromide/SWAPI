---
title: "GetThumbnail3 Method (IEdmFile18)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile18"
member: "GetThumbnail3"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18~GetThumbnail3.html"
---

# GetThumbnail3 Method (IEdmFile18)

Gets this file's thumbnail handle.

## Syntax

### Visual Basic

```vb
Function GetThumbnail3( _
   ByVal lVersion As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetThumbnail3(
   System.int lVersion
)
```

### C++/CLI

```cpp
System.int GetThumbnail3(
   System.int lVersion
)
```

### Parameters

- `lVersion`: Version of the file whose thumbnail to retrieve

### Return Value

Thumbnail handle

## Examples

[Get File's Thumbnail Handle by File Version (C#)](Get_File_Thumbnail_Handle_by_File_Version_Example_CSharp.htm)

## See Also

[IEdmFile18 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18.html)
[IEdmFile18 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18_members.html)
[IEdmFile15::GetThumbnail2 Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15~GetThumbnail2.html)

## Availability

SOLIDWORKS PDM Professional 2023 SP01

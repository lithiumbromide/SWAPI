---
title: "GetThumbnail2 Method (IEdmFile15)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile15"
member: "GetThumbnail2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15~GetThumbnail2.html"
---

# GetThumbnail2 Method (IEdmFile15)

Obsolete. Superseded by [IEdmFile18::GetThumbnail3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile18~GetThumbnail3.html).

## Syntax

### Visual Basic

```vb
Function GetThumbnail2( _
   ByVal lVersion As System.Integer _
) As System.Object
```

### C#

```csharp
System.object GetThumbnail2(
   System.int lVersion
)
```

### C++/CLI

```cpp
System.Object^ GetThumbnail2(
   System.int lVersion
)
```

### Parameters

- `lVersion`: Version of the file whose thumbnail to retrieve

### Return Value

IPicture

## Examples

[Get a File's Thumbnail by File Version (C#)](Get_File_Thumbnail_by_Version_Example_CSharp.htm)

## Remarks

If a thumbnail of this file is not available, this method returns Nothing or null.

## See Also

[IEdmFile15 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15.html)
[IEdmFile15 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile15_members.html)
[IEdmEnumeratorVariable5::GetThumbnail Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetThumbnail.html)

## Availability

SOLIDWORKS PDM Professional 2018 SP04

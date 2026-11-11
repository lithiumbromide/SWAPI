---
title: "GetPreviewBitmapBytes Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetPreviewBitmapBytes"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapBytes.html"
---

# GetPreviewBitmapBytes Method (IApplication)

Gets a byte array of the preview bitmap for the specified document.

## Syntax

### Visual Basic

```vb
Function GetPreviewBitmapBytes( _
   ByVal DocumentPath As System.String, _
   ByVal Format As dsBitmapFormat_e, _
   ByRef Width As System.Integer, _
   ByRef Height As System.Integer, _
   ByRef BitmapByteArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GetPreviewBitmapBytes(
   System.string DocumentPath,
   dsBitmapFormat_e Format,
   out System.int Width,
   out System.int Height,
   out System.object BitmapByteArray
)
```

### JScript

```
function GetPreviewBitmapBytes(
   DocumentPath : System.String,
   Format : dsBitmapFormat_e,
   Width : System.int,
   Height : System.int,
   BitmapByteArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetPreviewBitmapBytes(
   System.string* DocumentPath,
   dsBitmapFormat_e Format,
   [PARAMFLAG::Out] System.int Width,
   [PARAMFLAG::Out] System.int Height,
   [PARAMFLAG::Out] System.Object* BitmapByteArray
)
```

### C++/CLI

```cpp
System.bool GetPreviewBitmapBytes(
   System.String^ DocumentPath,
   dsBitmapFormat_e Format,
   [Out] System.int Width,
   [Out] System.int Height,
   [Out] System.Object^ BitmapByteArray
)
```

### Parameters

- `DocumentPath`: Path and file name of the document's preview bitmap (.**bmp**)
- `Format`: Format of the preview bitmap as defined in [dsBitmapFormat_e](Interop.dsAutomation~Interop.dsAutomation.dsBitmapFormat_e.html)
- `Width`: Width of the preview bitmap
- `Height`: Height of the preview bitmap
- `BitmapByteArray`: Byte array of the preview bitmap

### Return Value

True if successful, false if not

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetPreviewBitmap Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmap.html)
[IApplication::GetPreviewBitmapFile Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapFile.html)
[IApplication::GetPreviewOfEntities Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewOfEntities.html)

## Availability

DraftSight V1R3.0

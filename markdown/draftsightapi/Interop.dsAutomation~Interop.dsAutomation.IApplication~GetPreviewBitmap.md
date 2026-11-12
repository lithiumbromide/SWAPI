---
title: "GetPreviewBitmap Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetPreviewBitmap"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmap.html"
---

# GetPreviewBitmap Method (IApplication)

Gets the preview bitmap of the specified document.

## Syntax

### Visual Basic

```vb
Function GetPreviewBitmap( _
   ByVal DocumentPath As System.String, _
   ByRef BitmapByteArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool GetPreviewBitmap(
   System.string DocumentPath,
   out System.object BitmapByteArray
)
```

### JScript

```
function GetPreviewBitmap(
   DocumentPath : System.String,
   BitmapByteArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetPreviewBitmap(
   System.string* DocumentPath,
   [PARAMFLAG::Out] System.Object* BitmapByteArray
)
```

### C++/CLI

```cpp
System.bool GetPreviewBitmap(
   System.String^ DocumentPath,
   [Out] System.Object^ BitmapByteArray
)
```

### Parameters

- `DocumentPath`: Path and file name of the document's preview bitmap (.**bmp**)
- `BitmapByteArray`: Byte array of the preview bitmap

### Return Value

True if successful, false if not

## Remarks

Binary data is organized into variable-length chunks. The maximum length of each chunk is 127 bytes.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetPreviewBitmapFile Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapFile.html)
[IApplication::GetPreviewBitmapBytes Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapBytes.html)
[IApplication::GetPreviewOfEntities Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewOfEntities.html)
[IDocumentExporter::ExportToBmp Method](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToBmp.html)

## Availability

DraftSight V1R3.0

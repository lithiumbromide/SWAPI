---
title: "GetPreviewBitmapFile Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetPreviewBitmapFile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapFile.html"
---

# GetPreviewBitmapFile Method (IApplication)

Gets the preview bitmap of the specified document and saves it as a Windows bitmap file (.**bmp**) using the specified file name.

## Syntax

### Visual Basic

```vb
Function GetPreviewBitmapFile( _
   ByVal DocumentPath As System.String, _
   ByVal BitmapFile As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool GetPreviewBitmapFile(
   System.string DocumentPath,
   System.string BitmapFile
)
```

### JScript

```
function GetPreviewBitmapFile(
   DocumentPath : System.String,
   BitmapFile : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetPreviewBitmapFile(
   System.string* DocumentPath,
   System.string* BitmapFile
)
```

### C++/CLI

```cpp
System.bool GetPreviewBitmapFile(
   System.String^ DocumentPath,
   System.String^ BitmapFile
)
```

### Parameters

- `DocumentPath`: Path and file name of the document's preview bitmap **(.bmp**)
- `BitmapFile`: File name to which to save the preview bitmap

### Return Value

True if the preview bitmap is saved, false if not

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetPreviewBitmap Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmap.html)
[IApplication::GetPreviewBitmapBytes Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewBitmapBytes.html)
[IApplication::GetPreviewOfEntities Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetPreviewOfEntities.html)

## Availability

DraftSight V1R3.0

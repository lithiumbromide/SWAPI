---
title: "GetData Method (IDropData)"
project: ""
interface: "IDropData"
member: "GetData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~GetData.html"
---

# GetData Method (IDropData)

Gets the data stored in this drop for the specified MIME type.

## Syntax

### Visual Basic

```vb
Function GetData( _
   ByVal MimeType As System.String _
) As System.Object
```

### C#

```csharp
System.object GetData(
   System.string MimeType
)
```

### JScript

```
function GetData(
   MimeType : System.String
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetData(
   System.string* MimeType
)
```

### C++/CLI

```cpp
System.Object^ GetData(
   System.String^ MimeType
)
```

### Parameters

- `MimeType`: MIME type (see **Remarks**)

### Return Value

Byte array

## Remarks

Use this method to get data for less common or custom MIME types, e.g.:

"text/csv"
"application/x-qt-windows-mime; value="<custom type>""

Common values for MimeType:

"text/plain"
"text/html"
"text/uri-list"
"image/*", where * is the image format (e.g., "image/bmp")
"application/x-color"

Instead of calling this method with the common MimeTypes, use these getters:

[IDropData::Text](Interop.dsAutomation~Interop.dsAutomation.IDropData~Text.html)

[IDropData::Html](Interop.dsAutomation~Interop.dsAutomation.IDropData~Html.html)

[IDropData::Urls](Interop.dsAutomation~Interop.dsAutomation.IDropData~Urls.html)

[IDropData::ImageData](Interop.dsAutomation~Interop.dsAutomation.IDropData~ImageData.html)

[IDropData::ColorData](Interop.dsAutomation~Interop.dsAutomation.IDropData~ColorData.html)

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)

## Availability

DraftSight 2020 SP3

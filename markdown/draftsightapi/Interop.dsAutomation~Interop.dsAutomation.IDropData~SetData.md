---
title: "SetData Method (IDropData)"
project: ""
interface: "IDropData"
member: "SetData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~SetData.html"
---

# SetData Method (IDropData)

Sets the data stored in this drop for the specified MIME type.

## Syntax

### Visual Basic

```vb
Sub SetData( _
   ByVal MimeType As System.String, _
   ByVal NewVal As System.Object _
)
```

### C#

```csharp
void SetData(
   System.string MimeType,
   System.object NewVal
)
```

### JScript

```
function SetData(
   MimeType : System.String,
   NewVal : System.Object
);
```

### Managed Extensions for C++

```
void SetData(
   System.string* MimeType,
   System.Object* NewVal
)
```

### C++/CLI

```cpp
void SetData(
   System.String^ MimeType,
   System.Object^ NewVal
)
```

### Parameters

- `MimeType`: MIME type (see **Remarks**)
- `NewVal`: Byte array

## Remarks

Use this method to set data for less common or custom MIME types, e.g.:

"text/csv"
"application/x-qt-windows-mime; value="<custom type>""

Common values for MimeType:

"text/plain"
"text/html"
"text/uri-list"
"image/*", where * is the image format (e.g., "image/bmp")
"application/x-color"

Instead of calling this method with the common MimeTypes, use these setters:

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

---
title: "RemoveFormat Method (IDropData)"
project: ""
interface: "IDropData"
member: "RemoveFormat"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~RemoveFormat.html"
---

# RemoveFormat Method (IDropData)

Removes the data entry for the specified MIME type.

## Syntax

### Visual Basic

```vb
Sub RemoveFormat( _
   ByVal MimeType As System.String _
)
```

### C#

```csharp
void RemoveFormat(
   System.string MimeType
)
```

### JScript

```
function RemoveFormat(
   MimeType : System.String
);
```

### Managed Extensions for C++

```
void RemoveFormat(
   System.string* MimeType
)
```

### C++/CLI

```cpp
void RemoveFormat(
   System.String^ MimeType
)
```

### Parameters

- `MimeType`: MIME type (see **Remarks**)

## Remarks

Common values for MimeType:

- "text/plain"
- "text/html"
- "text/uri-list"
- "image/*", where * is the image format (e.g., "image/bmp")
- "application/x-color"

Less common or custom values for MimeType may also be specified:

"text/csv"

"application/x-qt-windows-mime;value="<custom type>""

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)

## Availability

DraftSight 2020 SP3

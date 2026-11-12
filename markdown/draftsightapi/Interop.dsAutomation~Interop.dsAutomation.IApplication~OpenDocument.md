---
title: "OpenDocument Method (IApplication)"
project: ""
interface: "IApplication"
member: "OpenDocument"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenDocument.html"
---

# OpenDocument Method (IApplication)

Obsolete. Superseded by [IApplication::OpenDocument2](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenDocument2.html).

## Syntax

### Visual Basic

```vb
Function OpenDocument( _
   ByVal PathName As System.String, _
   ByVal Option As dsDocumentOpenOption_e _
) As Document
```

### C#

```csharp
Document OpenDocument(
   System.string PathName,
   dsDocumentOpenOption_e Option
)
```

### JScript

```
function OpenDocument(
   PathName : System.String,
   Option : dsDocumentOpenOption_e
) : Document;
```

### Managed Extensions for C++

```
Document* OpenDocument(
   System.string* PathName,
   dsDocumentOpenOption_e Option
)
```

### C++/CLI

```cpp
Document^ OpenDocument(
   System.String^ PathName,
   dsDocumentOpenOption_e Option
)
```

### Parameters

- `PathName`: Path and file name of document to open
- `Option`: Mode in which to open the document as defined in [dsDocumentOpenOption_e](Interop.dsAutomation~interop.dsAutomation.dsDocumentOpenOption_e.html)

### Return Value

[Document](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R1

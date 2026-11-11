---
title: "NewDocument Method (IApplication)"
project: ""
interface: "IApplication"
member: "NewDocument"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~NewDocument.html"
---

# NewDocument Method (IApplication)

Creates a new document using the specified template.

## Syntax

### Visual Basic

```vb
Function NewDocument( _
   ByVal TemplateName As System.String _
) As Document
```

### C#

```csharp
Document NewDocument(
   System.string TemplateName
)
```

### JScript

```
function NewDocument(
   TemplateName : System.String
) : Document;
```

### Managed Extensions for C++

```
Document* NewDocument(
   System.string* TemplateName
)
```

### C++/CLI

```cpp
Document^ NewDocument(
   System.String^ TemplateName
)
```

### Parameters

- `TemplateName`: Path and file name of the template to use for the new document

### Return Value

[Document](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)

## Remarks

If the file specified for TemplateName does not exist, then a new document is not created.

To find out where the DraftSight templates are stored on your computer, interactively create a new document and make note of the path to the DraftSight template files and their file names.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

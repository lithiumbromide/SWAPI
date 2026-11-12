---
title: "SaveAs Method (IDocument)"
project: ""
interface: "IDocument"
member: "SaveAs"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SaveAs.html"
---

# SaveAs Method (IDocument)

Obsoleted. Superseded by [IDocument::SaveAs2](Interop.dsAutomation~Interop.dsAutomation.IDocument~SaveAs2.html).

## Syntax

### Visual Basic

```vb
Sub SaveAs( _
   ByVal Name As System.String, _
   ByVal Options As dsDocumentSaveAsOption_e, _
   ByRef Errors As dsDocumentSaveError_e _
)
```

### C#

```csharp
void SaveAs(
   System.string Name,
   dsDocumentSaveAsOption_e Options,
   out dsDocumentSaveError_e Errors
)
```

### JScript

```
function SaveAs(
   Name : System.String,
   Options : dsDocumentSaveAsOption_e,
   Errors : dsDocumentSaveError_e
);
```

### Managed Extensions for C++

```
void SaveAs(
   System.string* Name,
   dsDocumentSaveAsOption_e Options,
   [PARAMFLAG::Out] dsDocumentSaveError_e Errors
)
```

### C++/CLI

```cpp
void SaveAs(
   System.String^ Name,
   dsDocumentSaveAsOption_e Options,
   [Out] dsDocumentSaveError_e Errors
)
```

### Parameters

- `Name`: File name to which to save the document
- `Options`: File type to which to save the document as defined in [dsDocumentSaveAsOption_e](Interop.dsAutomation~Interop.dsAutomation.dsDocumentSaveAsOption_e.html)
- `Errors`: Status of saving the document as defined in [dsDocumentSaveError_e](Interop.dsAutomation~Interop.dsAutomation.dsDocumentSaveError_e.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::Save Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~Save.html)

## Availability

DraftSight V1R1

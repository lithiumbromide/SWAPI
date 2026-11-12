---
title: "SaveAs2 Method (IDocument)"
project: ""
interface: "IDocument"
member: "SaveAs2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SaveAs2.html"
---

# SaveAs2 Method (IDocument)

Saves the document as the specified file name and file type.

## Syntax

### Visual Basic

```vb
Sub SaveAs2( _
   ByVal Name As System.String, _
   ByVal Options As dsDocumentSaveAsOption_e, _
   ByVal Overwrite As System.Boolean, _
   ByRef Errors As dsDocumentSaveError_e _
)
```

### C#

```csharp
void SaveAs2(
   System.string Name,
   dsDocumentSaveAsOption_e Options,
   System.bool Overwrite,
   out dsDocumentSaveError_e Errors
)
```

### JScript

```
function SaveAs2(
   Name : System.String,
   Options : dsDocumentSaveAsOption_e,
   Overwrite : System.boolean,
   Errors : dsDocumentSaveError_e
);
```

### Managed Extensions for C++

```
void SaveAs2(
   System.string* Name,
   dsDocumentSaveAsOption_e Options,
   System.bool Overwrite,
   [PARAMFLAG::Out] dsDocumentSaveError_e Errors
)
```

### C++/CLI

```cpp
void SaveAs2(
   System.String^ Name,
   dsDocumentSaveAsOption_e Options,
   System.bool Overwrite,
   [Out] dsDocumentSaveError_e Errors
)
```

### Parameters

- `Name`: Path and file name to which to save the document
- `Options`: File type to which to save the document as defined in [dsDocumentSaveAsOption_e](Interop.dsAutomation~Interop.dsAutomation.dsDocumentSaveAsOption_e.html)
- `Overwrite`: True to overwrite an already existing file of the same name in the specified path, false to not
- `Errors`: Status of saving the document as defined in [dsDocumentSaveError_e](Interop.dsAutomation~Interop.dsAutomation.dsDocumentSaveError_e.html)

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::Save Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~Save.html)
[IDocument::WriteBlockByAllEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByAllEntities.html)
[IDocument::WriteBlockByName Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByName.html)
[IDocument::WriteBlockBySpecifiedEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockBySpecifiedEntities.html)

## Availability

DraftSight V1R1.3

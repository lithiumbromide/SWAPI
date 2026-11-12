---
title: "GetImmediateChildReferences Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetImmediateChildReferences"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetImmediateChildReferences.html"
---

# GetImmediateChildReferences Method (IDocument)

Gets the immediate child external references for this document.

## Syntax

### Visual Basic

```vb
Sub GetImmediateChildReferences( _
   ByRef ExternalDefinitionTypeLongArray As System.Object, _
   ByRef ExternalDefinitionsArray As System.Object _
)
```

### C#

```csharp
void GetImmediateChildReferences(
   out System.object ExternalDefinitionTypeLongArray,
   out System.object ExternalDefinitionsArray
)
```

### JScript

```
function GetImmediateChildReferences(
   ExternalDefinitionTypeLongArray : System.Object,
   ExternalDefinitionsArray : System.Object
);
```

### Managed Extensions for C++

```
void GetImmediateChildReferences(
   [PARAMFLAG::Out] System.Object* ExternalDefinitionTypeLongArray,
   [PARAMFLAG::Out] System.Object* ExternalDefinitionsArray
)
```

### C++/CLI

```cpp
void GetImmediateChildReferences(
   [Out] System.Object^ ExternalDefinitionTypeLongArray,
   [Out] System.Object^ ExternalDefinitionsArray
)
```

### Parameters

- `ExternalDefinitionTypeLongArray`: Array of external definition types as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html) that map onto elements of ExternalDefinitionsArray. Possible values:

  - dsDgnDefinitionType
  - dsPdfDefinitionType
  - dsImageDefinitionType
- `ExternalDefinitionsArray`: Array of external definitions that map onto elements of ExternalDefinitionTypeLongArray. Possible values:

  - [IDgnDefinition](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
  - [IPdfDefinition](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition.html)
  - [IImageDefinition](Interop.dsAutomation~Interop.dsAutomation.IImageDefinition.html)

## Examples

Also see the [ISketchManager::InsertPdf](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPdf.html) example.

## Examples

[Insert Picture (VBA)](Insert_Picture_Example_VBA.htm)
[Insert Picture (VB.NET)](Insert_Picture_Example_VBNET.htm)
[Insert Picture (C#)](Insert_Picture_Example_CSharp.htm)

## Remarks

This method is valid only for documents to which one or more DGN, PDF, or Image files have been attached. Before calling this method, use one or more of the following methods to attach files:

- [ISketchManager::InsertDgn](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertDgn.html)
- [ISketchManager::InsertPdf](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPdf.html)
- [ISketchManager::InsertPicture](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPicture.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetExternalReferences Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetExternalReferences.html)

## Availability

DraftSight 2020 SP0

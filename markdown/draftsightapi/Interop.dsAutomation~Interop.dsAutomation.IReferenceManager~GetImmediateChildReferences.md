---
title: "GetImmediateChildReferences Method (IReferenceManager)"
project: ""
interface: "IReferenceManager"
member: "GetImmediateChildReferences"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceManager~GetImmediateChildReferences.html"
---

# GetImmediateChildReferences Method (IReferenceManager)

Gets the nearest child external references of the specified unopened drawing file.

## Syntax

### Visual Basic

```vb
Sub GetImmediateChildReferences( _
   ByVal DrawingFilePath As System.String, _
   ByRef ExternalDefinitionTypeLongArray As System.Object, _
   ByRef ExternalDefinitionsArray As System.Object _
)
```

### C#

```csharp
void GetImmediateChildReferences(
   System.string DrawingFilePath,
   out System.object ExternalDefinitionTypeLongArray,
   out System.object ExternalDefinitionsArray
)
```

### JScript

```
function GetImmediateChildReferences(
   DrawingFilePath : System.String,
   ExternalDefinitionTypeLongArray : System.Object,
   ExternalDefinitionsArray : System.Object
);
```

### Managed Extensions for C++

```
void GetImmediateChildReferences(
   System.string* DrawingFilePath,
   [PARAMFLAG::Out] System.Object* ExternalDefinitionTypeLongArray,
   [PARAMFLAG::Out] System.Object* ExternalDefinitionsArray
)
```

### C++/CLI

```cpp
void GetImmediateChildReferences(
   System.String^ DrawingFilePath,
   [Out] System.Object^ ExternalDefinitionTypeLongArray,
   [Out] System.Object^ ExternalDefinitionsArray
)
```

### Parameters

- `DrawingFilePath`: Full path name of the drawing file for which to retrieve the nearest external child references
- `ExternalDefinitionTypeLongArray`: Array of external definition types as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html) that map onto elements of ExternalDefinitionsArray. Possible values:

  - dsDgnDefinitionType
  - dsPdfDefinitionType
  - dsImageDefinitionType
- `ExternalDefinitionsArray`: Array of external definitions that map onto elements of ExternalDefinitionTypeLongArray. Possible values:

  - [IDgnDefinition](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
  - [IPdfDefinition](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition.html)
  - [IImageDefinition](Interop.dsAutomation~Interop.dsAutomation.IImageDefinition.html)

## Examples

See the [IReferenceManager](Interop.dsAutomation~Interop.dsAutomation.IReferenceManager.html) examples.

## Remarks

This method allows you to retrieve the nearest child external references of unopened DrawingFilePath. To retrieve the nearest child external references of an opened drawing, use [IDocument::GetImmediateChildReferences](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetImmediateChildReferences.html).

## See Also

[IReferenceManager Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceManager.html)
[IReferenceManager Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceManager_members.html)

## Availability

DraftSight 2020 SP1

---
title: "HasBlockDefinition Method (IDocument)"
project: ""
interface: "IDocument"
member: "HasBlockDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~HasBlockDefinition.html"
---

# HasBlockDefinition Method (IDocument)

Gets whether the specified Block definition is inserted in the document.

## Syntax

### Visual Basic

```vb
Function HasBlockDefinition( _
   ByVal BlockName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool HasBlockDefinition(
   System.string BlockName
)
```

### JScript

```
function HasBlockDefinition(
   BlockName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool HasBlockDefinition(
   System.string* BlockName
)
```

### C++/CLI

```cpp
System.bool HasBlockDefinition(
   System.String^ BlockName
)
```

### Parameters

- `BlockName`: Name of the Block definition

### Return Value

True if BlockName is inserted in the document, false if not

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CreateBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateBlockDefinition.html)
[IDocument::GetBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinition.html)
[IDocument::GetBlockDefinitions Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinitions.html)

## Availability

DraftSight V1R5.0

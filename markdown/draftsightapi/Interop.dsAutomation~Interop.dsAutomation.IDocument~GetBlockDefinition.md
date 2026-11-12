---
title: "GetBlockDefinition Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetBlockDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinition.html"
---

# GetBlockDefinition Method (IDocument)

Gets the specified Block definition for the document.

## Syntax

### Visual Basic

```vb
Function GetBlockDefinition( _
   ByVal BlockName As System.String _
) As BlockDefinition
```

### C#

```csharp
BlockDefinition GetBlockDefinition(
   System.string BlockName
)
```

### JScript

```
function GetBlockDefinition(
   BlockName : System.String
) : BlockDefinition;
```

### Managed Extensions for C++

```
BlockDefinition* GetBlockDefinition(
   System.string* BlockName
)
```

### C++/CLI

```cpp
BlockDefinition^ GetBlockDefinition(
   System.String^ BlockName
)
```

### Parameters

- `BlockName`: Name of the Block definition

### Return Value

[Block definition](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetBlockDefinitions Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinitions.html)
[IDocument::HasBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasBlockDefinition.html)
[IDocument::CreateBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateBlockDefinition.html)

## Availability

DraftSight V1R5.0

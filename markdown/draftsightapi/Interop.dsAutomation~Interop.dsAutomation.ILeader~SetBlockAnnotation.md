---
title: "SetBlockAnnotation Method (ILeader)"
project: ""
interface: "ILeader"
member: "SetBlockAnnotation"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~SetBlockAnnotation.html"
---

# SetBlockAnnotation Method (ILeader)

Attaches a [Block instance](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html) to the Leader.

## Syntax

### Visual Basic

```vb
Sub SetBlockAnnotation( _
   ByVal BlockName As System.String, _
   ByVal InsertPoint As MathPoint _
)
```

### C#

```csharp
void SetBlockAnnotation(
   System.string BlockName,
   MathPoint InsertPoint
)
```

### JScript

```
function SetBlockAnnotation(
   BlockName : System.String,
   InsertPoint : MathPoint
);
```

### Managed Extensions for C++

```
void SetBlockAnnotation(
   System.string* BlockName,
   MathPoint* InsertPoint
)
```

### C++/CLI

```cpp
void SetBlockAnnotation(
   System.String^ BlockName,
   MathPoint^ InsertPoint
)
```

### Parameters

- `BlockName`: Name of the [Block definition](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html) to attach to the Leader (see **Remarks**)
- `InsertPoint`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) where to attach the Block to the Leader

## Examples

[Attach Block Definition Annotation to Leader (C#)](Attach_Block_Definition_Annotation_to_Leader_Example_CSharp.htm)
[Attach Block Definition Annotation to Leader (VB.NET)](Attach_Block_Definition_Annotation_to_Leader_Example_VBNET.htm)
[Attach Block Definition Annotation to Leader (VBA)](Attach_Block_Definition_Annotation_to_Leader_Example_VBA.htm)
[Attach Block Definition Annotatin to Leader (JavaScript)](Attach_Block_Definition_Annotation_to_Leader_Example_JS.htm)

## Remarks

You can create a Block definition using [IDocument::CreateBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateBlockDefinition.html). The name you specify for the BlockName parameter for IDocument::CreateBlockDefinition is the same name that you should specify for the BlockName parameter for ILeader::SetBlockAnnotation. When ILeader::SetBlockAnnotation executes, it creates a Block instance of the specified Block definition.

If a Block definition already exists, then you can get the existing Block definitions for a document using [IDocument::GetBlockDefinitions](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinitions.html) and the name of each existing Block definition using [IBlockDefinition::GetName](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetName.html). Use the desired name returned by IBlockDefinition::GetName for the BlockName parameter for ILeader::SetBlockAnnotation.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::GetBlockAnnotation Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetBlockAnnotation.html)
[ILeader::RemoveAnnotation Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~RemoveAnnotation.html)

## Availability

DraftSight V1R3.1

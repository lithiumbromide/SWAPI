---
title: "CreateBlockDefinition Method (IDocument)"
project: ""
interface: "IDocument"
member: "CreateBlockDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateBlockDefinition.html"
---

# CreateBlockDefinition Method (IDocument)

Creates a Block definition.

## Syntax

### Visual Basic

```vb
Function CreateBlockDefinition( _
   ByVal BlockName As System.String, _
   ByVal Description As System.String, _
   ByVal BasePointX As System.Double, _
   ByVal BasePointY As System.Double, _
   ByVal BasePointZ As System.Double, _
   ByVal EntityTypeLongArray As System.Object, _
   ByVal EntitiesArray As System.Object, _
   ByVal BlockDefinitionEntities As dsBlockDefinitionEntities_e _
) As BlockDefinition
```

### C#

```csharp
BlockDefinition CreateBlockDefinition(
   System.string BlockName,
   System.string Description,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.object EntityTypeLongArray,
   System.object EntitiesArray,
   dsBlockDefinitionEntities_e BlockDefinitionEntities
)
```

### JScript

```
function CreateBlockDefinition(
   BlockName : System.String,
   Description : System.String,
   BasePointX : System.double,
   BasePointY : System.double,
   BasePointZ : System.double,
   EntityTypeLongArray : System.Object,
   EntitiesArray : System.Object,
   BlockDefinitionEntities : dsBlockDefinitionEntities_e
) : BlockDefinition;
```

### Managed Extensions for C++

```
BlockDefinition* CreateBlockDefinition(
   System.string* BlockName,
   System.string* Description,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.Object* EntityTypeLongArray,
   System.Object* EntitiesArray,
   dsBlockDefinitionEntities_e BlockDefinitionEntities
)
```

### C++/CLI

```cpp
BlockDefinition^ CreateBlockDefinition(
   System.String^ BlockName,
   System.String^ Description,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   System.Object^ EntityTypeLongArray,
   System.Object^ EntitiesArray,
   dsBlockDefinitionEntities_e BlockDefinitionEntities
)
```

### Parameters

- `BlockName`: Name of the Block definition
- `Description`: Description of Block definition
- `BasePointX`: x coordinate for the base point of the Block definition
- `BasePointY`: y coordinate for the base point of the Block definition
- `BasePointZ`: z coordinate for the base point of the Block definition
- `EntityTypeLongArray`: Array of longs of the types of source entities in the Block definition as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)
- `EntitiesArray`: Array of objects of the source entities in the Block definition
- `BlockDefinitionEntities`: Options for the source entities of the Block definition as defined in [dsBlockDefinitionEntities_e](Interop.dsAutomation~Interop.dsAutomation.dsBlockDefinitionEntities_e.html)

### Return Value

[Block definition](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)

## Examples

[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Attach Block Definition Annotation to Leader (C#)](Attach_Block_Definition_Annotation_to_Leader_Example_CSharp.htm)
[Attach Block Definition Annotation to Leader (VB.NET)](Attach_Block_Definition_Annotation_to_Leader_Example_VBNET.htm)
[Attach Block Definition Annotation to Leader (VBA)](Attach_Block_Definition_Annotation_to_Leader_Example_VBA.htm)
[Attach Block Definition Annotation to Leader (JavaScript)](Attach_Block_Definition_Annotation_to_Leader_Example_JS.htm)

## Remarks

If a Block definition with the specified name already exists in the drawing, then that Block definition is overwritten by this method.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinition.html)
[IDocument::GetBlockDefinitions Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBlockDefinitions.html)
[IDocument::HasBlockDefinition Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasBlockDefinition.html)

## Availability

DraftSight V1R1.3

---
title: "WriteBlockBySpecifiedEntities Method (IDocument)"
project: ""
interface: "IDocument"
member: "WriteBlockBySpecifiedEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockBySpecifiedEntities.html"
---

# WriteBlockBySpecifiedEntities Method (IDocument)

Saves the specified entities in this drawing to a new drawing file.

## Syntax

### Visual Basic

```vb
Sub WriteBlockBySpecifiedEntities( _
   ByVal EntitiesArray As System.Object, _
   ByVal Units As System.Integer, _
   ByVal WriteBlockMode As dsWriteBlockMode_e, _
   ByVal InsertionPoint As Point, _
   ByVal Destination As System.String _
)
```

### C#

```csharp
void WriteBlockBySpecifiedEntities(
   System.object EntitiesArray,
   System.int Units,
   dsWriteBlockMode_e WriteBlockMode,
   Point InsertionPoint,
   System.string Destination
)
```

### JScript

```
function WriteBlockBySpecifiedEntities(
   EntitiesArray : System.Object,
   Units : System.int,
   WriteBlockMode : dsWriteBlockMode_e,
   InsertionPoint : Point,
   Destination : System.String
);
```

### Managed Extensions for C++

```
void WriteBlockBySpecifiedEntities(
   System.Object* EntitiesArray,
   System.int Units,
   dsWriteBlockMode_e WriteBlockMode,
   Point* InsertionPoint,
   System.string* Destination
)
```

### C++/CLI

```cpp
void WriteBlockBySpecifiedEntities(
   System.Object^ EntitiesArray,
   System.int Units,
   dsWriteBlockMode_e WriteBlockMode,
   Point^ InsertionPoint,
   System.String^ Destination
)
```

### Parameters

- `EntitiesArray`: Array of entities to export (see **Remarks**)
- `Units`: Units as defined in [dsBlockInsertUnits_e](Interop.dsAutomation~Interop.dsAutomation.dsBlockInsertUnits_e.html) to use for automatic scaling when the file is inserted in a drawing that uses different units
- `WriteBlockMode`: Handling of drawing entities after they are exported as defined in [dsWriteBlockMode_e](Interop.dsAutomation~Interop.dsAutomation.dsWriteBlockMode_e.html)
- `InsertionPoint`: Insertion base [point](Interop.dsAutomation~Interop.dsAutomation.IPoint.html) for changing the Block's scale and rotation
- `Destination`: Path and filename where to save the specified entities, e.g., "c:\my_block.dwg"

## Remarks

Call [ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html), [IBlockDefinition::GetEntities](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetEntities.html), or [ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html) to specify EntitiesArray.

This method corresponds to the _EXPORTDRAWING command.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::WriteBlockByAllEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByAllEntities.html)
[IDocument::WriteBlockByName Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByName.html)
[IDocument::SaveAs2 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SaveAs2.html)

## Availability

DraftSight 2017 SP2

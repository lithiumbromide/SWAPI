---
title: "WriteBlockByName Method (IDocument)"
project: ""
interface: "IDocument"
member: "WriteBlockByName"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByName.html"
---

# WriteBlockByName Method (IDocument)

Saves the specified Block in this drawing to a new drawing file.

## Syntax

### Visual Basic

```vb
Sub WriteBlockByName( _
   ByVal BlockName As System.String, _
   ByVal Units As System.Integer, _
   ByVal Destination As System.String _
)
```

### C#

```csharp
void WriteBlockByName(
   System.string BlockName,
   System.int Units,
   System.string Destination
)
```

### JScript

```
function WriteBlockByName(
   BlockName : System.String,
   Units : System.int,
   Destination : System.String
);
```

### Managed Extensions for C++

```
void WriteBlockByName(
   System.string* BlockName,
   System.int Units,
   System.string* Destination
)
```

### C++/CLI

```cpp
void WriteBlockByName(
   System.String^ BlockName,
   System.int Units,
   System.String^ Destination
)
```

### Parameters

- `BlockName`: Name of the Block to save to a drawing file (see **Remarks**)
- `Units`: Units as defined in [dsBlockInsertUnits_e](Interop.dsAutomation~Interop.dsAutomation.dsBlockInsertUnits_e.html) to use for automatic scaling when the file is inserted in a drawing that uses different units
- `Destination`: Path and filename where to save this block, e.g., "c:\my_block.dwg"

## Remarks

Use [IBlockDefinition::GetName](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetName.html) to specify BlockName.

This method corresponds to the _EXPORTDRAWING command.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::WriteBlockByAllEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByAllEntities.html)
[IDocument::WriteBlockBySpecifiedEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockBySpecifiedEntities.html)
[IDocument::SaveAs2 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SaveAs2.html)

## Availability

DraftSight 2017 SP2

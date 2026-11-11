---
title: "WriteBlockByAllEntities Method (IDocument)"
project: ""
interface: "IDocument"
member: "WriteBlockByAllEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByAllEntities.html"
---

# WriteBlockByAllEntities Method (IDocument)

Saves this entire drawing to a new drawing file.

## Syntax

### Visual Basic

```vb
Sub WriteBlockByAllEntities( _
   ByVal Units As System.Integer, _
   ByVal Destination As System.String _
)
```

### C#

```csharp
void WriteBlockByAllEntities(
   System.int Units,
   System.string Destination
)
```

### JScript

```
function WriteBlockByAllEntities(
   Units : System.int,
   Destination : System.String
);
```

### Managed Extensions for C++

```
void WriteBlockByAllEntities(
   System.int Units,
   System.string* Destination
)
```

### C++/CLI

```cpp
void WriteBlockByAllEntities(
   System.int Units,
   System.String^ Destination
)
```

### Parameters

- `Units`: Units as defined in [dsBlockInsertUnits_e](Interop.dsAutomation~Interop.dsAutomation.dsBlockInsertUnits_e.html) to use for automatic scaling when the file is inserted in a drawing that uses different units
- `Destination`: Path and filename where to save this drawing, e.g., "c:\my_block.dwg"

## Remarks

This method corresponds to the _EXPORTDRAWING command.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::WriteBlockByName Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockByName.html)
[IDocument::WriteBlockBySpecifiedEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~WriteBlockBySpecifiedEntities.html)
[IDocument::SaveAs2 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SaveAs2.html)

## Availability

DraftSight 2017 SP2

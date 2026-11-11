---
title: "CreateHighlightSet Method (IDocument)"
project: ""
interface: "IDocument"
member: "CreateHighlightSet"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateHighlightSet.html"
---

# CreateHighlightSet Method (IDocument)

Creates a highlight selection set containing the specified entities.

## Syntax

### Visual Basic

```vb
Function CreateHighlightSet( _
   ByVal EntitiesArray As System.Object _
) As HighlightSet
```

### C#

```csharp
HighlightSet CreateHighlightSet(
   System.object EntitiesArray
)
```

### JScript

```
function CreateHighlightSet(
   EntitiesArray : System.Object
) : HighlightSet;
```

### Managed Extensions for C++

```
HighlightSet* CreateHighlightSet(
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
HighlightSet^ CreateHighlightSet(
   System.Object^ EntitiesArray
)
```

### Parameters

- `EntitiesArray`: Entities to add to the highlight selection set

### Return Value

[Highlight selection set](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet.html)

## Examples

[Create Highlight Selection Set (C#)](Create_Highlight_Selection_Set_Example_CSharp.htm)
[Create Highlight Selection Set (VB.NET)](Create_Highlight_Selection_Set_Example_VBNET.htm)
[Create Highlight Selection Set (VBA)](Create_Highlight_Selection_Set_Example_VBA.htm)

## Remarks

Creating a highlight selection set allows you to [highlight](Interop.dsAutomation~Interop.dsAutomation.IHighlightSet~Highlight.html) specific entities in a drawing.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R5.0

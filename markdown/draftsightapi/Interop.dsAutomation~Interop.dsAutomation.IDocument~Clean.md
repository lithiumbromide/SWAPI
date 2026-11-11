---
title: "Clean Method (IDocument)"
project: ""
interface: "IDocument"
member: "Clean"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~Clean.html"
---

# Clean Method (IDocument)

Purges this document of the objects that are defined or loaded but not used.

## Syntax

### Visual Basic

```vb
Sub Clean( _
   ByVal EntityTypesForClean As System.Integer, _
   ByVal DeleteDependedEntities As System.Boolean _
)
```

### C#

```csharp
void Clean(
   System.int EntityTypesForClean,
   System.bool DeleteDependedEntities
)
```

### JScript

```
function Clean(
   EntityTypesForClean : System.int,
   DeleteDependedEntities : System.boolean
);
```

### Managed Extensions for C++

```
void Clean(
   System.int EntityTypesForClean,
   System.bool DeleteDependedEntities
)
```

### C++/CLI

```cpp
void Clean(
   System.int EntityTypesForClean,
   System.bool DeleteDependedEntities
)
```

### Parameters

- `EntityTypesForClean`: Types of objects to purge as defined in [dsCleanObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsCleanObjectType_e.html); 0 for all types
- `DeleteDependedEntities`: True to purge dependent objects, false to not

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1.4

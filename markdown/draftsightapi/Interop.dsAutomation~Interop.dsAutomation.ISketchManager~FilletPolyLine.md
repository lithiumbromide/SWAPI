---
title: "FilletPolyLine Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "FilletPolyLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletPolyLine.html"
---

# FilletPolyLine Method (ISketchManager)

Fillets the specified 2D PolyLine.

## Syntax

### Visual Basic

```vb
Sub FilletPolyLine( _
   ByVal PolyLine As PolyLine _
)
```

### C#

```csharp
void FilletPolyLine(
   PolyLine PolyLine
)
```

### JScript

```
function FilletPolyLine(
   PolyLine : PolyLine
);
```

### Managed Extensions for C++

```
void FilletPolyLine(
   PolyLine* PolyLine
)
```

### C++/CLI

```cpp
void FilletPolyLine(
   PolyLine^ PolyLine
)
```

### Parameters

- `PolyLine`: [2D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html) to fillet

## Remarks

Fillets all vertices of a 2D PolyLine in one step by inserting fillet Arcs at each vertex of the 2D PolyLine where two Lines meet, if applicable.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::FilletEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletEntities.html)
[ISketchManager::ChamferPolyLine Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferPolyLine.html)

## Availability

DraftSight V1R6.0

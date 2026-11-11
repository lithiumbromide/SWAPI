---
title: "ChamferPolyLine Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "ChamferPolyLine"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferPolyLine.html"
---

# ChamferPolyLine Method (ISketchManager)

Chamfers the specified 2D PolyLine.

## Syntax

### Visual Basic

```vb
Sub ChamferPolyLine( _
   ByVal PolyLine As PolyLine _
)
```

### C#

```csharp
void ChamferPolyLine(
   PolyLine PolyLine
)
```

### JScript

```
function ChamferPolyLine(
   PolyLine : PolyLine
);
```

### Managed Extensions for C++

```
void ChamferPolyLine(
   PolyLine* PolyLine
)
```

### C++/CLI

```cpp
void ChamferPolyLine(
   PolyLine^ PolyLine
)
```

### Parameters

- `PolyLine`: [2D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html) to chamfer

## Remarks

Chamfers all vertices of a 2D PolyLine in one step by inserting chamfers at each vertex of the 2D PolyLine where two Lines meet, if applicable.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::ChamferEntities Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferEntities.html)
[ISketchManager::FilletPolyLine Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletPolyLine.html)

## Availability

DraftSight V1R6.0

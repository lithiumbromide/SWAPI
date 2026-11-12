---
title: "Pan Method (IDocument)"
project: ""
interface: "IDocument"
member: "Pan"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~Pan.html"
---

# Pan Method (IDocument)

Moves the visible portion of the drawing in the direction and distance defined through a vector.

## Syntax

### Visual Basic

```vb
Sub Pan( _
   ByVal PanX As System.Double, _
   ByVal PanY As System.Double _
)
```

### C#

```csharp
void Pan(
   System.double PanX,
   System.double PanY
)
```

### JScript

```
function Pan(
   PanX : System.double,
   PanY : System.double
);
```

### Managed Extensions for C++

```
void Pan(
   System.double PanX,
   System.double PanY
)
```

### C++/CLI

```cpp
void Pan(
   System.double PanX,
   System.double PanY
)
```

### Parameters

- `PanX`: x coordinate of the vector where to move the visible portion of the document
- `PanY`: y coordinate of the vector where to move the visible portion of the document

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IApplication::Zoom Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~Zoom.html)

## Availability

DraftSight V1R4.0

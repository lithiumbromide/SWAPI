---
title: "LineStyleGeneration Property (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "LineStyleGeneration"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~LineStyleGeneration.html"
---

# LineStyleGeneration Property (IPolyLine)

Gets whether to use a continuous or dashed LineStyle around the vertices of the 2D PolyLine with a noncontinuous LineStyle.

## Syntax

### Visual Basic

```vb
Property LineStyleGeneration As System.Boolean
```

### C#

```csharp
System.bool LineStyleGeneration {get; set;}
```

### JScript

```
function get,set LineStyleGeneration : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_LineStyleGeneration();
__property void set_LineStyleGeneration(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool LineStyleGeneration {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if a continuous or dashed LineStyle around the vertices of the 2D PolyLine with a noncontinuous LineStyle is used, false if breaks are placed between dashes in the LineStyles so that the LineStyles are positioned properly at corners

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)

## Availability

DraftSight V1R1.1

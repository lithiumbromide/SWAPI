---
title: "FitSmooth Property (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "FitSmooth"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~FitSmooth.html"
---

# FitSmooth Property (IPolyLine3D)

Gets or sets the smoothing function to apply to the 3D PolyLine.

## Syntax

### Visual Basic

```vb
Property FitSmooth As dsPolyLine3DFitSmooth_e
```

### C#

```csharp
dsPolyLine3DFitSmooth_e FitSmooth {get; set;}
```

### JScript

```
function get,set FitSmooth : dsPolyLine3DFitSmooth_e
```

### Managed Extensions for C++

```
__property dsPolyLine3DFitSmooth_e get_FitSmooth();
__property void set_FitSmooth(
   dsPolyLine3DFitSmooth_e value
);
```

### C++/CLI

```cpp
property dsPolyLine3DFitSmooth_e FitSmooth {
   dsPolyLine3DFitSmooth_e get();
   void set (    dsPolyLine3DFitSmooth_e value);
}
```

### Property Value

Smoothing function as defined in [dsPolyLine3DFitSmooth_e](Interop.dsAutomation~Interop.dsAutomation.dsPolyLine3DFitSmooth_e.html)

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)

## Availability

DraftSight V1R1.3

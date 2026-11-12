---
title: "Close Method (IGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis"
member: "Close"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~Close.html"
---

# Close Method (IGeometryAnalysis)

Performs any necessary cleanup after the geometry analysis finishes.

## Syntax

### Visual Basic (Declaration)

```vb
Function Close() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGeometryAnalysis
Dim value As System.Integer

value = instance.Close()
```

### C#

```csharp
System.int Close()
```

### C++/CLI

```cpp
System.int Close();
```

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IGeometryAnalysis::Close](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~Close.html).

## Examples

[Analyze Geometry (VBA)](Analyze_Geometry_VB6.htm)

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[IGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html)
[IGeometryAnalysis::Init Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~Init.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS

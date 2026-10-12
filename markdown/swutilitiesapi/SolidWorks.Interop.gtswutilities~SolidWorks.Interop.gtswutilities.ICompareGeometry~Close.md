---
title: "Close Method (ICompareGeometry)"
project: "SOLIDWORKS Utilities API Help"
interface: "ICompareGeometry"
member: "Close"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry~Close.html"
---

# Close Method (ICompareGeometry)

Performs any necessary cleanup after the geometry in the documents have been compared.

## Syntax

### Visual Basic (Declaration)

```vb
Function Close() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICompareGeometry
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

See [ICompareGeometry::Close](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareGeometry~Close.html).

## Examples

[Compare Geometry (VBA)](Compare_Geometry_VB6.htm)
[Set Tolerances and Compare Geometry (VBA)](Set_Tolerances_and_Compare_Geometry_VB6.htm)
[Compare Geometry (VB.NET)](Compare_Geometry_VBNET.htm)
[Compare Geometry (C#)](Compare_Geometry_CSharp.htm)
[Set Tolerances and Compare Geometry (VB.NET)](Set_Tolerances_and_Compare_Geometry_VBNET.htm)
[Set Tolerances and Compare Geometry (C#)](Set_Tolerances_and_Compare_Geometry_CSharp.htm)

## See Also

[ICompareGeometry Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry.html)
[ICompareGeometry Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareGeometry_members.html)

## Availability

SOLIDWORKS Utilities API 2004 FCS

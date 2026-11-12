---
title: "IsLine Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IsLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html"
---

# IsLine Method (ICurve)

Gets whether the curve is a line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsLine() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Boolean

value = instance.IsLine()
```

### C#

```csharp
System.bool IsLine()
```

### C++/CLI

```cpp
System.bool IsLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this curve is a line, false if other curve type

## VBA Syntax

See [Curve::IsLine](ms-its:sldworksapivb6.chm::/sldworks~Curve~IsLine.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ILineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.html)
[ICurve::LineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)

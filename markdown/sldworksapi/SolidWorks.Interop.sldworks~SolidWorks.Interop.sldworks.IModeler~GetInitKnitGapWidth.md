---
title: "GetInitKnitGapWidth Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "GetInitKnitGapWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetInitKnitGapWidth.html"
---

# GetInitKnitGapWidth Method (IModeler)

Gets the initial gap bound width for knitting a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInitKnitGapWidth() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim value As System.Double

value = instance.GetInitKnitGapWidth()
```

### C#

```csharp
System.double GetInitKnitGapWidth()
```

### C++/CLI

```cpp
System.double GetInitKnitGapWidth();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Initial knitting gap width used for body sewing

## VBA Syntax

See [Modeler::GetInitKnitGapWidth](ms-its:sldworksapivb6.chm::/sldworks~Modeler~GetInitKnitGapWidth.html).

## Remarks

This value is 0 until a call to knit a body is made.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::SetInitKnitGapWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetInitKnitGapWidth.html)

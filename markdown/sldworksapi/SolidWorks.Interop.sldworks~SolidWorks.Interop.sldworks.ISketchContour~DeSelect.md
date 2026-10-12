---
title: "DeSelect Method (ISketchContour)"
project: "SOLIDWORKS API Help"
interface: "ISketchContour"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~DeSelect.html"
---

# DeSelect Method (ISketchContour)

Deselects the sketch contour.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchContour
Dim value As System.Boolean

value = instance.DeSelect()
```

### C#

```csharp
System.bool DeSelect()
```

### C++/CLI

```cpp
System.bool DeSelect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sketch contour is deselected, false if not

## VBA Syntax

See [SketchContour::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~SketchContour~DeSelect.html).

## See Also

[ISketchContour Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.html)
[ISketchContour Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html)
[ISketchContour::Select2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour~Select2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

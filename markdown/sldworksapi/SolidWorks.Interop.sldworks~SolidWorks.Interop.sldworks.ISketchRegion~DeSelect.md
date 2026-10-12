---
title: "DeSelect Method (ISketchRegion)"
project: "SOLIDWORKS API Help"
interface: "ISketchRegion"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~DeSelect.html"
---

# DeSelect Method (ISketchRegion)

Deselects the sketch region.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchRegion
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

True if the sketch region is deselected, false if not

## VBA Syntax

See [SketchRegion::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~SketchRegion~DeSelect.html).

## See Also

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.html)
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html)
[ISketchRegion::Select2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~Select2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

---
title: "IGetDesignTableExtent Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDesignTableExtent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDesignTableExtent.html"
---

# IGetDesignTableExtent Method (IView)

Gets the size and location of the design table associated with this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDesignTableExtent() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

value = instance.IGetDesignTableExtent()
```

### C#

```csharp
System.double IGetDesignTableExtent()
```

### C++/CLI

```cpp
System.double IGetDesignTableExtent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 6 doubles; the lower left (x,y,z) and upper right (x,y,z) values indicating the design table extents; values are in meters and refer to drawing view space

## VBA Syntax

See [View::IGetDesignTableExtent](ms-its:sldworksapivb6.chm::/sldworks~View~IGetDesignTableExtent.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::HasDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HasDesignTable.html)
[IView::GetDesignTableExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDesignTableExtent.html)

## Availability

SOLIDWORKS 99, datecode 1999207

---
title: "GetDesignTableExtent Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDesignTableExtent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDesignTableExtent.html"
---

# GetDesignTableExtent Method (IView)

Gets the size and location of the design table associated with this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDesignTableExtent() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDesignTableExtent()
```

### C#

```csharp
System.object GetDesignTableExtent()
```

### C++/CLI

```cpp
System.Object^ GetDesignTableExtent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 6 doubles; the lower left (x,y,z) and upper right (x,y,z) values indicating the design table extents; values are in meters and refer to drawing view space

## VBA Syntax

See [View::GetDesignTableExtent](ms-its:sldworksapivb6.chm::/sldworks~View~GetDesignTableExtent.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::HasDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HasDesignTable.html)
[IView::IGetDesignTableExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDesignTableExtent.html)

## Availability

SOLIDWORKS 99, datecode 1999207

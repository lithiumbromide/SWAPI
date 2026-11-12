---
title: "GetCenterLineSketch Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCenterLineSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLineSketch.html"
---

# GetCenterLineSketch Method (IView)

Gets the sketch that contains all of the centerline information for this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterLineSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As Sketch

value = instance.GetCenterLineSketch()
```

### C#

```csharp
Sketch GetCenterLineSketch()
```

### C++/CLI

```cpp
Sketch^ GetCenterLineSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [View::GetCenterLineSketch](ms-its:sldworksapivb6.chm::/sldworks~View~GetCenterLineSketch.html).

## Remarks

All of the centerlines for a drawing view are stored on a sketch. This method returns that sketch. You can get information about the sketch entities, including the centerlines, in the sketch.

This method allows you to access properties of individual centerlines. DXF translation may use this method to get the centerline information in a SOLIDWORKS drawing.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterLine.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0

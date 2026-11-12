---
title: "ShowSplineHandles Property (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "ShowSplineHandles"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ShowSplineHandles.html"
---

# ShowSplineHandles Property (ISketchSpline)

Gets or sets whether to show the [handles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle.html) for this spline.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowSplineHandles As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim value As System.Boolean

instance.ShowSplineHandles = value

value = instance.ShowSplineHandles
```

### C#

```csharp
System.bool ShowSplineHandles {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowSplineHandles {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show spline handles, false to not

## VBA Syntax

See [SketchSpline::ShowSplineHandles](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~ShowSplineHandles.html).

## Examples

[Get and Set Spline Properties (VBA)](Get_and_Set_Spline_Properties_Example_VB.htm)

## Remarks

If setting this property to True, then use [IModelDoc2::WindowRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~WindowRedraw.html) after to see the spline handles.

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetSplineHandleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandleCount.html)
[ISketchSpline::GetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetSplineHandles.html)
[ISketchSpline::IGetSplineHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IGetSplineHandles.html)
[ISketchSpline::ResetAllHandles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~ResetAllHandles.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

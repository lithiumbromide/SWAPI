---
title: "ISplineHandle Interface"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html"
---

# ISplineHandle Interface

Provides access to spline handles.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISplineHandle
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
```

### C#

```csharp
public interface ISplineHandle
```

### C++/CLI

```cpp
public interface class ISplineHandle
```

## VBA Syntax

See [SplineHandle](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle.html).

## Examples

[Get and Set Spline Handles (VBA)](Get_and_Set_Spline_Handles_Example_VB.htm)
[Get and Set Spline Handles (VB.NET)](Get_and_Set_Spline_Handles_Example_VBNET.htm)
[Get and Set Spline Handles (C#)](Get_and_Set_Spline_Handles_Example_CSharp.htm)

## Remarks

To enable spline tangency and curvature handles, set [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) swDisplayAllSplineHandles to True.

NOTE: [ISelectionMgr::GetSelectedObjectType3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html) returns swSelMANIPULATORS for a spline handle.

## Accessors

[ISketchSpline::AddCurvatureControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~AddCurvatureControl.html)

[ISketchSpline::AddTangencyControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~AddTangencyControl.html)

[ISketchSpline::GetSplineHandles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~GetSplineHandles.html) and [ISketchSpline::IGetSplineHandles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~IGetSplineHandles.html)

## Access Diagram

[SplineHandle](SWObjectModel.pdf#SplineHandle)

## See Also

[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)

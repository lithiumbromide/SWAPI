---
title: "CurvatureControlled Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "CurvatureControlled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~CurvatureControlled.html"
---

# CurvatureControlled Property (ISplineHandle)

Gets or sets whether the spline handle has curvature control.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurvatureControlled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Boolean

instance.CurvatureControlled = value

value = instance.CurvatureControlled
```

### C#

```csharp
System.bool CurvatureControlled {get; set;}
```

### C++/CLI

```cpp
property System.bool CurvatureControlled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the spline handle has curvature control, false if not

## VBA Syntax

See [SplineHandle::CurvatureControlled](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~CurvatureControlled.html).

## Remarks

If the spline handle has curvature control, you can use:

- [ISplineHandle::Curvature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle~Curvature.html)
- [ISplineHandle::RadiusOfCurvature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineHandle~RadiusOfCurvature.html)

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

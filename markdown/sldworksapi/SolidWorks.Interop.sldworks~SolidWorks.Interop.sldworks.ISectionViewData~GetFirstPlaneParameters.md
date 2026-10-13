---
title: "GetFirstPlaneParameters Method (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "GetFirstPlaneParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetFirstPlaneParameters.html"
---

# GetFirstPlaneParameters Method (ISectionViewData)

Gets the first transformed plane's parameters for this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFirstPlaneParameters( _
   ByRef PlaneCenter As MathPoint, _
   ByRef PlaneVector As MathVector _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim PlaneCenter As MathPoint
Dim PlaneVector As MathVector

instance.GetFirstPlaneParameters(PlaneCenter, PlaneVector)
```

### C#

```csharp
void GetFirstPlaneParameters(
   out MathPoint PlaneCenter,
   out MathVector PlaneVector
)
```

### C++/CLI

```cpp
void GetFirstPlaneParameters(
   [Out] MathPoint^ PlaneCenter,
   [Out] MathVector^ PlaneVector
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PlaneCenter`: [Plane center point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)
- `PlaneVector`: [Plane normal vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [SectionViewData::GetFirstPlaneParameters](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~GetFirstPlaneParameters.html).

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[ISectionViewData::GetSecondPlaneParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetSecondPlaneParameters.html)
[ISectionViewData::GetThirdPlaneParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetThirdPlaneParameters.html)
[ISectionViewData::FirstPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstPlane.html)
[ISectionViewData::SecondPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondPlane.html)
[ISectionViewData::ThirdPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdPlane.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0

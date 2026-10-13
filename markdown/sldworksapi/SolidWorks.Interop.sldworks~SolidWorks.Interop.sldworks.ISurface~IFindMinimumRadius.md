---
title: "IFindMinimumRadius Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IFindMinimumRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius.html"
---

# IFindMinimumRadius Method (ISurface)

Gets the minimum radius of curvature for the selected surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFindMinimumRadius( _
   ByRef UBound As System.Double, _
   ByRef VBound As System.Double, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef UVParameter As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UBound As System.Double
Dim VBound As System.Double
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim UVParameter As System.Object
Dim value As System.Boolean

value = instance.IFindMinimumRadius(UBound, VBound, NumOfRadius, Radius, Location, UVParameter)
```

### C#

```csharp
System.bool IFindMinimumRadius(
   ref System.double UBound,
   ref System.double VBound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object UVParameter
)
```

### C++/CLI

```cpp
System.bool IFindMinimumRadius(
   System.double% UBound,
   System.double% VBound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ UVParameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UBound`: MinMax UParameter
- `VBound`: MinMax VParameter
- `NumOfRadius`: Number of radius; can be 0, 1, or 2
- `Radius`: Minimum radius of curvature (see **Remarks**)
- `Location`: [Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) where the minimum radius curvature occurred (see **Remarks**)
- `UVParameter`: [UV parameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html); because points are UV, third ordinates are 0 (see **Remarks**)

### Return Value

True if operation succeeds, false if it fails

## VBA Syntax

See [Surface::IFindMinimumRadius](ms-its:sldworksapivb6.chm::/sldworks~Surface~IFindMinimumRadius.html).

## Examples

**In-process, unmanaged C++:**

/////////////////////////////////////////////////////////////////////////////

// IMinRadius implementation

STDMETHODIMP CMinRadius::StartNotepad()

{

// TODO: Add your implementation code here

CComPtr<IModelDoc> iModelDoc2;

m_iSldWorks->get_**IActiveDoc**(&iModelDoc2);

CComPtr<ISelectionMgr> swSelMgr;

iModelDoc2->get_**ISelectionManager**(&swSelMgr);

struct IDispatch* pDispSelection;

CComPtr<IFace2> swFace;

swSelMgr->**GetSelectedObject6**(1,-1,&pDispSelection);

pDispSelection->QueryInterface(__uuidof(IFace2),reinterpret_cast<void**>(&swFace));

pDispSelection->Release();

double boundArr[4];

swFace->**IGetUVBounds** ( boundArr );

double UBound[2] = {boundArr[0],boundArr[1]};

double VBound[2] = {boundArr[2],boundArr[3]};

CComPtr<ISurface> swSurface;

swFace->**IGetSurface**(&swSurface);

long numOfRadius(0);

VARIANT radius,Location,UVParameter;

VARIANT_BOOL status(FALSE);

swSurface->**IFindMinimumRadius**(UBound,VBound,&numOfRadius,&radius,&Location,&UVParameter,&status);

SafeDoubleArray radiusSA(radius);

double test1 = radiusSA[0];

double test2 = radiusSA[1];

SafeDISPATCHArray locationSA(Location);

CComPtr<IMathPoint> swMathPoint1;

CComPtr<IMathPoint> swMathPoint2;

locationSA[0]->QueryInterface(__uuidof(IMathPoint),reinterpret_cast<void**>(&swMathPoint1));

locationSA[1]->QueryInterface(__uuidof(IMathPoint),reinterpret_cast<void**>(&swMathPoint2));

double locationArra1[3];

double locationArra2[3];

swMathPoint1->get_**IArrayData**(locationArra1);

swMathPoint2->get_**IArrayData**(locationArra2);

SafeDISPATCHArray UVParameterSA(UVParameter);

return S_OK;

}

## Remarks

The search is confined to the portion of the selected curve lying inside of UBound and VBound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)
- UVParameter: VARIANT of SafeDispatchArray of [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius.html)
[IFace2::IGetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.html)
[IFace2::GetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.html)
[ICurve::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.html)
[ICurve::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.html)
[ISurface::IParameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.html)
[ISurface::Parameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

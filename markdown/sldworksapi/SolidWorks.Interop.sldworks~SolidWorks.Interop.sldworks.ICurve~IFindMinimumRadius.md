---
title: "IFindMinimumRadius Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IFindMinimumRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.html"
---

# IFindMinimumRadius Method (ICurve)

Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFindMinimumRadius( _
   ByRef Bound As System.Double, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef Parameter As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Bound As System.Double
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim Parameter As System.Object
Dim value As System.Boolean

value = instance.IFindMinimumRadius(Bound, NumOfRadius, Radius, Location, Parameter)
```

### C#

```csharp
System.bool IFindMinimumRadius(
   ref System.double Bound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object Parameter
)
```

### C++/CLI

```cpp
System.bool IFindMinimumRadius(
   System.double% Bound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ Parameter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bound`: Array containing the start and end boundary parameters (see **Remarks**)
- `NumOfRadius`: Number of radius returned; can be 0 or 1
- `Radius`: Minimum radius of curvature (see **Remarks**)
- `Location`: [Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) where minimum radius curvature occurred (see **Remarks**)
- `Parameter`: Curve parameter (see **Remarks**)

### Return Value

True if operation succeeds, false if it fails

## VBA Syntax

See [Curve::IFindMinimumRadius](ms-its:sldworksapivb6.chm::/sldworks~Curve~IFindMinimumRadius.html).

## Examples

**Unmanaged C++ COM:**

/////////////////////////////////////////////////////////////////////////////

// IMinRadius implementation

STDMETHODIMP CMinRadius::StartNotepad()

{

// TODO: Add your implementation code here

CComPtr<IModelDoc> iModelDoc2;

m_iSldWorks->get_**IActiveDoc**(&iModelDoc2);

CComPtr<ISelectionMgr> swSelMgr;

iModelDoc2->get_**ISelectionManager**(&swSelMgr);

struct

IDispatch* pDispSelection;

CComPtr<IEdge> swEdge;

swSelMgr->**GetSelectedObject6**(1,-1,&pDispSelection);

pDispSelection->QueryInterface(

__uuidof(IEdge),reinterpret_cast<void

**>(&swEdge));

pDispSelection->Release();

double

boundArr[2];

CComPtr<ICurve> swCurve;

swEdge->**IGetCurve**(&swCurve);

VARIANT_BOOL isClose,isPeriodic,testRetVal;

swCurve->**GetEndParams**(&boundArr[0],&boundArr[1],&isClose,&isPeriodic,&testRetVal);

long

numOfRadius(0);

VARIANT radius,Location,UVParameter;

VARIANT_BOOL status(FALSE);

swCurve->**IFindMinimumRadius**(boundArr,&numOfRadius,&radius,&Location,&UVParameter,&status);

SafeDoubleArray radiusSA(radius);

double

test1 = radiusSA[0];

SafeDISPATCHArray locationSA(Location);

CComPtr<IMathPoint> swMathPoint1;

locationSA[0]->QueryInterface(

__uuidof(IMathPoint),reinterpret_cast<void**>(&swMathPoint1));

double locationArra1[3];

swMathPoint1->get_**IArrayData**(locationArra1);

SafeDoubleArray UVParameterSA(UVParameter);

double uvpara1 = UVParameterSA[0];

return S_OK;

}

## Remarks

The search is confined to the portion of the selected curve lying inside of Bound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)
- Parameter: VARIANT of SafeDoubleArray

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.html)
[ISurface::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius.html)
[ISurface::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius.html)
[ICurve::GetEndParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0

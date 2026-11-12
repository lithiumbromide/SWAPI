---
title: "Get Curve Spline Points Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm"
---

# Get Curve Spline Points Example (C++ COM)

This example shows how to get the point coordinates from a selected sketch spline segment.

The methods ICurve::IGetSplinePts and ICurve::IGetBCurveParams return arrays, so this code must be used in an in-process DLL. Otherwise, use the methods ICurve::GetSplinePts and ICurve::GetBCurveParams that return VARIANTs.

```vb
void GetCurveSplinePoints(ISldWorks* m_pSldWorks)
{
 HRESULT hres;
 LPMODELDOC2 pModelDoc = NULL;
 hres = m_pSldWorks->get_IActiveDoc2(&pModelDoc);
 if( pModelDoc == NULL)
  return;

 LPUNKNOWN pUnk = NULL;
 LPSELECTIONMGR pSelectMgr = NULL;
 pModelDoc->get_ISelectionManager( &pSelectMgr);
 if( pSelectMgr)
 {
  pSelectMgr->IGetSelectedObject3( 1, &pUnk);
  pSelectMgr->Release();
 }

 LPSKETCHSEGMENT pSketchSeg = NULL;

 if( pUnk)
 {
  pUnk->QueryInterface( IID_ISketchSegment, (void **)&pSketchSeg);
  pUnk->Release();
  pUnk = NULL;
 }

 LPCURVE pCurve = NULL;
 if( pSketchSeg)
 {
  pSketchSeg->IGetCurve( &pCurve);
  pSketchSeg->Release();
 }

 if( pCurve)
 {
  long nParamSize;
  pCurve->IGetBCurveParamsSize2( FALSE, TRUE, &nParamSize);
  double *dSplineParams = new double [nParamSize];

  pCurve->IGetBCurveParams( dSplineParams);
  int *propArray = (int*)&dSplineParams[0];

  double *dKnotArray = &dSplineParams[2];
  double *dCtrlArray = &dSplineParams[ 2+ propArray[1]+propArray[2] ];

  long nSplinePts;
  pCurve->IGetSplinePtsSize( propArray, dKnotArray, dCtrlArray, &nSplinePts);
  double *dSplinePts = new double[nSplinePts];

  pCurve->IGetSplinePts( dSplinePts);

  for( int i = 0; i < nSplinePts; i += 3)
  {
   TRACE( auT("x = %f, y = %f, z = %f\n"),

   dSplinePts[i], dSplinePts[i+1], dSplinePts[+2]);

  }

  delete [] dSplineParams;
  delete [] dSplinePts;

  pCurve->Release();
 }
 pModelDoc->Release();
}
```

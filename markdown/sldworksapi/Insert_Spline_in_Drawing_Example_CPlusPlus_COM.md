---
title: "Insert Spline in Drawing Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm"
---

# Insert Spline in Drawing Example (C++ COM)

This example shows how to insert a spline in a drawing.

```vb
STDMETHODIMP CDgtlPen::demo3()
{
    HRESULT                                 hr = S_OK;
    CComPtr <IModelDoc2>                    pModel;
    CComQIPtr <IDrawingDoc>                 pDraw;
    CComPtr <IView>                         pView;
    CComPtr <IView>                         pFocusLockedView;
    CComPtr <ISheet>                        pSheet;
    int                                     pPropArray[4];
    double                                  pKnotsArray[11];
    double                                  pCntrlPntCoordArray[21];
    VARIANT_BOOL                            updateEditRebuild = TRUE;
    long                                    retval = NULL;
    VARIANT_BOOL                            focusLocked = NULL;
    ZeroMemory(pPropArray, 4 * sizeof(int));
    ZeroMemory(pKnotsArray, 11 * sizeof(double));
    ZeroMemory(pCntrlPntCoordArray, 21 * sizeof(double));
    pPropArray[0] = 3;      //Dimension
    pPropArray[1] = 4;      //Order
    pPropArray[2] = 7;      //Number of control Points
    pPropArray[3] = 0;      //Periodicity
    pKnotsArray[0] = 0;
    pKnotsArray[1] = 0;
    pKnotsArray[2] = 0;
    pKnotsArray[3] = 0;
    pKnotsArray[4] = 0.3;
    pKnotsArray[5] = 0.3;
    pKnotsArray[6] = 0.6;
    pKnotsArray[7] = 1;
    pKnotsArray[8] = 1;
    pKnotsArray[9] = 1;
    pKnotsArray[10] = 1;
    pCntrlPntCoordArray[0] = -0.1;      pCntrlPntCoordArray[1] = -0.009;    pCntrlPntCoordArray[2] = 0;
    pCntrlPntCoordArray[3] = -0.11;     pCntrlPntCoordArray[4] = 0.013;     pCntrlPntCoordArray[5] = 0;
    pCntrlPntCoordArray[6] = -0.14;     pCntrlPntCoordArray[7] = 0.035;     pCntrlPntCoordArray[8] = 0;
    pCntrlPntCoordArray[9] = 0.015;     pCntrlPntCoordArray[10] = 0.019;    pCntrlPntCoordArray[11] = 0;
    pCntrlPntCoordArray[12] = -0.059;   pCntrlPntCoordArray[13] = -0.024;   pCntrlPntCoordArray[14] = 0;
    pCntrlPntCoordArray[15] = 0.012;    pCntrlPntCoordArray[16] = -0.018;   pCntrlPntCoordArray[17] = 0;
    pCntrlPntCoordArray[18] = 0.054;    pCntrlPntCoordArray[19] = -0.013;   pCntrlPntCoordArray[20] = 0;
    hr = m_iSldWorks->get_IActiveDoc2(&pModel);
    _ASSERT(pModel);
    pDraw = pModel;
    _ASSERT(pDraw);
    hr = pDraw->IGetFirstView(&pView);
    _ASSERT(pView);
    while(pView != NULL)
    {
        CComPtr <IView>                     pNextView;
        hr = pView->get_FocusLocked(&focusLocked);

        if (focusLocked)
        {
            pFocusLockedView = pView;
            _ASSERT(pView);
            pView = NULL;
        }
        else
        {
            hr = pView->IGetNextView(&pNextView);
            pView = NULL;
            pView = pNextView;
        }
    }
    hr = pDraw->IGetCurrentSheet(&pSheet);
    _ASSERT(pSheet);
    hr = pSheet->get_FocusLocked(&focusLocked);
    hr = pSheet->put_FocusLocked (TRUE);

    hr = pModel->InsertSketch2(updateEditRebuild);
    hr = pModel->ISketchSplineByEqnParams(pPropArray, pKnotsArray, pCntrlPntCoordArray, &retval);
    _ASSERT(retval);
    hr = pSheet->put_FocusLocked(focusLocked);
    if(pFocusLockedView != NULL)
        {
        hr = pFocusLockedView->put_FocusLocked(TRUE);
        }
    hr = pModel->GraphicsRedraw2();
    return S_OK;
}
```

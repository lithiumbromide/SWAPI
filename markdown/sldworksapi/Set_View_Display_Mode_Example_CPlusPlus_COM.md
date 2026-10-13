---
title: "Set View Display Mode Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_View_Display_Mode_Example_CPlusPlus_COM.htm"
---

# Set View Display Mode Example (C++ COM)

This example shows how to set the display mode of drawing views.

```vb
STDMETHODIMP CDgtlPen::demo2()
{
    HRESULT                                 hr = S_OK;
    CComPtr <IModelDoc2>                    pModel;
    CComQIPtr <IDrawingDoc>                 pDraw;
    CComPtr <ISheet>                        pSheet;
    CComPtr <IView>                         pSheetView;
    CComPtr <IView>                         pView;
    long                                    swDisplayMode = -1;
    VARIANT_BOOL                            UseParent = FALSE;
    VARIANT_BOOL                            Facetted = TRUE;
    VARIANT_BOOL                            Edges = TRUE;
    VARIANT_BOOL                            retval = NULL;
    hr = m_iSldWorks->get_IActiveDoc2(&pModel);
    _ASSERT(pModel);
    pDraw = pModel;
    _ASSERT(pDraw);
    hr = pDraw->IGetCurrentSheet(&pSheet);
    _ASSERT(pSheet);
    hr = pDraw->IGetFirstView(&pSheetView);
    _ASSERT(pSheetView);
    hr = pSheetView->IGetNextView(&pView);
    _ASSERT(pView);
    while(pView != NULL)
    {
        CComPtr <IView>                     pNextView;
        hr = pView->GetDisplayMode2(&swDisplayMode);
        switch(swDisplayMode)
        {
            case swWIREFRAME:
            case swHIDDEN_GREYED:
            case swHIDDEN:
                break;
            case swSHADED:
            case swFACETED_WIREFRAME:
            case swFACETED_HIDDEN_GREYED:
            case swFACETED_HIDDEN:
                hr = pView->SetDisplayMode3(UseParent, swHIDDEN, Facetted, Edges, &retval);
                _ASSERT(retval);
                break;
            default :
                _ASSERT(FALSE);
                break;
        }
        hr = pView->IGetNextView(&pNextView);
        // Release view
        pView = NULL;
        pView = pNextView;
    }
    return S_OK;
}
```

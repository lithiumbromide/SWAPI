---
title: "Get Bodies Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bodies_Example_CPlusPlus_COM.htm"
---

# Get Bodies Example (C++ COM)

This example shows how to get the bodies in a part document.

```vb
// -------------------------------------------------------------------
void APITestFunction()
{
    HRESULT                                 hr = S_OK;
    VARIANT_BOOL                            bRet = VARIANT_FALSE;
    long                                    nRetVal = -1;
    CComPtr <ISldWorks>                     pSldWorks;
    CComPtr <IModelDoc2>                    pModel;
    CComQIPtr <IPartDoc>                    pPart;
    VARIANT                                 vBodyArr;
    long                                    i = -1;
    // Connect to SOLIDWORKS Design
    pSldWorks = TheApplication->GetSWApp();
    ASSERT(pSldWorks);
    hr = pSldWorks->get_IActiveDoc2(&pModel);
    ASSERT(pModel);
    hr = pModel->ClearSelection2(VARIANT_TRUE);
    pPart = pModel;
    ASSERT(pPart);
    hr = pPart->GetBodies2(swSolidBody, VARIANT_TRUE, &vBodyArr);
    ASSERT(NULL != vBodyArr.pparray);
    // Process bodies
    SAFEARRAY*              psaBody = V_ARRAY(&vBodyArr);
    LPDISPATCH*             pBodyDispArray = NULL;
    long                    nBodyHighIndex = -1;
    long                    nBodyCount = -1;
    hr = SafeArrayAccessData(psaBody, (void **) &pBodyDispArray);
    ASSERT(S_OK == hr);
    ASSERT(NULL != pBodyDispArray);
    // Get index number of highest array element
    // The array range is from 0 to highIndex
    hr = SafeArrayGetUBound(psaBody, 1, &nBodyHighIndex);
    ASSERT(S_OK == hr);
    // Actual number of array elements is nBodyHighIndex + 1
    nBodyCount = nBodyHighIndex + 1;
    // Process each body
    for (i = 0; i < nBodyCount; i++)
        {
        CComQIPtr <IBody2>          pBody;
        // Calls AddRef() on IDispatch ---> refcount = 2
        pBody = pBodyDispArray[i];
        ASSERT(pBody);
        hr = pBody->Select(VARIANT_TRUE, 0, &bRet);
        ASSERT(bRet);
        // After this call ---> refcount = 1
        // When it goes out of scope ---> refcount = 0
        pBody.Release();
        }
    // Unaccess & destroy the component SafeArray
    hr = SafeArrayUnaccessData(psaBody);
    hr = SafeArrayDestroy(psaBody);
    return;
} //void APITestFunction()
// -------------------------------------------------------------------
```

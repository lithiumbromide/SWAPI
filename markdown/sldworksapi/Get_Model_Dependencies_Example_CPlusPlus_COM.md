---
title: "Get Model Dependencies Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Dependencies_Example_CPlusPlus_COM.htm"
---

# Get Model Dependencies Example (C++ COM)

This example shows how to get the names of the dependencies for a model.

```vb
// -------------------------------------------------------------------
void APITestFunction()
{
    HRESULT                                 hr = S_OK;
    VARIANT_BOOL                            bRet = VARIANT_FALSE;
    long                                    nRetVal = -1;
    CComPtr <ISldWorks>                     pSldWorks;
    CComPtr<IModelDoc2>                     pModelDoc;
    long                                    nNumDepend = -1;
    BSTR*                                   psDepends = NULL;
    long                                    i = -1;
    // Connect to SOLIDWORKS Design application
    pSldWorks = TheApplication->GetSWApp();
    ASSERT(pSldWorks);
    hr = pSldWorks->get_IActiveDoc2(&pModelDoc);
    ASSERT(pModelDoc);
    hr = pModelDoc->IGetNumDependencies(VARIANT_TRUE, VARIANT_TRUE, &nNumDepend);
    ASSERT(nNumDepend > 0);
    psDepends = new BSTR[nNumDepend];
    ASSERT(psDepends);
    ZeroMemory(psDepends, nNumDepend * sizeof(BSTR));
    hr = pModelDoc->IGetDependencies2(VARIANT_TRUE, VARIANT_TRUE, VARIANT_FALSE, psDepends);
    ASSERT(psDepends);
    for (i = 0; i < nNumDepend / 2; i++)
        {
        CComBSTR                                sDepend1;
        CComBSTR                                sDepend2;
        CComBSTR                                sOutputStr;
        sDepend1.Attach(psDepends[2 * i + 0]);
        sDepend2.Attach(psDepends[2 * i + 1]);
        sOutputStr = sDepend1;
        sOutputStr += CComBSTR(_T(" --> "));
        sOutputStr += sDepend2;
        sOutputStr += CComBSTR(_T("\n"));
        OutputDebugString(sOutputStr);
       }
    delete [] psDepends;
    return;
} //void APITestFunction()
// -------------------------------------------------------------------
```

---
title: "Get Parent Features Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parent_Features_Example_CPlusPlus_COM.htm"
---

# Get Parent Features Example (C++ COM)

This example shows how to get the parent features of the selected feature.

```vb
// -------------------------------------------------------------------
STDMETHODIMP CAPITestATL::API_Test(void)
{
    AFX_MANAGE_STATE(AfxGetStaticModuleState());
    HRESULT                             hr = S_OK;
    CComPtr <ISldWorks>                 pSldWorks;
    CComPtr <IModelDoc2>                pModel;
    CComPtr <ISelectionMgr>             pSelMgr;
    CComPtr <IUnknown>                  pUnk;
    CComQIPtr <IFeature>                pSelFeat;
    long                                NumParents = 0;
    long                                i = 0;
    IFeature**                          pParentsOfFeature = NULL;
    try
        {
        // Connect to SOLIDWORKS Design application
        ASSERT(m_iSldWorks);
        hr = m_iSldWorks->get_IActiveDoc2(&pModel);
        ASSERT(pModel);
        hr = pModel->get_ISelectionManager(&pSelMgr);
        ASSERT(pSelMgr);
        hr = pSelMgr->IGetSelectedObject5(1, &pUnk);
        ASSERT(pUnk);
        pSelFeat = pUnk;
        ASSERT(pSelFeat);
        hr = pSelFeat->IGetParentCount(&NumParents);
        ASSERT(NumParents > 0);
        pParentsOfFeature = new IFeature * [NumParents];
        ZeroMemory(pParentsOfFeature, NumParents * sizeof(IFeature *));
        hr = pSelFeat->IGetParents(pParentsOfFeature);
        // For debugging purposes only
        for (i = 0; i < NumParents; i++)
            {
            CComBSTR            sFeatName;
            CComBSTR            sTypeName;
            hr = pParentsOfFeature[i]->get_Name(&sFeatName);
            hr = pParentsOfFeature[i]->GetTypeName(&sTypeName);
            }
        try
            {
            // Clean up each object in the list
            for (i = 0; i < NumParents; i++)
                {
                if (pParentsOfFeature[i] != NULL)
                    {
                    pParentsOfFeature[i]->Release();
                    pParentsOfFeature[i] = NULL;
                    }
                }
            }
        catch (...)
            {
            DebugBreak();
            }
        }
    catch (...)
        {
        DebugBreak();
        }
    delete [] pParentsOfFeature;
    return S_OK;
}
// -------------------------------------------------------------------
```

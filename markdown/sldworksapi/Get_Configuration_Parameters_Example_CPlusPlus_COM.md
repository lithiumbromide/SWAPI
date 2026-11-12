---
title: "Get Configuration Parameters Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configuration_Parameters_Example_CPlusPlus_COM.htm"
---

# Get Configuration Parameters Example (C++ COM)

This example shows how to get the parameters for the specified configuration.

```vb
'--------------------------------
'
' Preconditions: Part is open and has a configuration named aaa.
'
' Postconditions: None
'
'---------------------------------
#define USING_DEBUG_SOLIDWORKS          TRUE
#ifdef _DEBUG && USING_DEBUG_SOLIDWORKS
    #define AFX_MANAGE_STATE_ADDIN      AFX_MANAGE_STATE(AfxGetAppModuleState());
#else
    #define AFX_MANAGE_STATE_ADDIN      AFX_MANAGE_STATE(AfxGetStaticModuleState());
#endif
// -------------------------------------------------------------------
STDMETHODIMP CAPITestATL::API_Test(void)
{
    AFX_MANAGE_STATE_ADDIN;
    HRESULT                             hr = S_OK;
    CComPtr <ISldWorks>                 pSldWorks;
    CComPtr <IModelDoc2>                pModel;
    CComPtr <IConfigurationManager>     pCfgMgr;
    CComBSTR                            sCfgName(_T("aaa"));
    long                                NumParams = 0;
    long                                i = 0;
BSTR                                *vNames = NULL;
BSTR                                *vValues = NULL;
VARIANT_BOOL                        bret = VARIANT_FALSE;
    try
        {
        // Connect to SOLIDWORKS Design
        ASSERT(m_iSldWorks);
        hr = m_iSldWorks->get_IActiveDoc2(&pModel);
        ASSERT(pModel);
        hr = pModel->get_ConfigurationManager(&pCfgMgr);
        ASSERT(pCfgMgr);
        hr = pCfgMgr->GetConfigurationParamsCount(sCfgName, &NumParams);
        ASSERT(NumParams > 0);
        vNames  = new BSTR[NumParams];  ASSERT(vNames );
        vValues = new BSTR[NumParams];  ASSERT(vValues);
        hr = pCfgMgr->IGetConfigurationParams(sCfgName, NumParams, vNames, vValues, &bret);
        ASSERT(bret);
        for (i = 0; i < NumParams; i++)
            {
            CComBSTR                sName ;
            CComBSTR                sValue;

            sName .Attach(vNames [i]);
            sValue.Attach(vValues[i]);
            OutputDebugString(sName );
            OutputDebugString(_T("\n"));
            OutputDebugString(sValue);
            OutputDebugString(_T("\n"));
            }
        delete [] vNames ;
        delete [] vValues ;
        }
    catch (...)
        {
        DebugBreak();
        }
    delete [] vNames ;
    delete [] vValues ;
return S_OK;
}
```

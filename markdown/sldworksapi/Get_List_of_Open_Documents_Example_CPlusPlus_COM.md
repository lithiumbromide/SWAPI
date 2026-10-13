---
title: "Get List of Open Documents Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm"
---

# Get List of Open Documents Example (C++ COM)

This example shows how to get a list of the currently open SOLIDWORKS Design documents.

```vb
// -------------------------------------------------------------------
void APITestFunction()
{
    HRESULT                                 hr = S_OK;
    VARIANT_BOOL                            bRet = VARIANT_FALSE;
    long                                    nRetVal = -1;
    CComPtr <ISldWorks>                     pSldWorks;
    CComPtr<IEnumDocuments2>                pEnumDoc;
    long                                    nFetched = -1;
    CComPtr<IModelDoc2>                     pModelDoc;
    long                                    i = -1;
    // Connect to SOLIDWORKS Design application
    pSldWorks = TheApplication->GetSWApp();
    ASSERT(pSldWorks);
    hr = pSldWorks->EnumDocuments2(&pEnumDoc);
    ASSERT(pEnumDoc);
    hr = pEnumDoc->Reset();
    do
        {
        CComBSTR                                sPathName;
        // Reset before reuse
        pModelDoc = NULL;
        // Could also check HRESULT or nFetched
        hr = pEnumDoc->Next(1, &pModelDoc, &nFetched);
        if (pModelDoc)
            {
            // Debugging only
            hr = pModelDoc->GetPathName(&sPathName);
            }
        } while (pModelDoc);
    return;
} //void APITestFunction()
// -------------------------------------------------------------------
```

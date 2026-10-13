---
title: "Copy Document Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Document_Example_CPlusPlus_COM.htm"
---

# Copy Document Example (C++ COM)

This example shows how to copy documents.

```vb
// -------------------------------------------------------------------
void APITestFunction()
{
    HRESULT                                 hr = S_OK;
    VARIANT_BOOL                            bRet = VARIANT_FALSE;
    long                                    nRetVal = -1;
    CComPtr <ISldWorks>                     pSldWorks;
    BSTR                                    s1, s2, s3[1], s4[1];
    long                                    error = -1;
    s1 = SysAllocString(_T("c:\\temp\\1\\assem1.sldasm"));
    s2 = SysAllocString(_T("c:\\temp\\2\\2\\assem2.sldasm"));
    s3[0] = SysAllocString(_T("c:\\temp\\1\\part1.sldprt"));
    s4[0] = SysAllocString(_T("c:\\temp\\2\\2\\part2.sldprt"));
    // connect to SW
    pSldWorks = TheApplication->GetSWApp();
    ASSERT(pSldWorks);
    hr = pSldWorks->ICopyDocument(
            s1, s2,
            1,
            s3, s4,
            swMoveCopyOptionsOverwriteExistingDocs + swMoveCopyOptionsCreateNewFolder,
            &error);
    return;
} //void APITestFunction()
// -------------------------------------------------------------------
```

---
title: "Add Components and Transforms Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Components_and_Transforms_Example_CPlusPlus_COM.htm"
---

# Add Components and Transforms Example (C++ COM)

This example shows how to use transforms when adding components.

```vb
// -------------------------------------------------------------------
void APITestFunction()
{
    HRESULT                                 hr = S_OK;
    long                                    nRetVal = -1;
    CComPtr <ISldWorks>                     pSldWorks;
    CComPtr <IModelDoc2>                    pModel;
    CComQIPtr <IAssemblyDoc>                pAssy;
    long                                    nNumComp = 2;
    BSTR                                    sPartPath[2] =
                                                {
                                                _T("c:/samples/Part1.SLDPRT"),
                                                _T("c:/samples/Part2.SLDPRT")
                                                };
    LPCOMPONENT                             swCompArr[2] = { NULL, NULL};
    double                                  dTransform[32] =
                                                {
                                                1,
                                                0,
                                                0,
                                                0,
                                                1,
                                                0,
                                                0,
                                                0,
                                                1,
                                                0.135786163522013,
                                                -3.73411949685534E-02,
                                                -2.04999999999997E-02,
                                                1,
                                                0,
                                                0,
                                                0,

                                                1,
                                                0,
                                                0,
                                                0,
                                                1,
                                                0,
                                                0,
                                                0,
                                                1,
                                                -0.205037106918239,
                                                -8.82610062893077E-03,
                                                -5.62499999999999E-02,
                                                1,
                                                0,
                                                0,
                                                0
                                                };
    // Connect to SOLIDWORKS Design
    pSldWorks = TheApplication->GetSWApp();
    ASSERT(pSldWorks);
    hr = pSldWorks->get_IActiveDoc2(&pModel);
    ASSERT(pModel);
    pAssy = pModel;
    ASSERT(pAssy);
    hr = pAssy->IAddComponents2(&nNumComp, sPartPath, dTransform, swCompArr);
    ASSERT(swCompArr[0]);
    ASSERT(swCompArr[1]);
    hr = swCompArr[0]->Release();
    hr = swCompArr[1]->Release();
}
// -------------------------------------------------------------------
```

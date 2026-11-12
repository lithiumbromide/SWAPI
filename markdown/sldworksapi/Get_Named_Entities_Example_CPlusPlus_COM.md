---
title: "Get Named Entities Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Named_Entities_Example_CPlusPlus_COM.htm"
---

# Get Named Entities Example (C++ COM)

This example shows how to get the named entities.

```vb
// -------------------------------------------------------------------
// Preconditions:
//          1) An part is open.
//          2) At least one named entity exists in the part.
//
 void APITestFunction()
 {
     HRESULT                         hr = S_OK;
     VARIANT_BOOL                    bRet = VARIANT_FALSE;
     CComPtr <ISldWorks>             pSldWorks;
     CComPtr <IModelDoc>             pModel;
     CComQIPtr <IPartDoc>            pPart;
     long                            nEntCount = -1;
     CComPtr <IEntity>               pEntity;
     LPENTITY*                       ppEntity = NULL;
     long                            i = -1;

     // Connect to SOLIDWORKS
     pSldWorks = TheApplication->GetSWApp();
     ASSERT(pSldWorks);

     hr = pSldWorks->get_IActiveDoc(&pModel);
     ASSERT(pModel);

     pPart = pModel;
     ASSERT(pPart);

     hr = pPart->GetNamedEntitiesCount (&nEntCount);
     ASSERT(nEntCount > 0);

     ppEntity = new LPENTITY[nEntCount];
     ASSERT(ppEntity);

     ZeroMemory(ppEntity, nEntCount * sizeof(LPENTITY));

     hr = pPart->IGetNamedEntities(nEntCount, ppEntity);
     ASSERT(S_OK == hr);

     for (i = 0; i < nEntCount; i++)
         {
         CComPtr <IEntity>               pEntity;
         CComBSTR                        sEntName;

         pEntity.Attach(ppEntity[i]);

         hr = pPart->IGetEntityName(pEntity, &sEntName);

         OutputDebugString(sEntName);
         OutputDebugString(_T("\n"));
         }

     delete [] ppEntity;
 } //void APITestFunction()
 // -------------------------------------------------------------------
```

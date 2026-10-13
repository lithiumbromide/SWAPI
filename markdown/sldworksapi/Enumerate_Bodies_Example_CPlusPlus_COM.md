---
title: "Enumerate Bodies Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Enumerate_Bodies_Example_CPlusPlus_COM.htm"
---

# Enumerate Bodies Example (C++ COM)

This example shows how to use IEnumBodies to traverse the list of body objects. The IBody objects returned in IEnumBodies are the bodies associated with reference surfaces. This list does not include the part body itself. IEnumBodies::Next allows your application to get each individual body and then call appropriate methods for that body.

SOLIDWORKS API represents each reference surface with two IBody objects, one for the front face and one for the back face. The faces for each body pair should have Normal vectors that are opposite.

**NOTE:** Replace `public_documents` with the path where the header files for the general helper functions are installed on your computer. This path is typically **C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 20**`nn,` where `nn` is the 2-digit release year of the version of SOLIDWORKS Design that you are running.

```vb
// Precompiled header
#include "stdafx.h"

#include <public_documents/appcomm/amapp.h>
#include "userapp.h"

void WalkGTBody()
{
 LPMODELDOC m_ModelDoc = NULL;
 HRESULT hres = NOERROR;

 hres = UserApp->getSWApp()->get_IActiveDoc( &m_ModelDoc );  // Retrieve IModelDoc pointer
 if( m_ModelDoc == NULL )
  return;

 LPPARTDOC m_PartDoc = NULL;
 hres = m_ModelDoc->QueryInterface( IID_IPartDoc, (LPVOID *)&m_PartDoc);

 walkBody(m_PartDoc);

 m_ModelDoc ->Release();
 m_PartDoc->Release();
}

void walkBody(LPPARTDOC pPartDoc)
{
 LPENUMBODIES pBodyEnum = NULL;
 HRESULT resultVal = pPartDoc->EnumRelatedBodies(&pBodyEnum);
 LPBODY pOldBody;
 resultVal = pBodyEnum->Next(1, &pOldBody, NULL); // Two bodies for each RefSurface
 while (S_OK == resultVal)
 {
  LPENUMFACES pFaceEnum = NULL;
  resultVal = pOldBody->EnumFaces(&pFaceEnum);
  int faceNum = 0;
  LPFACE pFace;
  resultVal = pFaceEnum->Next(1, &pFace, NULL);
  while (S_OK == resultVal)
  {
   VARIANT normal;
   faceNum++;

   LPBODY pCheckBody;
   resultVal = pFace->IGetBody(&pCheckBody);
   if (pCheckBody != NULL) pCheckBody->Release();

   pFace->Release();
   pFace = NULL;
   resultVal = pFaceEnum->Next(1, &pFace, NULL);
  }

  if (pFaceEnum != NULL) pFaceEnum->Release();

  pOldBody ->Release();
  pOldBody = NULL;
  resultVal = pBodyEnum->Next(1, &pOldBody, NULL);
 }

 if (pBodyEnum != NULL) pBodyEnum->Release();
}
```

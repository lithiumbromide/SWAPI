---
title: "Display of Item in FeatureManager Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm"
---

# Display of Item in FeatureManager Example (C++ COM)

## Display of Item in FeatureManager Design Tree Example (C++ COM)

This example shows how to change the visibility of features in the FeatureManager design tree. Import swconst.tlb.

```vb
ToggleFeatureManagerItemDisplay()
{
 VARIANT_BOOL flag;
 HRESULT hres;
 LPMODELDOC2 pModelDoc = NULL;
 hres = m_pSldWorks->get_IActiveDoc2(&pModelDoc);
  if (S_OK == hres && pModelDoc != NULL)
 {
  // Get the Selection Manager
  LPSELECTIONMGR SelectionMgr = NULL;
  hres = pModelDoc->get_ISelectionManager(&SelectionMgr);
  if (S_OK != hres || SelectionMgr == NULL )
   return;
  long numSelObjects;
  hres = SelectionMgr->GetSelectedObjectCount ( &numSelObjects );
   if (S_OK != hres || S_OK== hres && numSelObjects == 0 )
   return;

  LPUNKNOWN pSelObject;
  long index;
  long SelType;
   for (index=1; index <= numSelObjects; index++)
  {

   if(S_OK == SelectionMgr->GetSelectedObjectType2(index,&SelType))
   {
    if( SelType == swSelBODYFEATURES ||
     SelType == swSelDATUMAXES  ||
     SelType == swSelDATUMPLANES  ||
     SelType == swSelDATUMPOINTS  ||
     SelType == swSelMATES  ||
     SelType == swSelREFCURVES  ||
     SelType == swSelREFERENCECURVES ||
     SelType == swSelREFSURFACES  ||
     SelType == swSelSKETCHES )
    {

     if(S_OK == SelectionMgr->IGetSelectedObject3( index,
        &pSelObject ) && pSelObject != NULL)
     {
      LPFEATURE pFeature;
      if(S_OK == pSelObject->QueryInterface(IID_IFeature,
           (void**)&pFeature))
      {
       // Determine if the feature is hidden in the
       // FeatureManager design tree
       if(S_OK == pFeature->GetUIState(
         swIsHiddenInFeatureMgr, &flag))
       {
        // If feature is hidden in the
        // FeatureManager design tree, display it,
        // otherwise, hide it.
        if (flag)
        {
pFeature->SetUIState(
          swIsHiddenInFeatureMgr,
          FALSE);
        }else{
         pFeature->SetUIState(
          swIsHiddenInFeatureMgr, TRUE);
        }
       }
      }
     }
    }
   }
  }

  // Update the Feature Manager Window by performing a Rebuild on the Doc Type
  long doctype;
  hres = pModelDoc->GetType(&doctype);

  if (doctype == swDocPART )
  {
   LPPARTDOC pPartDoc = NULL;

   // Retrieve IPartDoc pointer
   hres = pModelDoc->QueryInterface(IID_IPartDoc, (LPVOID *)&pPartDoc);

   ASSERT( hres == S_OK );

   hres = pPartDoc->EditRebuild();

   // clean up
   pPartDoc->Release(); // Release the IPartDoc pointer
  }
  else if (doctype == swDocASSEMBLY)
  {
   LPASSEMBLYDOC pAssemblyDoc = NULL;

   // Retrieve IAssemblyDoc pointer
   hres = pModelDoc->QueryInterface(IID_IAssemblyDoc,
         (LPVOID *)&pAssemblyDoc);

   ASSERT( hres == S_OK );

   hres = pAssemblyDoc->EditRebuild();

   // clean up
  pAssemblyDoc->Release(); // Release the IAssemblyDoc pointer
  }
  else if (doctype == swDocDRAWING)
  {
   LPDRAWINGDOC pDrawingDoc = NULL;

   // Retrieve IDrawingDoc pointer
   hres = pModelDoc->QueryInterface(IID_IDrawingDoc,
         (LPVOID *)&pDrawingDoc);

   ASSERT( hres == S_OK );

   hres = pDrawingDoc->EditRebuild();

   // clean up
   pDrawingDoc->Release(); // Release the IDrawingDoc pointer
  }

  pModelDoc->Release(); // Release the IModelDoc pointer
 }
}
```

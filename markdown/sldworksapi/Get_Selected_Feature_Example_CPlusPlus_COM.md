---
title: "Get Selected Feature Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selected_Feature_Example_CPlusPlus_COM.htm"
---

# Get Selected Feature Example (C++ COM)

## Get Selected Feature Example

This example shows how to get the selected feature and its type, and return the object to the calling method.

```vb
LPFEATURE CGetSelectedFeatureApp::GetSelectedFeature1( LPMODELDOC2 pModelDoc, CString* Message )
{
 long lres = 0;
 LPSELECTIONMGR pSelectMgr = NULL;
 HRESULT hres =NULL;
 LPUNKNOWN pUnk = NULL;
 LPFEATURE pSelectedFeature = NULL;
 BSTR bFeatureTypeName;
 BSTR bFeatureName;

 // Get the Selection Manager for this doc
 if(S_OK != pModelDoc->get_ISelectionManager( &pSelectMgr ) ||
pSelectMgr == NULL)
 {
  *Message = "Unable to get the Selection Manager.\r\n";
 }
 else if(S_OK != pSelectMgr->GetSelectedObjectType( 1, &lres )
|| lres == 0)
 {
 // Get the Selected Object type
  *Message = "No Feature is currently selected.\r\n";
 }
 else if(S_OK != pSelectMgr->IGetSelectedObject2( 1, &pUnk )
|| pUnk == NULL)
 {
 // Get the Selected Object of Unknown Type
  *Message = "Unable to get the selected Object.\r\n";
 }
 else if(S_OK != pUnk->QueryInterface( IID_IFeature,
(LPVOID *)&pSelectedFeature) || pSelectedFeature == NULL)
 {
 // Get the Selected Feature
  *Message = "Unable to get the selected Feature.\r\n";
 }
 else if(S_OK != pSelectedFeature->GetTypeName(&bFeatureTypeName)||
bFeatureTypeName == NULL)
 {
 // Get the Selected Feature Type Name

  *Message = "Unable to get the selected Feature Type Name.\r\n";
 }
 else if(S_OK != pSelectedFeature->get_Name(&bFeatureName)||
bFeatureName == NULL)
 {
 // Get the Selected Feature Name
  *Message = "Unable to get the selected Feature Name.\r\n";
 }
 else
 {
  // Everything is okay. Clean up and report back with object.

  // Release the Selection Manager
  pSelectMgr->Release();
  // Release the unknown object
  pUnk->Release();

  // Form the return message
  CString FeatureTypeName(bFeatureTypeName);
  CString FeatureName(bFeatureName);
  *Message = "Found a Feature called " + FeatureName + " of type "
+ FeatureTypeName + ".\r\n";

  SysFreeString(bFeatureTypeName);
  SysFreeString(bFeatureName);
  // Return with Feature object
  return pSelectedFeature;
 }
 // Something went wrong. Clean up and report back without object.
 // Release the Selection Manager
 if(pSelectMgr)pSelectMgr->Release();
 // Release the unknown object
 if(pUnk)pUnk->Release();
 // Return with no object
 return NULL;
}
```

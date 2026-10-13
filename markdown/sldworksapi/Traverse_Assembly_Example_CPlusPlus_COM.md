---
title: "Traverse Assembly Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Assembly_Example_CPlusPlus_COM.htm"
---

# Traverse Assembly Example (C++ COM)

This example shows how to traverse an assembly using the IComponent2 object. The method IComponent2::IGetChildren returns an array, so this code must be used in an in-process DLL. Otherwise, use the method IComponent2::GetChildren that returns a VARIANT.

```vb
void GetModelAssembly(ISldWorks* m_pSldWorks)
{
 LPCONFIGURATION pConfiguration = NULL;
 LPCOMPONENT pRootComponent = NULL;

 LPMODELDOC2 pModelDoc = NULL;
 HRESULT hres = S_OK;
 long RecurseLevel = 0;

 hres = m_pSldWorks->get_IActiveDoc2( &pModelDoc );

 // Retrieve model document pointer
 if( S_OK != hres || pModelDoc == NULL )
  return;

 // Get the active configuration and root component
 if ( pModelDoc->IGetActiveConfiguration(&pConfiguration) == S_OK )
 {
  if ( pConfiguration->IGetRootComponent(&pRootComponent) == S_OK )
  {
   CString MyString;
   TraverseChildren(RecurseLevel,&MyString,pRootComponent);

   pRootComponent->Release();

   // Display the structure in a message box
   AfxMessageBox (MyString);
  }
  pConfiguration->Release();
 }
 pModelDoc->Release();

}

//////////////////////////////////////////////////////////////////////////
// Function: TraverseChildren
// Arguments: RecurseLevel - Level of recursion
//    MyString - Textural record of assembly
//    pComponent - Component to traverse
// Return: Number of children
// Description: Perform any operations specific to the component, then
//    if the component has children, recursively call
//    this function for each child.
//////////////////////////////////////////////////////////////////////////
int TraverseChildren(long RecurseLevel, CString* MyString, LPCOMPONENT pComponent)
{
 LPCOMPONENT* pChildren = NULL;
 int   nChildren;
 int   i;
 BSTR   Name;
 HRESULT  hres = S_OK;
 LPMODELDOC  pModelDoc = NULL;

 // Retrieve the component name
 if(RecurseLevel==0)
 {
  // Special case of top-level components
  hres = m_pSldWorks->get_IActiveDoc( &pModelDoc );
  if( S_OK == hres || pModelDoc != NULL )
   hres = pModelDoc->GetTitle(&Name);
 }
 else
 {
  // Get the component name
  hres = pComponent->get_Name(&Name);
 }

 if( S_OK == hres && Name != NULL )
 {
  CString tempstr;
  for( i=1; I<=RecurseLevel; i++)
  {
   tempstr += " ";
  }

  CString Tmp(Name);
  tempstr += Tmp;
  tempstr += "\r\n";
  *MyString = *MyString + tempstr;
 }

 RecurseLevel++;

 hres = pComponent->IGetChildrenCount(&nChildren);

 // Check if this component has children
 if ( S_OK == hres || nChildren > 0 )
 {
  pChildren = new LPCOMPONENT [nChildren];

  hres = pComponent->IGetChildren((LPCOMPONENT**)&pChildren);
  if(S_OK == hres)
  {
   // Recursively traverse the children
   for ( i=0; i<nChildren; i++ )
   {
    TraverseChildren(RecurseLevel,MyString,pChildren[i]);
    pChildren[i]->Release();
   }
  }
  delete [] pChildren;
 }

 RecurseLevel--;
 return nChildren;
}
```

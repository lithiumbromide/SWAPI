---
title: "SelectionManagerC++"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SelectionManagerCPP.htm"
---

# SelectionManagerC++

## SelectionManager.cpp Written in C++

// SelectionManager.cpp : Defines the entry point for the console application

// Gets the selected objects in the active model document

#include "stdafx.h"

// Add the path to the SOLIDWORKS type libraries to the "Additional Include Directories".

#import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids // SOLIDWORKS type library

#import "swconst.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids // SOLIDWORKS constants type library

int _tmain(int argc, _TCHAR* argv[])

{

// Initialize COM

// Do this before using ATL smart pointers so COM is available

CoInitialize(NULL);

// Use a block so the smart pointers are destructed when the scope of this block is left

{

// Use ATL smart pointers

CComPtr<ISldWorks> swApp;

if(swApp.CoCreateInstance(__uuidof(SldWorks), NULL, CLSCTX_LOCAL_SERVER) != S_OK) {

return(0);

}

swApp->put_UserControl(VARIANT_TRUE);

swApp->put_Visible(VARIANT_TRUE);

CComPtr<IModelDoc2> swModel;

swApp->get_IActiveDoc2(&swModel);

if (! swModel) {

return(0);

}

CComBSTR strModelTitle;

long nDocumentType; // swDocumentTypes_e

swModel->GetTitle(&strModelTitle);

swModel->GetType(&nDocumentType);

CComPtr<ISelectionMgr> swSelectionManager;

long lNumSelections;

long nSelectionType; // swSelectType_e

CComPtr<IDispatch> swSelectedObject;

CComPtr<IFace2> swFace;

CComPtr<IEdge> swEdge;

swModel->get_ISelectionManager(&swSelectionManager);

swSelectionManager->GetSelectedObjectCount2(-1, &lNumSelections);

for (int i = 1; i <= lNumSelections; i++) {

swSelectionManager->GetSelectedObject6(i, -1, &swSelectedObject);

swSelectionManager->GetSelectedObjectType3(i, -1, &nSelectionType);

switch (nSelectionType) {

case swSelectType_e::swSelFACES:

swSelectedObject.QueryInterface(&swFace);

break;

case swSelectType_e::swSelEDGES:

swSelectedObject.QueryInterface(&swEdge);

break;

}

}

}

// ATL smart pointers are destructed so all COM objects you held on to are released

// Now you can safely shut down COM as you do not need it any longer

// Stop COM

CoUninitialize();

return(0);

}

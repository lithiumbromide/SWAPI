---
title: "FeatureTraversalC++"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/FeatureTraversalCPP.htm"
---

# FeatureTraversalC++

## FeatureTraversal.cpp Written in C++

// FeatureTraversal.cpp : Defines the entry point for the console application

// Traverses the FeatureManager design tree

#include "stdafx.h"

// Add the path to the SOLIDWORKS type libraries to the "Additional Include Directories".

#import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids // SOLIDWORKS type library

#import "swconst.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids // SOLIDWORKS constants type library

int _tmain(int argc, _TCHAR* argv[])

{

// Initialize COM

// Do this before using ATL smart pointers so COM is available.

CoInitialize(NULL);

// Use a block, so the smart pointers are destructed when the scope of this block is left

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

CComPtr<IFeature> swFeature;

CComPtr<IFeature> swSubFeature;

CComBSTR strFeatureName;

CComBSTR strFeatureType;

swModel->IFirstFeature(&swFeature);

while (swFeature) {

swFeature->get_Name(&strFeatureName);

swFeature->GetTypeName2(&strFeatureType);

swFeature->IGetFirstSubFeature(&swSubFeature);

while (swSubFeature) {

swSubFeature->get_Name(&strFeatureName);

swSubFeature->GetTypeName2(&strFeatureType);

CComPtr<IFeature> swNextSubFeature;

swSubFeature->IGetNextSubFeature(&swNextSubFeature);

swSubFeature = swNextSubFeature;

}

CComPtr<IFeature> swNextFeature;

swFeature->IGetNextFeature(&swNextFeature);

swFeature = swNextFeature;

}

}

// ATL smart pointers are destructed so all COM objects you held on to are released

// Now you can safely shutdown COM as you do not need it any longer

// Stop COM

CoUninitialize();

return(0);

}

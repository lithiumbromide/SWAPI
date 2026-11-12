---
title: "Access Assembly Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_Assembly_Example_CPlusPlus_COM.htm"
---

# Access Assembly Example (C++ COM)

This example shows how to open, explode and collapse, and create a drawing of an assembly. It also shows how to traverse the FeatureManager design tree, get a component, and suppress and resolve that component. This example uses CComPtr Smart_Pointers.htm and CComBSTR smart types.

#### DemoAssemblies.cpp: application code

```vb
 ///////////////////////////////////////////////////////////////////////
//
// Preconditions:  ujoint.sldasm exists in the specified folder and
//                contains a component named bracket-1.
//
//
// Postconditions: None
//
// NOTE: Scroll down see the code for the stdafx.h header file.
//
 ///////////////////////////////////////////////////////////////////////

#include "stdafx.h"

VARIANT_BOOL retVal = VARIANT_FALSE;
HRESULT hres = NOERROR;

//Function prototypes
void OpenAssembly(ISldWorks* swApp, IModelDoc2** swModel);
void TraverseFeatureManagerDesignTree(IModelDoc2* swModel, IComponent2** swComponent);
void SuppressSelectedComponent(IComponent2* swComponent, ISldWorks* swApp);
void ResolveSelectedComponent(IComponent2* swComponent, ISldWorks* swApp);
void ExplodeAssembly(IModelDoc2* swModel, IAssemblyDoc** swAssemblyDoc);
void CollapseAssembly(IModelDoc2* swModel, IAssemblyDoc* swAssemblyDoc);
void CreateDrawingOfAssembly(ISldWorks* swApp, IModelDoc2* swModel);
void CloseDocuments(ISldWorks* swApp);

using namespace std;

int _tmain()
{
//Initialize COM
CoInitialize(NULL);

//Use ATL smart pointers
CComPtr<ISldWorks> swApp;
CComPtr<IModelDoc2> swModel;
CComPtr<IComponent2> swComponent;
CComPtr<IAssemblyDoc> swAssemblyDoc;

bool bDone;

do
{
try
{
//Open or attach to the currently running instance of the sldworks.exe
//COM server on your local computer; throw an exception if
//SOLIDWORKS Design is not opened or attached to
hres = swApp.CoCreateInstance(__uuidof(SldWorks), NULL, CLSCTX_LOCAL_SERVER);

if (hres != S_OK)
throw 0;

bDone = true;

IModelDoc2* swModel = NULL;

//Open assembly
OpenAssembly(swApp, &swModel);
IComponent2* swComponent = NULL;

//Traverse FeatureManager design tree to get specified feature
 TraverseFeatureManagerDesignTree(swModel, &swComponent);

//Suppress selected component if it is resolved
 SuppressSelectedComponent(swComponent, swApp);

//Resolve selected component if it is suppressed
 ResolveSelectedComponent(swComponent, swApp);
IAssemblyDoc* swAssemblyDoc = NULL;

//Explode assembly
ExplodeAssembly(swModel, &swAssemblyDoc);

//Collapse exploded assembly
CollapseAssembly(swModel, swAssemblyDoc);

//Create drawing of assembly
CreateDrawingOfAssembly(swApp, swModel);

//Close documents
CloseDocuments(swApp);

}
//Catch the exception and tell the user that SOLIDWORKS Design is not running
catch (int)
{
cout << "Error starting or attaching to a SOLIDWORKS Design session." << endl;

//Release COM references
swApp = NULL;
swModel = NULL;
swComponent = NULL;
swAssemblyDoc = NULL;

//Uninitialize COM
CoUninitialize();

return 1;
}
}
while(!bDone);

//Release COM references
swApp = NULL;
swModel = NULL;
swComponent = NULL;
swAssemblyDoc = NULL;

//Uninitialize COM
CoUninitialize();

return 0;
}
void OpenAssembly(ISldWorks* swApp, IModelDoc2** swModel)
//Open assembly
{
CComBSTR sFileName(L"c:\\test\\universaljoint\\ujoint.sldasm");
CComBSTR sDefaultConfiguration(L"Default");

long fileerror, filewarning;

IModelDoc2* swModelAssembly;
hres = swApp->OpenDoc6(sFileName, swDocASSEMBLY, swOpenDocOptions_Silent, sDefaultConfiguration, &fileerror, &filewarning, &swModelAssembly);
*swModel = swModelAssembly; //Set the value of the input argument equal to address of the interface
}

void TraverseFeatureManagerDesignTree(IModelDoc2* swModel, IComponent2** swComponent)
// Traverse FeatureManager design tree to get the
// specified feature in FeatureManager design tree
{
//Use ATL smart pointers
CComPtr<IFeature> swFeature;
CComPtr<ISelectionMgr> swSelMgr;

CComBSTR sGetFeatureName(L"");
CComBSTR sFeatureName(L"bracket-1");

bool bFoundComponents = false;
hres = swModel->IFirstFeature(&swFeature);
// If the name of the feature is "bracket-1"
// then select the feature
do
{
hres = swFeature->get_Name(&sGetFeatureName);
if (sGetFeatureName == sFeatureName)
{
hres = swFeature->Select2(true, 1, &retVal);
hres = swModel->get_ISelectionManager(&swSelMgr);
struct IDispatch *pComponentDisp;
hres = swSelMgr->GetSelectedObject6(1, -1, &pComponentDisp);
IComponent2* swSelectedComponent;
hres = pComponentDisp->QueryInterface(__uuidof(IComponent2), reinterpret_cast<void**>(&swSelectedComponent));
pComponentDisp->Release();
*swComponent = swSelectedComponent;  //Set the value of the input argument equal to address of the interface
bFoundComponents = true;
}
else
//Get next feature
{
CComPtr<IFeature> swFeatureNext;
hres = swFeature->IGetNextFeature(&swFeatureNext);
swFeature.Release();
swFeature = swFeatureNext;
}
}while ( !bFoundComponents);
}

void SuppressSelectedComponent(IComponent2* swComponent, ISldWorks* swApp)
//Suppress selected component if it is resolved
{
CComBSTR messageSuppressed (L"Component is already suppressed.");

long lComponentSuppressState;
long lSuppressMessageResult;
long lSuppressError;

hres = swComponent->GetSuppression(&lComponentSuppressState);
if (lComponentSuppressState == swComponentSuppressed)
hres = swApp->SendMsgToUser2(messageSuppressed, swMbInformation, swMbOk, &lSuppressMessageResult);
else
hres = swComponent->SetSuppression2(swComponentSuppressed, &lSuppressError);
}

void ResolveSelectedComponent(IComponent2* swComponent, ISldWorks* swApp)
//Resolve selected component if it is suppressed
{
CComBSTR messageResolved (L"Component is already resolved.");

long lComponentResolveState;
long lResolveMessageResult;
long lResolveError;

hres = swComponent->GetSuppression(&lComponentResolveState);
if (lComponentResolveState == swComponentFullyResolved)
hres = swApp->SendMsgToUser2(messageResolved, swMbInformation, swMbOk, &lResolveMessageResult);
else
hres = swComponent->SetSuppression2(swComponentFullyResolved, &lResolveError);
}

void ExplodeAssembly(IModelDoc2* swModel, IAssemblyDoc** swAssemblyDoc)
//Explode assembly
{
CComPtr<IModelView> swExplodeModelView;

double dZoomFactorOut = 0.3;

IAssemblyDoc* swThisAssemblyDoc;
hres = swModel->get_IActiveView(&swExplodeModelView);
hres = swExplodeModelView->ZoomByFactor(dZoomFactorOut);
hres = swModel->QueryInterface(__uuidof(IAssemblyDoc), reinterpret_cast<void**>(&swThisAssemblyDoc));
hres = swThisAssemblyDoc->AutoExplode(&retVal);
*swAssemblyDoc = swThisAssemblyDoc;
}

void CollapseAssembly(IModelDoc2* swModel, IAssemblyDoc* swAssemblyDoc)
//Collapse assembly
{
hres = swAssemblyDoc->AutoExplode(&retVal);
hres = swAssemblyDoc->ViewCollapseAssembly();
hres = swModel->ViewZoomtofit2();
}

void CreateDrawingOfAssembly(ISldWorks* swApp, IModelDoc2* swModel)
//Create a drawing of the assembly
{
CComPtr<IModelDoc2> swNewModel;
CComPtr<IModelDocExtension> swModelDocExt;
CComPtr<IDrawingDoc> swDrawingDoc;

CComBSTR sDrawingDocTemplate (L"c:\\Program Files\\SOLIDWORKS\\data\\templates\\Drawing.drwdot");
CComBSTR sActiveAssembly (L"c:\\test\\universaljoint\\ujoint.sldasm");
CComBSTR sDrawingDocName (L"ujoint - Sheet1");

double dWidth = 0.2794;
double dHeight = 0.4318;
long lPaperSize = 2;
long lWindowStyle = 2;
long lErrorActivatingDoc;
hres = swApp->INewDocument2(sDrawingDocTemplate, lPaperSize, dWidth, dHeight, &swNewModel);
swDrawingDoc = swNewModel;
hres = swApp->ArrangeWindows(lWindowStyle);
hres = swModel->Release();
hres = swApp->IActivateDoc3(sActiveAssembly, false, &lErrorActivatingDoc, &swModel);
hres = swModel->get_Extension(&swModelDocExt);
hres = swModelDocExt->SelectByID2(sActiveAssembly, L"COMPONENT", 0.0, 0.0, 0.0, VARIANT_FALSE, 0, NULL, swSelectOptionDefault, &retVal);
swNewModel.Release();
hres = swApp->IActivateDoc3(sDrawingDocName, false, &lErrorActivatingDoc, &swNewModel);
hres = swDrawingDoc->Create3rdAngleViews(sActiveAssembly, &retVal);
}
void CloseDocuments(ISldWorks* swApp)
//Close assembly and drawing documents
{
swApp->CloseAllDocuments(true, &retVal);
}
```

#### stdafx.h: header file

```vb
 //////////////////////////////////////////////////////////////////////
//
//stdafx.h: include file for standard system include files,
// or project-specific include files that are used frequently, but
// are changed infrequently
//
 //////////////////////////////////////////////////////////////////////

#pragma once

#define WIN32_LEAN_AND_MEAN // Exclude rarely-used stuff from Windows headers
#include <stdio.h>
#include <tchar.h>
#define _ATL_CSTRING_EXPLICIT_CONSTRUCTORS // some CString constructors will be explicit

#include <windows.h>
#include <atlbase.h> //Microsoft's ATL helper classes
#include <iostream>

using namespace std;  //Use the standard C++ libraries for text output.

#import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids  //the SOLIDWORKS type library
#import "swconst.tlb"  raw_interfaces_only, raw_native_types, no_namespace, named_guids  //the SOLIDWORKS constant type library

// TODO: reference additional headers your program requires here
```

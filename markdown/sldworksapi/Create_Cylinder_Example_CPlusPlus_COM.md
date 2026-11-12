---
title: "Create Cylinder Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cylinder_Example_CPlusPlus_COM.htm"
---

# Create Cylinder Example (C++ COM)

This example shows how to create a cylinder.

```vb
'------------------------------------
'
' Preconditions: None.
'
' Postconditions: A cylinder is created.
'
'------------------------------------
#include "stdafx.h"
#include "CreateCylinder.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

#include <atlbase.h>

#import "sldworks.tlb" no_namespace raw_interfaces_only
#import "swconst.tlb" no_namespace

/////////////////////////////////////////////////////////////////////////////
// The one and only application object
CWinApp theApp;

using namespace std;

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
int nRetCode = 0;
// initialize MFC and print and error on failure
if (!AfxWinInit(::GetModuleHandle(NULL), NULL, ::GetCommandLine(), 0))
{
// TODO: change error code to suit your needs
cerr << _T("Fatal Error: MFC initialization failed") << endl;
nRetCode = 1;
}
else
{
::CoInitialize(NULL);
{
VARIANT_BOOL bRetval = VARIANT_FALSE;

CComPtr<ISldWorks> swApp;
swApp.CoCreateInstance(L"SldWorks.Application", NULL, CLSCTX_LOCAL_SERVER);

CComPtr<IModelDoc2> swDoc;
CComPtr<IModelDocExtension> swDocExt;
CComPtr<IFeatureManager> swFeatMgr;

swApp->get_IActiveDoc2(&swDoc);
swDoc->get_Extension(&swDocExt);
swDoc->get_FeatureManager(&swFeatMgr);

CComPtr<ISketch> swSketch;
swDoc->IGetActiveSketch2(&swSketch);
if (swSketch == NULL)
{
swDocExt->SelectByID2(L"Front Plane", L"PLANE", 0.0, 0.0, 0.0, VARIANT_FALSE, 0, NULL, swSelectOptionDefault, &bRetval);
swDoc->InsertSketch2(VARIANT_TRUE);
}
CComPtr<ISketchSegment> swSkSeg;
swDoc->ICreateCircle2(0.0, 0.0, 0.0, 0.025, 0.0, 0.0, &swSkSeg);

CComPtr<IFeature> swFeat;
swFeatMgr->FeatureExtrusion2(VARIANT_FALSE, VARIANT_FALSE, VARIANT_FALSE,
0, 0, 0.100, 0.100,
VARIANT_FALSE, VARIANT_FALSE, VARIANT_FALSE, VARIANT_FALSE, 0.0, 0.0,
VARIANT_FALSE, VARIANT_FALSE, VARIANT_FALSE, VARIANT_FALSE,
VARIANT_TRUE, VARIANT_FALSE, VARIANT_TRUE, 0, 0.0, VARIANT_FALSE, &swFeat);
}
::CoUninitialize();
}
return nRetCode;
}
```

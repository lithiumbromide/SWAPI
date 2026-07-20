---
title: "Get Scale Factor of Each Model View Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm"
---

# Get Scale Factor of Each Model View Example (C++)

This example shows how to get the scale factor of each model view in a part
document.

```
//-----------------------------------------
// Preconditions:
// 1. Start Microsoft Visual Studio 2019 or later.
//    a. Click File > New > Project > (C++ Windows) Console App.
//    b. Click Next.
//    c. Type the name of your project in Project Name.
//    d. Click Create.
//    e. Right-click project, select Add, New Item, Select ATL > ATL Support, Click Add.
//    f. Click Project > projectname Properties > Configuration Properties >
//       C/C++ and type the path to sldworks.tlb and swconst.tlb,
//       typically C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS,
//       in Additional Include Directories.
//    g. Click Apply or OK.
// 2. Replace the code in the code window with This code.
// 3. Click Debug > Start Debugging.
// 4. Start up SOLIDWORKS and open a part document.
// 5. Click Window > Viewport > Four View.
// 6. Click a model view and spin the middle-mouse
//    button forward or back.
// 7. Click Debug > Start Debugging.
//
// Postconditions:
// 1. Gets the number of model views in the part document.
// 2. Gets the scale factor of each model view.
// 3. Examine the Immediate Window.
//-----------------------------------------

//This code
#include "framework.h"
#include <iostream>
#include <sstream>
#import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids  // SOLIDWORKS type library
#import "swconst.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids   // SOLIDWORKS constants type library

int _tmain(int argc, _TCHAR* argv[])
{
		//Initialize COM
		//Do this before using ATL smart pointers so that
		//COM is available
		CoInitialize(NULL);

		//Use a block so that the smart pointers are destructed when
		//scope of this block is exited
		{
			//Use ATL smart pointers
			CComPtr<ISldWorks> swApp;
			if(swApp.CoCreateInstance(L"SldWorks.Application", NULL, CLSCTX_LOCAL_SERVER) != S_OK){
					return(0);
			}

			HRESULT hres;

			CComPtr<IModelDoc2> swDoc;
			swApp->get_IActiveDoc2(&swDoc);

			//Get number of model views
			CComPtr<IModelDocExtension> swDocExt;
			hres = swDoc->get_Extension(&swDocExt);
			long nbrModelViews;
			hres = swDocExt->GetModelViewCount(&nbrModelViews);
			_bstr_t s;
			s =(long)nbrModelViews;
			OutputDebugString("Number of model views: " + s + "\n");

			//Get an ISafeArrayUtility object
			CComPtr<IDispatch> dispatchSafeArray = NULL;
			CComPtr<ISafeArrayUtility> swSafeArray = NULL;
			hres = swApp->GetSafeArrayUtility(&dispatchSafeArray);
			hres = dispatchSafeArray->QueryInterface<ISafeArrayUtility>(&swSafeArray);

			//Pack a Variant SafeArray of Dispatch-based objects
			IDispatch** dispArray = new IDispatch*[nbrModelViews];
			VARIANT vPacked;
			::VariantInit(&varPersist);
			int arrType = swDispatchArray;
			hres = swSafeArray->PackVariant(&vPacked, nbrModelViews, arrType, (long*)dispArray);

			//Get the model views in the model document
			hres = swDocExt->GetModelViews(&vPacked);

			//Get scale factor of each model view
			for (int i = 0; i < nbrModelViews; i++)
			{
				CComPtr<IModelView>swModelView;
				IDispatch *pDisp;
				hres = swSafeArray->GetDispatch(vPacked, i, &pDisp);
				pDisp->QueryInterface(IID_IModelView, (void**)&swModelView);
				_bstr_t t;
				double scale;
				hres = swModelView->get_Scale2(&scale);
				t = (double)scale;
				OutputDebugString("Scale of this model view is: " + t + "\n");
			}

		}

	return 0;
}
```

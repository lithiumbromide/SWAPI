---
title: "Get Names of Configurations Using Variant Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/ConfigurationTraversalCPP.htm"
---

# Get Names of Configurations Using Variant Example (C++)

This example shows how to:

- get the names of the configurations in the
  active model.
- pass a Variant to IModelDoc2::GetConfigurationNames.
- use the ISafeArrayUtility interface
  to get the names of the configurations.

```
//-------------------------------------------------------
// Preconditions:
// 1. Start up SOLIDWORKS and open a part or assembly document.
// 2. Start Microsoft Visual Studio 2019 or later.
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
// 3. Replace the code in the code window with This code.
// 4. Click Debug > Start Debugging.
//
// Postconditions:
// 1. Pops up a message box for each configuration in the active
//    model that contains the name of that configuration.
// 2. Click OK to close each message box.
//--------------------------------------------------------

//This code
#include "framework.h"
#import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids  // SOLIDWORKS type library
#import "swconst.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids   // SOLIDWORKS constants type library

int _tmain(int argc, _TCHAR* argv[])
{
	// Initialize COM
	// Do this before using ATL smart pointers so that
	// COM is available
	CoInitialize(NULL);

	// Use a block so that the smart pointers are destructed when
	// the scope of this block is exited
	{
		// Use ATL smart pointers
		CComPtr<ISldWorks>  pSwApp;

		if(pSwApp.CoCreateInstance(__uuidof(SldWorks), NULL, CLSCTX_LOCAL_SERVER) != S_OK) {
			return(0);
		}

		pSwApp->put_UserControl(VARIANT_TRUE);
		pSwApp->put_Visible(VARIANT_TRUE);

		CComPtr<IModelDoc2>  pSwModel;
		pSwApp->get_IActiveDoc2(&pSwModel);

		if (! pSwModel) {
			return(0);
		}

		CComBSTR strModelTitle;
		long nDocumentType;  // swDocumentTypes_e

		pSwModel->GetTitle(&strModelTitle);
		pSwModel->GetType(&nDocumentType);

		VARIANT  vConfigurationNames;
		::VariantInit(&vConfigurationNames);

		// Get the names of the configurations in the active model
                  // NOTE: This is an out-of-process client, so you cannot
                  // use ModelDoc2::IGetConfigurationNames
		pSwModel->GetConfigurationNames(&vConfigurationNames);

		CComPtr<IDispatch> pDispatchSafeArray = NULL;
		CComPtr<ISafeArrayUtility> pSwSafeArray = NULL;
		HRESULT hres;
		hres = pSwApp->GetSafeArrayUtility(&pDispatchSafeArray);
		hres = pDispatchSafeArray.QueryInterface<ISafeArrayUtility>(&pSwSafeArray);

		long saCount = 0;
		long saType = 0;
		long* visible = 0;

		long nbrConfigs = 0;
		pSwModel->GetConfigurationCount(&nbrConfigs);

		//Get the name of each configuration
		for (long i = 0; i < nbrConfigs; i++) {
			BSTR configurationName;
			pSwSafeArray->GetBstr(vConfigurationNames, i, &configurationName);
			CComBSTR msg;
			msg = (OLESTR("Name of configuration: "));
			msg.Append(configurationName);
			long res;
			pSwApp->SendMsgToUser2(msg, 0,0, &res);
		}

	}
	// ATL smart pointers are destructed so that all COM objects
	// held on to are released
	// Shut down COM because you no longer need it

	// Stop COM
	CoUninitialize();

	return(0);
}
```

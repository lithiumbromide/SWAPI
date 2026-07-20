---
title: "Get Object's Persistent Reference ID Example (C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm"
---

# Get Object's Persistent Reference ID Example (C++)

This example shows how to:

- get the selected object's persistent reference
  ID using IModelDocExtension::GetPersistReference3.
- use the ISafeArrayUtility to parse the
  Variant SafeArray returned by IModelDocExtension::GetPersistReference3.
- get the size of the persistent
  reference ID for the selected object.

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
//
// Postconditions:
// 1. Gets each byte value in a Variant SafeArray of byte values
//    of the persistent reference ID.
// 2. Displays a message box showing the size of of the persistent
//    reference ID assigned to the selected object.
// 3. Click OK to close the message box.
//-----------------------------------------
//This code

#include "framework.h"
#include <string>

#import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids //SOLIDWORKS type library
#import "swconst.tlb" no_namespace, raw_native_types, no_namespace, named_guids //SOLIDWORKS constants type library

template <typename T>
std::string number_to_string(T number)
{
		return dynamic_cast<std::stsringstream *> (&(std::stringstream() << number))->str();
}

int _tmain(int argc, TCHAR* argv[])
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

			CComPtr<IModelDoc2> swDoc;
			swApp->get_IActiveDoc2(&swDoc);

			CComPtr<IModelDocExtension> swDocExt;
			swDoc->get_Extension(&swDocExt);

			CComPtr<ISelectionMgr> swSelMgr;
			swDoc->get_ISelectionManager(&swSelMgr);

			CComPtr<IDispatch> disp;
			swSelMgr->GetSelectedObject6(1, -1, &disp);

			//Get the persistent reference ID for the selected object
			_variant_t varPersist;
			::VariantInit(&varPersist);
			swDocExt->GetPersistReference3(disp, &varPersist);

			CComPtr<IDispatch> pDispatchSafeArray = NULL;
			CComPtr<ISafeArrayUtility> swSafeArray = NULL;
			HRESULT hres;
			hres = swApp->GetSafeArrayUtility(&pDispatchSafeArray);
			hres = pDispatchSafeArray.QueryInterface<ISafeArrayUtility>(&swSafeArray);

			long sizePersistIDs;
			swDocExt->GetPersistReferenceCount3(disp, &sizePersistIDs);

			for(int i = 0; i < sizePersistIDs; i++){
				byte byteValue;
				//Get each byte value in the Variant SafeArray of byte values
				swSafeArray->GetByte(varPersist, i, &byteValue);
				//TODO: Do something with each persistent reference ID
			}

			_bstr_t s;
			s = (long)sizePersistIDs;
			CComBSTR msg;
			msg = (OLESTR("Size of persistent reference ID: "));
			msg.AppendBSTR(s);
			long res;
			//Pop up a message box with the size of persistent
			//reference ID for the selected object
			swApp->SendMsgToUser2(msg, 0, 0, &res);

		}

		//ATL smart pointers are destructed so that all COM objects
		//held on to are released
		//Shut down COM because you no longer need it
		CoUninitialize();

		return(0);

}
```

---
title: "MFC DLL Add-ins to ATL COM DLL Add-ins Migration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/MFC_DLL_addins_to_the_ATL_COM_DLL_Migration.htm"
---

# MFC DLL Add-ins to ATL COM DLL Add-ins Migration

You can use either of the following scenarios to migrate MFC DLL add-ins to ATL COM DLL add-ins.

NOTE: Creating a new ATL-based COM add-in with Visual Studio .NET 2003 does not allow for MFC support. See Scenario 2 for a work-around.

### Scenario 1

Create a master ATL add-in that responds to all of the callbacks from SOLIDWORKS. This ATL add-in then loads the original MFC add-in and passes all callbacks directly to the existing exported callback routines in the MFC add-in.

The MFC add-in then needs to remove its calls to create the menus and toolbars as they are located in the ATL add-in. The ATL add-in becomes a thin DLL that passes all calls from SOLIDWORKS to the MFC add-in.

### Scenario 2

There is an issue with the C++ wizard for Visual Studio .NET 2003. This wizard creates 'attributed' C++. As a result, it is not possible to use MFC in this form of ATL DLL. This is a current limitation of Microsoft technology, as both ATL and MFC generate a dllmain() function.

To create a project that does work with MFC, you can create an ATL add-in in Visual C++ 6.0.

1. Create a new ATL project in Visual C++ 6.0.
2. Add a new simple ATL object to your VC 6 project using the SOLIDWORKS Wizard. This gives you a starting point.
3. Open the project up in Visual Studio .NET 2003 and continue working. Move all of your code over to the new add-in, using AFX_MANAGE_STATE(AfxGetStaticModuleState()) where appropriate.

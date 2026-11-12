---
title: "Using SwAddin to Create a SOLIDWORKS Addin"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Using_SwAddin_to_Create_a_SolidWorks_Addin.htm"
---

# Using SwAddin to Create a SOLIDWORKS Addin

## Using SwAddin to Create a SOLIDWORKS Add-In

You can create a SOLIDWORKS add-in using the [ISwAddin](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwAddin.html) object instead of using a [SOLIDWORKS add-in wizard](SolidWorks_API_Add-Ins,_Project_Templates,_and_Wizards.htm).

When you use the ISwAddin object to create a SOLIDWORKS add-in, the add-in must include some specific functionality and code. It is also important to understand what SOLIDWORKS Design does for the add-in. Click a link to read that section.

- [What does the add-in have to do?](#addin)
- [What does SOLIDWORKS Design do?](#application)

### What does the add-in have to do?

The add-in DLL must be created as a COM Server and it must:

1. Implement a co-creatable object that supports SwAddin.
2. During installation call:

- **Regsvr32.exe** for unmanaged C++ and managed C++/CLI add-ins. See [How to use the Regsvr32 tool and troubleshoot Regsvr32 error messages](https://support.microsoft.com/en-us/kb/249873) for details.

Register the add-in's CLSID in **HKEY_LOCAL_MACHINE\SOFTWARE\SOLIDWORKS\AddIns** and set the following registry keys:

- Default to 1 or 0, where 1 enables the add-in in the add-in manager so that it loads when the user starts SOLIDWORKS Design.
- Description to a text description of the add-in that is displayed in the add-in manager.
- Title to a text title of the description that is displayed in the add-in manager.

- **RegAsm.exe** for C# and VB.NET add-ins. See [Registering Assemblies with COM](https://msdn.microsoft.com/en-us/library/h627s4zy(v=vs.110).aspx) for details.

1. Define event handlers as needed.

In its implementation of [ISwAddin::ConnectToSW](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwAddin~ConnectToSW.html), the add-in can:

1. Call [ISldWorks::SetAddinCallbackInfo](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks~SetAddinCallbackInfo.html) and pass the instance handle of the add-in and the object that supports the callback methods. SOLIDWORKS Design holds onto this object and makes callbacks.
2. Call [ISldWorks::AddMenuItem3](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks~AddMenuItem3.html) and pass the callback method associated with the menu item.
3. Call [ISldWorks::AddToolbar4](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks~AddToolbar4.html) and pass the callback method associated with the toolbar button.

[Back to top](#top)

### What does SOLIDWORKS Design do?

When the end-user starts SOLIDWORKS Design, SOLIDWORKS Design:

1. Checks the registry for add-ins.
2. Creates an object associated with the CLSID of the add-in.
3. Performs a QueryInterface on the add-in looking for the SwAddin object.
4. Calls [ISwAddin::ConnectToSW](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwAddin~ConnectToSW.html).

When the user closes SOLIDWORKS Design or disables an add-in in the add-in Manager, SOLIDWORKS Design:

1. Calls [ISwAddin::DisconnectFromSW](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwAddin~DisconnectFromSW.html), providing the add-in an opportunity for cleanup.
2. Destroys the object it created with the add-in CLSID.

If the end-user disables an add-in in the add-in manager, SOLIDWORKS Design does not reload it the next time SOLIDWORKS Design starts. If the end-user closes SOLIDWORKS Design with an add-in enabled, SOLIDWORKS Design reloads the add-in the next time it starts.

[Back to top](#top)

To learn more about add-ins and their menu items and toolbars:

- [Add-in Callbacks](Add-in_Callbacks.htm)
- [Add-in Icons](Add-in_Icons.htm)
- [Add-in Shortcut Menus](Add-in_Shortcut_Menus.htm)
- [Add-in Toolbars](Add-in_Toolbars.htm)

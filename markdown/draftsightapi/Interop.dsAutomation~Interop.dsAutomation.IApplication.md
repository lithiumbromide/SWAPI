---
title: "IApplication Interface"
project: ""
interface: "IApplication"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication.html"
---

# IApplication Interface

Allows access to all exposed interfaces in the DraftSight API.

## Syntax

### Visual Basic

```vb
Public Interface IApplication
```

### C#

```csharp
public interface IApplication
```

### JScript

```
public interface IApplication
```

### Managed Extensions for C++

```
public __gc __interface IApplication
```

### C++/CLI

```cpp
public interface class IApplication
```

## Examples

The following code snippets show how to get the IApplication object:

- COM native C++ (from the DraftSight API [COM native C++ template file](GettingStarted-draftsightapi.html) **DsAddinConnection.h**)
- [C++](#CPP) (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

public:

CComQIPtr<IApplication> m_DsApp;

public:
STDMETHOD(ConnectToDraftSight)(LPDISPATCH DsApp, long Cookie, VARIANT_BOOL * IsConnected)
{
m_DsApp = DsApp;
IUnknown* dsUnk = NULL ;
HRESULT hr = DsApp->QueryInterface(IID_IUnknown, (void **) &dsUnk)

}

##### C++

myApplication *myApp = NULL;

const dsString myApplication::appID = L"`Replace_with_`a`dd-in's`_`GUID`";

#ifdef DS_WIN

DSADDINSAMPLE_EXPORT bool connectToDraftSight(int cookie, dsApplication_c *dsApp)

#else //DS_WIN

extern "C" DSADDINSAMPLE_EXPORT bool connectToDraftSight(int cookie, dsApplication_c *dsApp)

#endif //DS_WIN

{

if ( myApp == NULL )

{

myApp = new myApplication(dsApp);

myApp->CreateUserInterfaceAndCommands();

return true;

}

return false;

}

[Back to top](#examplebookmark)

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)
[Get and Set Document Settings (C#)](Get_and_Set_Document_Settings_Example_CSharp.htm)
[Get and Set Document Settings (VB.NET)](Get_and_Set_Document_Settings_Example_VBNET.htm)
[Get and Set Document Settings (VBA)](Get_and_Set_Document_Settings_Example_VBA.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (C#)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VB.NET)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBNET.htm)
[Get and Set Block Definitions, Block Instances, and BlockAttribute Instances (VBA)](Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_VBA.htm)
[Get and Set Print Options (C#)](Get_and_Set_Print_Options_Example_CSharp.htm)
[Get and Set Print Options (VB.NET)](Get_and_Set_Print_Options_Example_VBNET.htm)
[Get and Set Print Options (VBA)](Get_and_Set_Print_Options_Example_VBA.htm)
[Switch Layouts (C#)](Switch_Layouts_Example_CSharp.htm)
[Switch Layouts (VB.NET)](Switch_Layouts_Example_VBNET.htm)
[Switch Layouts (VBA)](Switch_Layouts_Example_VBA.htm)
[Insert Lines and Angular Dimension (JavaScript)](Insert_Lines_and_Angular_Dimension_Example_JS.htm)
[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)
[Insert Block, Notes, and Sketch Entities (JavaScript)](Insert_Block_Notes_and_Sketch_Entitites_Example_JS.htm)
[Insert Splines (JavaScript)](Insert_Splines_Example_JS.htm)
[Insert HyperLink (JavaScript)](Insert_HyperLink_Example_JS.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)
[Mirror Entities (JavaScript)](Mirror_Entities_Example_JS.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)
[Create Model and Sheet Views (JavaScript)](Create_Model_and_Sheet_Views_Example_JS.htm)

## Access Diagram

[Application](DSObjectModel.pdf#Application)

## See Also

[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IApplication Event ActiveDocumentChangedNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_ActiveDocumentChangedNotifyEventHandler.html)
[IApplication Event DestroyNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_DestroyNotifyEventHandler.html)
[IApplication Event FileNewNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileNewNotifyEventHandler.html)
[IApplication Event FileOpenPostNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileOpenPostNotifyEventHandler.html)
[IApplication Event FileOpenPreNotify](Interop.dsAutomation~Interop.dsAutomation._IApplicationEvents_FileOpenPreNotifyEventHandler.html)

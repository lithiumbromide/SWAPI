---
title: "Getting Started"
project: "DraftSight API Help"
interface: ""
member: ""
kind: "topic"
source: "draftsightapi/GettingStarted-draftsightapi.html"
---

# Getting Started

This topic contains information to help you get started with automating and creating add-ins for DraftSight. This topic also contains general information about the DraftSight API.

- [DraftSight type libraries and primary interop assemblies](#TypeLibrariesAssemblies)
- [DraftSight API automation](#Automation)
- [Microsoft Visual Studio DraftSight API templates and add-ins](#Templates)
- - [C#](#CSharpTemplate)
  - [VB.NET](#VBNETTemplate)
  - [COM native C++](#COMTemplate)#COMAddin
  - [C++](#CPPTemplate)

    - [Smart pointers](#CPPSmartPointers)
    - [Callback functions](#CPPCallbackFunctions)
  - [addinConfigs folder and project-specific XML files](#addinConfigs)
  - [Add-in activation and deactivation](#ActivateAdd-ins)
- [COM native C++ and C++ interface data types](#DataTypes)

  - [HRESULT and DSRESULT values](#ReturnValues)
- [JavaScript](#JavaScript)

  - [Supported web browsers](#SupportedWebBrowsers)
  - [Editors](#Editors)
  - [Debuggers](#Debuggers)
  - [Disassociating from server-side memory](#DisassocateFromMemory)
  - [Syntax](#Syntax)
  - [Troubleshooting startup](#ToubleshootJS)
- [Code to connect to DraftSight](#ConnectingCode)

  - [C#](#CSharp)
  - [VB.NET](#VB.NET)
  - [VBA](#VBA)
  - [JavaScript](#JS)
- [Access to objects in DraftSight API](#AccessingObjects)
- [convertVariantArrayToPtrArray method](#convertVariantArrayToPtrArray)
- [Tips and tricks for 3D modeling in DraftSight](#3D)

[Sample Projects](SampleProjects.htm) are available to DraftSight users with network licenses.

**NOTE:** Italicized words in this topic and throughout the Help indicate where you should substitute the actual names of the entities that exist on your computer, in your add-in project, and elsewhere.

##### DraftSight type libraries and primary interop assemblies

The DraftSight API type libraries and primary interop assemblies are:

- Type libraries:

  - `install_dir`\APISDK\tlb\dsAddin.tlb
  - `install_dir\`**bin\dsAutomation.dll**
- Primary interop assemblies:

  - install_dir\APISDK\tlb\**DraftSight.Interop.dsAddin.dll**
  - install_dir\APISDK\tlb\**DraftSight.Interop.dsAutomation.dll**

The DraftSight `install_dir` path is typically **C:\Program Files\Dassault Systemes\DraftSight**.

**NOTE:** After upgrading to a new version of the DraftSight API, you must replace references to DraftSight API type libraries and primary interop assemblies in existing DraftSight API projects developed in Microsoft Visual Studio. See the Microsoft Visual Studio documentation for details on how to add and remove references in a project.

[Back to top](#Top)

##### DraftSight API automation

You can automate DraftSight by writing standalone applications.

Visual C#, VB.NET, and VBA, examples illustrating DraftSight applications are included in the Help that you can copy, paste, and run in the respective language's integrated development environment (IDE). Copy and paste the JavaScript examples into HTML files.

Examples are linked to individual Help topics when the subject of the Help topic appears in the examples.

**NOTE:** See the Example section of a Help topic to locate the links to its associated examples. Some topics contain COM native C++ and C++ code, so be sure to scroll to the Example section that contains the links to the Visual C#, JavaScript, VB.NET, and VBA examples.

[Back to top](#Top)

##### Microsoft Visual Studio DraftSight API templates and add-ins

When you installed the DraftSight API SDK, the DraftSight API project templates for Microsoft Visual Studio VB.NET, C#, and C++ were installed if Microsoft Visual Studio was detected on your computer. After installing the DraftSight API SDK, the DraftSight API project templates are available in Microsoft Visual Studio's New Project dialogs.

The DraftSight API project templates provide you with a basis for creating your add-in projects in Microsoft Visual Studio.

Building a project in Microsoft Visual Studio from a DraftSight add-in template creates an add-in DLL. Copy the DLL to `install_dir\`bin\addins\`addin_name_folder`. Add the add-in DLL to DraftSight (on the DraftSight menu, click **Tools > Options > Add-ins > New**). Navigate to `add_name_folder` and click **Open**. After the add-in DLL has been added to DraftSight, you will see the add-in in the DraftSight **[Tools > Add-Ins](#ActivateAdd-ins)** dialog. When active, the add-in adds its:

- command for the menu bar
- toolbar button
- command for the command window

to DraftSight. Clicking the add-in command on the menu bar and selecting **Open Notepad**, clicking the add-in toolbar button, or typing the add-in command in the command window opens Microsoft Notepad.

[Back to top](#Top)

###### Creating a C# add-in using the template

To create a project using the C# add-in template:

1. Click **Start > Programs > Microsoft Visual Studio** `version_number` **> Microsoft Visual Studio** `version_number`.
2. Click the **New Project** button.

  1. Select **Visual C#** in **Other Languages**.
  2. Select **DSAddinCSharp** in **Templates**.
  3. Type the name of your project in **Name**.
  4. Click **OK**.

The COM server for the add-in is created when the project is created.

To get acquainted with the contents of the files created by the template, examine the Solution Explorer and the following table.

| C# Files | Description |
| --- | --- |
| BitmapHandler.cs | This file contains the class to handle the add-in's images . |
| DsAddin.cs | This file contains the main add-in class. |
| DsAddinCommand.cs | This file contains the DsAddinCommand class that handles events thrown when a command executes. There is an instance of this class for every add-in command. This file also contains the DraftSight ICommand event callback functions. |
| DsAddinDocument.cs | This file contains the DsAddinDocument class that handles events thrown by open drawing documents. There is an instance of this class for every open drawing document. This file also contains the DraftSight IDocument event callback functions. |
| DsAddinUserCommand.cs | This file contains the DsAddinUserCommand class, which you use to create commands for menu items and toolbar items, get command IDs, and validate commands. |

[Back to top](#Top)

###### Creating a VB.NET add-in using the template

To create a project using the VB.NET add-in template:

1. Click **Start > Programs > Microsoft Visual Studio** `version_number` **> Microsoft Visual Studio** `version_number`.
2. Click the **New Project** button.

  1. Select **Visual Basic**.
  2. Select **DSAddinVBNet** in **Templates**.
  3. Type the name of your project in **Name**.
  4. Click **OK**.

The COM server for the add-in is created when the project is created.

To get acquainted with the contents of the files created by the template, examine the Solution Explorer and the following table.

| VB.NET Files | Description |
| --- | --- |
| BitmapHandler. vb | This file contains the class to handle the add-in's images . |
| DsAddinCommand. vb | This file contains the DsAddinCommand class that handles events thrown when a command executes. There is an instance of this class for every add-in command. This file also contains the DraftSight ICommand event callback functions. |
| DsAddinDocument.vb | This file contains the DsAddinDocument class that handles events thrown by open drawing documents. There is an instance of this class for every open drawing document. This file also contains the DraftSight IDocument event callback functions. |
| DsAddinUserCommand. vb | This file contains the DsAddinUserCommand class, which you use to create commands for menu items and toolbar items, get command IDs, and validate commands. |
| DsAddinVBNet. vb | This file contains the main add-in class. |

###### Back to top

###### Creating a COM native C++ interface add-in using the template

To create a project using the COM native C++ interface add-in template:

1. Click **Start > Programs > Microsoft Visual Studio** `version_number` **> Microsoft Visual Studio** `version_number`.
2. Click the **New Project** button.

  1. Select **Visual C++** in **Other Languages**.
  2. Select **DraftSight COM Addin** in **Templates**.
  3. Type the name of your project in **Name**.
  4. Type the path where to create the project in **Location**.
  5. Click **OK**.

The COM server for the add-in is created when the project is created.

To get acquainted with the contents of the files created by the template, examine the Solution Explorer and the following table.

| COM Native C++ Files | Description |
| --- | --- |
| DsAddin.def | This file declares DLL function exports. |
| DsAddin.idl | This file is used to generate the type library for the add-in. |
| DsAddinCommand.cpp and corresponding .h file | These files contain the DsAddinCommand class that handles events thrown when a command executes. There is an instance of this class for every add-in command. These files also contain the DraftSight ICommand event callback functions. |
| DsAddinConnection.cpp and corresponding .h file | These are the main add-in files. They contain the implementation of the IDsAddin interface. These files also contain IDsAddin::ConnectToDraftSight and IDsAddin::DisconnectFromDraftSight, which are the entry and exit functions for this add-in. The DraftSight IApplication event callback functions and the CreateUserInterfaceAndCommands method that creates the add-in's user interface and commands also appear in these files. |
| DsAddinConnection.rgs | This file contains the information that automatically registers your add-in with DraftSight when it is compiled. |
| DsAddinDocument.cpp and corresponding .h file | These files contain the DsAddinDocument class that handles events thrown by open drawing documents. There is an instance of this class for every open drawing document. These files also contain the DraftSight IDocument event callback functions. |
| DsAddinUserCommand.cpp and corresponding .h file | These files contain the DsAddinUserCommand class, which you use to create commands for menu items and toolbar items, get command IDs, and validate commands. |
| stdafx.cpp and corresponding .h file | These files contain the #import statements for the DraftSight type libraries and any other necessary DraftSight #include statements. |
| smartvars.cpp and corresponding .h file | These files define templates to more easily handle Variants in an add-in. |

###### Back to top

###### Creating a C++ interface add-in using the template

To create a project using the C++ interface add-in template:

1. Click Start > Programs > Microsoft Visual Studio `version_number` > Microsoft Visual Studio `version_number`.
2. Click the New Project button.

  1. Select **Visual C++** in **Other Languages**.
  2. Select **DraftSight** **CPP Addin** in **Templates**.
  3. Type the name of your project in Name.
  4. Type the path where to create the project in **Location**.
  5. Click OK.

To get acquainted with the contents of the files created by the template, examine the Solution Explorer and the following table.

| C++ Files | Description |
| --- | --- |
| Ds Addin.def | This file declares DLL function exports. |
| dsAddinConnection.cpp and corresponding .h file | These are the main add-in files. These files contain ConnectToDraftSight and DisconnectFromDraftSight, which are the entry and exit functions for this add-in. These files also contain the DraftSight IApplication event callback functions, the ICommand callback function, and the CreateUserInterfaceAndCommands method that creates the add-in's user interface and commands. |
| dsAddinDocument.cpp and corresponding .h file | These files contain the DsAddinDocument class that handles events thrown by open drawing documents. There is an instance of this class for every open drawing document. These files also contain the DraftSight IDocument event callback functions. |
| Interface header files | These files are located in install_dir \APISDK\headers\cpp. |
| stdafx.cpp and corresponding .h file | These files contain the #import statements for the DraftSight type libraries and any other necessary DraftSight #include statements. |

**NOTE**: DraftSight API C++ add-ins that were last compiled in DraftSight V1R2.0, or earlier, must be recompiled with the header files shipped with DraftSight API V1R2.1, or later, due to changes made to multiple signatures in DraftSight API V1R2.1.

[Back to top](#Top)

###### C++ interface add-in template smart pointers

The C++ interface add-in template provides two C++ smart pointer (_ptr) classes for use in your projects to manage object lifecycles. The header files containing the C++ _ptrs reside in `install_dir`\**APISDK\headers\cpp** and are named:

- dsInterfacePtr.h
- dsInterfaceArrayPtr.h

To use these C++ _ptrs, you must include these header files in your projects because the _ptrs are template classes and their implementations are defined in these header files. There are no library dependencies.

[Back to top](#Top)

###### C++ interface add-in template callback functions

The C++ interface add-in template uses macros to:

- register and unregister C++ interface callback functions.
- declare the C++ interface callback functions.
- implement the C++ interface callback functions.

| Events for these interfaces... | Defined in... | Registered, unregistered, and declared in... | Implemented in... |
| --- | --- | --- | --- |
| IApplication | dsApplication_c.h | dsAddinConnection.h | dsAddinConnection.cpp |
| ICommand | dscommand_c.h | dsAddinConnection.cpp | dsAddinConnection.cpp |
| IDocument | dsDocument_c.h | dsAddinDocument.h | dsAddinDocument.cpp |
| ISelectionManager | dsSelectionManager_c.h | Not used in template | Not used in template |

[Back to top](#Top)

###### addinConfigs folder and project-specific XML files

###### Microsoft Windows operating systems

Microsoft Vista and Windows Windows 7 and later operating systems include User Account Control (UAC). If you use a DraftSight add-in template to create your add-in project, then UAC affects whether the **addinConfigs** folder and the project-specific XML file are created.

| If UAC is turned... | Then... |
| --- | --- |
| Off | the project-specific XML file is created in the %PROGRAMDATA%\Dassault Systemes\DraftSight \addinConfigs folder, where %PROGRAMDATA% is typically C:\ProgramData . The addinConfigs folder is created by the template, if it does not already exist. The name of the XML file is the name of your project followed by the .xml file name extension. |
| On | the project-specific XML file is created in the project folder. You must manually create the DraftSight %PROGRAMDATA%\Dassault Systemes\DraftSight \addinConfigs folder, if it does not already exist. You must move the project-specific XML file to the addinConfigs folder. The name of the XML file is the name of your project followed by the .xml file name extension. The %PROGRAMDATA% path is typically C:\ProgramData. |

**NOTE**: Refer to Microsoft's documentation or contact your system administrator for details about UAC.

If you do not use a DraftSight template to create your add-in project, then you must manually create the **addinConfigs** folder, if it does not already exist, in **%PROGRAMDATA%\Dassault Systemes\DraftSight**`,` which is typically **C:\ProgramData\Dassault Systemes\DraftSight**.

You must also manually create a project-specific XML file for each of your add-in projects. The name of each XML file is the name of your project followed by the **.xml** file name extension. The XML file must reside in the **addinConfigs** folder.

###### Add-in project's XML file syntax

An add-in project's XML file contains specific and slightly different syntax. Shown next are sample language-specific XML files. Use the same syntax (substituting actual names for italicized text) and the suggested format when you manually create either file.

###### C#, VB.NET, and COM native C++

<addinmanager>
<draftsight version="">
<addin help="`add-in_ToolTip_in_Add-in_Manager`" startup="1" name="`add-in_project_name`" premiumOnly="2">
<com clsid="`your_generated_add-in_COM_CLSID`"></com>
<button bitmap="`path_and_name_of_image_for_add-in_icon_in_Add-in_manager`"></button>
</addin>
</draftsight>
</addinmanager>

###### C++

<addinmanager>
<draftsight version="">
<addin help="`add-in_ToolTip_in_Add-in_Manager`" startup="1" name="`add-in_project_name`" premiumOnly="2">
<button bitmap="`path_and_name_of_image_for_add-in_icon_in_Add-in_manager`"></button>
<cpp pathname="`add-in_project_name`.dll"></cpp>
</addin>
</draftsight>
</addinmanager>

**NOTES:**

- Setting premiumOnly = 1 indicates to load add-ins for both DraftSight Pro and Premium versions; setting premiumOnly = 2 indicates to load add-ins only for the DraftSight Premium version.
- Setting startup = 1 indicates to show the add-in on the DraftSight **Tools > Add-Ins** manager; setting startup = 0 indicates to not show the add-in on the DraftSight **Tools > Add-Ins** manager.
- If you do not specify an absolute path in pathname, then a path relative to the add-in application is used.
- The recommended size for bitmap, which appears on the **Tools > Add-Ins** manager, is 16 x 16. The supported image format is .**png** (Portable Network Graphics bitmap image).

[Back to top](#Top)

###### Add-in activation and deactivation

When you build a project created by an add-in template in Microsoft Visual Studio, an add-in is added to the DraftSight **Tools > Add-Ins** manager.

To activate the add-in:

1. Click **Tools > Add-Ins**.
2. Click the row in which the name of the add-in appears.
3. Select the check box in the Active column located next to the name of the add-in you want to activate.
4. Select the check box in the Start Up column located next to the name of the add-in if you want to automatically activate the add-in when DraftSight starts up.
5. Click **OK**.

To deactivate the add-in, clear the check box in the Active column, and in the Start Up column if it's selected, located next to the name of the add-in you want to deactivate.

[Back to top](#Top)

##### COM native C++ and C++ interface data types

The DraftSight API interface data types are:

| COM native C++ | C++ |
| --- | --- |
| BSTR | const dsString&, dsString* [out] |
| DOUBLE | double |
| HRESULT | DSRESULT |
| IDispatch | dsObject |
| interface I Interface (e.g., IApplication) | class ds Interface _c (e.g., dsApplication_c) |
| LONG | long |
| VARIANT | dsObjectPtrArray - or - const dsStringArray&, dsStringArray* [out] - or - const dsDoubleArray&, dsDoubleArray* [out] - or - const dsLongArray&, dsLongArray* |
| VARIANT_BOOL | bool |

###### HRESULT and DSRESULT

In the DraftSight API:

| A call in this language... | Always returns... |
| --- | --- |
| COM native C++ | HRESULT: S_OK = 0x00000000L S_FALSE = 0x00000001L E_NOTIMPL = 0x80004001L RPC_E_DISCONNECTED = 0x80010108L |
| C++ | DSRESULT: DSRESULT_False = 0 DSRESULT_True = 1 DSRESULT_Disconnected = 2 DSRESULT_NotImplemented =3 |

These return values indicate that the code was called successfully; however, these values do not indicate that your call achieved its objective. For example, if a method returns an object, then you should verify that the object returned is not NULL.

[Back to top](#Top)

##### JavaScript

###### Supported JavaScript interface web browsers

The prerequisites for executing the JavaScript examples from the DraftSight API Help are:

- Windows Internet Explorer 8 or later must be installed on your computer.

  If you see the following text in the Output field of a JavaScript example executed from the DraftSight API Help, then Windows Internet Explorer 7 or earlier is most likely installed on your computer and is not supported by the DraftSight JavaScript interface.

  TypeError: 'JSON' is undefined

  If possible, upgrade to either Windows Internet Explorer 8 or later.
- The DraftSight API service must be running. If you see the following text in the Output field of a JavaScript example executed from the DraftSight API Help, then you must start or restart the DraftSight API service from the Task Manager.

  dsJServerError: jsServer connection Failed
- DraftSight API Help must reside on a disk local to your computer.

  If you see the following text in the Output field of a JavaScript example executed from the DraftSight API Help, then most likely the DraftSight API Help resides on network disk.

  TypeError: Access is denied.

  If possible, locate the DraftSight API Help and copy it to a disk local to your computer, and execute it from that disk.

  **NOTE:** It takes several seconds for a Help topic containing a JavaScript application to display in the right-side pane in the Help window.

You can create and execute the JavaScript examples from your web browser. Instructions on how to create any DraftSight JavaScript example appear in the Notes section of the example.

These web browsers are supported by the DraftSight API and JavaScript interface:

- Windows Internet Explorer 8 or later, without network sharing
- Mozilla Firefox, with network sharing

  If your computer is running Mozilla Firefox under Windows 7, then uncomment the following line in your computer's hosts file, typically **C:\Windows\System32\drivers\etc\hosts,** to improve performance on localhost URLs. Edit the hosts file using Notepad as an administrator.

  127.0.0.1 localhost
- Google Chrome

Apple Safari web browser is not recommended because of random http timeouts.

[Back to top](#Top)

###### Editors

You can use Visual Studio, Visual Web Developer, Eclipse, or an HTML editor of your choice to create HTML files for the DraftSight JavaScript interface.

[Back to top](#Top)

###### Debuggers

To debug your JavaScript examples, you can use your web browser's debugger.

| Web browser | Debugger |
| --- | --- |
| Windows Internet Explorer | Windows Internet Explorer Developer Tools |
| Mozilla Firefox | Firebug for Firefox |
| Google Chrome | Google Chrome Developer Tools |

See your web browser's documentation for details about its debugger.

**NOTE:** [Select and Change Entities Example (JavaScript)](Select_and_Change_Entities_Example_JS.htm) includes instructions on using the Windows Internet Explorer Developer Tools.

[Back to top](#Top)

###### Disassociate JavaScript from server-side memory

To disassociate JavaScript from the server-side memory, call:

- **dsObject.release**, which releases the association of the **dsObject**
  - or -
- **dsApplication.releaseAll**, which releases all associated memory initiated from this **dsApplication**

**dsObject.release** or **dsApplication.releaseAll** must be called by the JavaScript client to prevent server-side memory leaks.

[Back to top](#Top)

###### JavaScript syntax in DraftSight API Help

###### Bitwise enumerations

JavaScript bitwise enumerations can include multiple enumerators when delimited by semicolons. For example, you can specify **dsHatchBoundaryLoopType_Polyline;dsHatchBoundaryLoopType_Textbox**.

###### Output arguments

| If... | Then... |
| --- | --- |
| One output argument is returned | One return value is shown |
| Multiple output arguments are returned | A collection is returned and shown |

For example:

###### One output value:

| JavaScript |  |
| --- | --- |
| InsertCircle( CenterX : Number, CenterY : Number, CenterZ : Number, Radius : Number ) : dsCircle |  |

To access the output value, use the name of the variable assigned to it. For example:

var **mCircle** = mSkMgr.InsertCircle(X,Y,Z,2);
var mColor = **mCircle**.get_Color();

###### Multiple output values:

| JavaScript |  |
| --- | --- |
| GetDefaultCustomCoordinateSystemFlag( ) : { IsDefault : Boolean, DefaultCustomCoordinateSystemFlag : String } |  |

To access an output value in a collection, use the name of the variable assigned to the collection followed by a dot (.) and the name of the parameter that appears in the DraftSight API Help. For example:

var dsColl = dsCCS.GetDefaultCustomCoordinateSystemFlag();
printOut("IsDefault? " + **dsColl**.**IsDefault**);
printOut("Default Custom Coordinate system flag: " + **dsColl**.**DefaultCustomCoordinateSystemFlag**)

##### Troubleshooting JavaScript startup

If a JavaScript add-in or HTML page does not execute, then make sure that the DraftSight API service is running.

1. On a computer running Windows, start the Task Manager, click the Services tab, and locate **DraftSight API Service**.
2. If **DraftSight API Service** is not listed in the Name column, then log on as a user with Administrator privileges.
3. Start **DraftSight API Service** using Windows **services.msc**. If you are unfamiliar with running **services.msc**, please search [Microsoft's website](http://www.microsoft.com) for instructions.
  - or -
  Open a command window, change your directory to **c:\Program Files\Dassault Systemes\DraftSight\bin**, and type:

  **dsHttpApiController.exe "DraftSight API Service” -s**

  If **DraftSight API Service** is still not listed in the Name column on the Services tab, then the service might not have started because of a port conflict.
4. To change the port number, log on to [Dassault Systèmes Communities](http://swym.3ds.com) and use the tool available at **[https://swym.3ds.com#post:17786](https://swym.3ds.com#post:17786)**.
5. If the DraftSight API Service is listed and running on the Services tab, but the HTML pages do not execute, then restart the service by right-clicking on the name and clicking **Restart**.

[Back to top](#Top)

##### Code to connect to DraftSight

The following code snippets show how to connect to a running instance of DraftSight in C#, VB.NET, and VBA, and how to connect to JavaScript.

###### C#

```
     static DraftSight.Interop.dsAutomation.Application dsApp = null;

     public static void Main()
     {
         //Connect to DraftSight
         dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
```

###### VB.NET

```
     Dim dsApp as Application
```

```
     Sub Main()
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
```

###### VBA

```vb
Sub Test()
```

```vb
Dim dsApp As DraftSight.Application
Set dsApp = GetObject(, "DraftSight.Application")
```

###### JavaScript

<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/djConnect.js"></script>

<script type="text/javascript" src="http://localhost:7776/APISDK/djLibrary/dsApplication.js"></script>

var mScript = new djScriptManager();
var mApp = mScript.getApplication();

[Back to top](#Top)

##### Access to objects in DraftSight API

To call any of the DraftSight API's methods or properties, you first must obtain the object.

For example, to use the [IDocument::GetPathName](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetPathName.html) method, you must first obtain an [IDocument](Interop.dsAutomation~Interop.dsAutomation.IDocument.html) object. To obtain the IDocument object, you could use [IApplication::GetActiveDocument](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveDocument.html), [IApplication::GetDocuments](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetDocuments.html), or [IApplication::OpenDocument](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenDocument.html). When you have an IDocument object, you can access the properties and methods in the Document class.

During the course of application processing, unknown entities may surface that have no interface representation in the DraftSight API. If you capture unknown entities with the event handlers, [_IDocumentEvents_ObjectAppendNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectAppendNotifyEventHandler.html), [_IDocumentEvents_ObjectEraseNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectEraseNotifyEventHandler.html), or[_IDocumentEvents_ObjectModifyNotify](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_ObjectModifyNotifyEventHandler.html), then you can use [IUnknownEntity](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html) to recognize and process specific ones.

See the Accessors and Access Diagram sections of interface Help topics.

[Back to top](#Top)

##### convertVariantArrayToPtrArray method

The convertVariantArrayToPtrArray method is used in several COM native C++ code snippets in the Help. The convertVariantArrayToPtrArray implementation is as follows:

```
// TypeConverter.h: This class contains a static method to convert a VARIANT array to a PTR array
```

```
#ifndef _TYPE_CONVERTER_H_
#define _TYPE_CONVERTER_H_
```

```
#include "atlsafe.h"
```

```
class TypeConverter
{
public:
        template<class SmartPtrType, class InterfaceType>
        static void convertVariantArrayToPtrArray( variant_t pVariantArraySource, SmartPtrType *&pResult, int &count )
        {
                CComSafeArray<IDispatch*> comSafeArray;
                comSafeArray.Attach( V_ARRAY(&pVariantArraySource) );
```

```
            count = comSafeArray.GetCount();
                pResult = new SmartPtrType[count];
```

```
             for( int i = 0; i < count; ++i )
                {
                        CComPtr<IDispatch> p = comSafeArray[i].p;
```

```
                      if( p.p != NULL )
                        {
                                CComQIPtr<InterfaceType> pVal ( p );
```

```
                           if( pVal.p != NULL )
                                {
                                        pResult[i].Attach ( pVal.Detach ( ) );
                                }
                        }
                }
```

```
            comSafeArray.Detach();
        }
};
```

```
#endif _TYPE_CONVERTER_H_
```

##### Tips and tricks for 3D modeling in DraftSight

In order to use 3D modeling and see your 3D entities in the DraftSight user interface, you need to:

1. Install DraftSight Premium or DraftSight Enterprise Plus.
2. Select **3D Modeling** from the list of workspaces in the **Quick Access Bar** dropdown at the top.
3. Select an isometric view in the **Views** toolbar so you can see your entities in 3D.
4. Select a shaded view in the **Render** toolbar and hide lines that may obscure your viewof entities.
5. Select **Constrained Orbit** in the **Render** toolbar or type **ROLLVIEW** in the command window to rotate the view in 3D space using your mouse.
6. Read these topics in the DraftSight user-interface help:

- **3D Viewing and Presentation**
- **3D Modeling**
- **3D Modeling Command Reference**

[Back to top](#Top)

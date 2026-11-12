---
title: "Using the SOLIDWORKS C# and VB.NET Add-in Templates to Create Add-ins"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SolidWorks_CSharp_and_VB.NET__Project_Templates.htm"
---

# Using the SOLIDWORKS C# and VB.NET Add-in Templates to Create Add-ins

This topic describes how to use the SOLIDWORKS C# Add-in Template or the SOLIDWORKS VB.NET Add-in Template to create an add-in using Microsoft Visual Studio.

After installing the [SOLIDWORKS API SDK](../GettingStarted/SolidWorks_API_Getting_Started_Overview.htm):

- Open Microsoft Visual Studio.
- Click **File > New > Project**.
- In the right panel of the Create a new project dialog, select:

  - C# in the first drop-down. Then scroll the list to find and select [SwCSharpAddin](Using_SolidWorks_C__Add-In_Wizard_to_Create_C__Add-In.htm).

or

- Click **Next**.
- Modify the **Project n****ame**, **Location**, and **Solution name** fields.
- Click **Create**.
- Open Solution Explorer in Visual Studio.
- Double-click **SwAddin.*** to open it.
- Notice that SwAddin uses or imports SolidWorksTools. The SOLIDWORKS API SDK installs **SolidWorksTools.dll** in `install_dir`. The template adds this DLL to the reference list of your add-in project. The DLL must be redistributed with your add-in application. Currently this DLL contains the SOLIDWORKS bitmap handler class, BitmapHandler, which is based on the SOLIDWORKS CommandManager. Use either the Microsoft Visual Studio Object Browser or Intellisense to see its members.

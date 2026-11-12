---
title: "SOLIDWORKS API Getting Started Overview"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/SolidWorks_API_Getting_Started_Overview.htm"
---

# SOLIDWORKS API Getting Started Overview

Prior to developing SOLIDWORKS API applications, you should be familiar with using the SOLIDWORKS Design software interactively and programming in the languages that you intend to use. If you are not, then you should:

- Attend [SOLIDWORKS Design training courses offered at SOLIDWORKS Authorized Training and Support Centers](http://www.solidworks.com/pages/services/Training/training.html).
- Take courses in the [programming languages](SolidWorks_API_Standalone_and_Add-in_Applications_Overview.htm) that you intend to use.

The SOLIDWORKS API SDK contains templates that help you develop SOLIDWORKS add-ins.

#### To install the SOLIDWORKS API SDK:

1. Ensure that Microsoft Visual Studio is installed.
2. For SOLIDWORKS Design installations, copy **\apisdk\SolidWorks API SDK.msi** from the installation media to a local directory. For SOLIDWORKS Design connected to the 3DEXPERIENCE platform installations, copy **\win_b64\resources\MSI\SOLIDWORKS API SDK.msi** from the installation media to a local directory.
3. Double-click **apisdk.exe** or **SolidWorks API SDK.msi** to run the API SDK InstallShield Wizard. (If you have multiple Visual Studio versions, you may need to manually copy the template zip files to the template folders of each VS version. Locate and copy the zip files to **c:\Users\**`user`**\Documents\Visual Studio 20xx\Templates\ProjectTemplates\Visual Basic** and **Visual C#**.)
4. Restart Visual Studio. SwVBAddin, SwCSharpAddin, and SOLIDWORKS COM Non-Attributed Add-in Wizard templates should be available in the Create a new project dialog. See the [Using the SOLIDWORKS C# and VB.NET Add-in Templates to Create Add-ins](../Overview/SolidWorks_CSharp_and_VB.NET__Project_Templates.htm) and the [Using the SOLIDWORKS COM Non-Attributed Add-in Wizard to Create a C++/CLI Add-in](../Overview/Using_SolidWorks_CPlusPlus_NET_Add-In_Wizard_to_Create.htm) topics.

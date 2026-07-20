---
title: "SOLIDWORKS API Getting Started Overview"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/SolidWorks_API_Getting_Started_Overview.htm"
---

# SOLIDWORKS API Getting Started Overview

Prior to developing SOLIDWORKS API applications, you should be familiar
with using the SOLIDWORKS software interactively and programming in the
languages that you intend to use. If you are not, then you should:

- Attend[SOLIDWORKS
  training courses offered at SOLIDWORKS Authorized Training and Support
  Centers](http://www.solidworks.com/pages/services/Training/training.html).
- Take courses in the[programming
  languages](SolidWorks_API_Standalone_and_Add-in_Applications_Overview.htm)that you intend to use.

The SOLIDWORKS API SDK contains templates that help you develop SOLIDWORKS
add-ins.

#### To install the SOLIDWORKS API SDK:

1. Ensure that Microsoft Visual Studio is installed in**c:\Program Files**.
2. Copy**\apisdk\SolidWorks API SDK.msi**from
  the installation media to a local directory. For SOLIDWORKS Connected
  installations, copy**\win_b64\resources\MSI\SOLIDWORKS API SDK.msi**from the installation media to a local directory.

  - Or -

  Modify your SOLIDWORKS installation from**Settings > Apps**.
  In the installation dialog under Product Selection, check**API Tools**and**SOLIDWORKS API SDK (install manually)**.**apisdk/SOLIDWORKS API SDK.msi**will be installed in your
  installation folder.
3. Double-click**apisdk.exe**or**SolidWorks API SDK.msi**to run
  the API SDK InstallShield Wizard. If you have multiple Visual Studio
  versions, you may need to manually install the templates into the proper
  template folders. Locate and copy the zip files into the**c:\Users\Documents\Visual Studio 20xx\Templates\ProjectTemplates\VisualBasic
  or Visual C#**. Restart Visual Studio. SwVBAddin and SwCSharpAddin
  are available project templates. See the API Programming Guide for more
  details.

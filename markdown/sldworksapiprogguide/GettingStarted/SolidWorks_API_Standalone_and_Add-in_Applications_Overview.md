---
title: "SOLIDWORKS API Standalone and Add-in Applications Overview"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/SolidWorks_API_Standalone_and_Add-in_Applications_Overview.htm"
---

# SOLIDWORKS API Standalone and Add-in Applications Overview

You can use any programming language that supports COM to create SOLIDWORKS standalone API (.exe files) and add-in (.dll files) applications. The programming languages most commonly used are:

- [Visual Basic .NET (VB.NET)](Visual_Basic_.NET_Standalone_and_Add-in_Applications.htm)
- [Visual C++/CLI](CPP_.NET_Standalone_and_Add-in_Applications.htm)
- [Visual C# .NET](Visual_C__Standalone_and_Add-in_Applications.htm)
- [Visual C++ 6.0](Visual_CPP_6_Standalone_and_Add-in_Applications.htm)

Please note that when programmatically creating a new SOLIDWORKS session, add-ins do not load even though **Start Up** is selected in the SOLIDWORKS Add-in dialog. You have to call [ISldWorks::LoadAddIn](sldworksapi.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks~LoadAddIn.html) to load your add-ins.

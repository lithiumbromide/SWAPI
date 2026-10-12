---
title: "Add Derived Configurations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Derived_Configurations_Example_VBNET.htm"
---

# Add Derived Configurations Example (VB.NET)

This example shows how to add a derived configuration for each existing configuration.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Open a part or assembly.
 '
 ' Postconditions: For each configuration, adds and selects a derived
 ' configuration.
 '
 ' NOTE: IConfigurationManager::AddConfiguration returns
 ' Nothing or null if the new configuration already exists.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim vConfigNameArr As Object
         Dim vConfigName As Object
         Dim swConf As Configuration
         Dim swConfMgr As ConfigurationManager
         Dim swDerivConf As Configuration
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swConfMgr = swModel.ConfigurationManager
         swConf = swConfMgr.ActiveConfiguration

         vConfigNameArr = swModel.GetConfigurationNames

         For Each vConfigName In vConfigNameArr
             swConf = swModel.GetConfigurationByName(vConfigName)

             ' Nothing or null if (derived) configuration already exists
             swDerivConf = swConfMgr.AddConfiguration(swConf.Name + " Derived", "Derived comment", "Derived alternate name", 1, swConf.Name, "Derived description")
             bRet = swDerivConf.Select2(True, Nothing)
         Next

     End Sub

     Public swApp As SldWorks

 End  Class
```

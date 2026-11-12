---
title: "Add Derived Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Derived_Configurations_Example_VB.htm"
---

# Add Derived Configurations Example (VBA)

This example shows how to add a derived configuration for each existing configuration.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Open a part or assembly.
 '
 ' Postconditions: For each configuration, adds and selects
 ' a derived configuration.
 '
 ' NOTE: IConfigurationManager::AddConfiguration returns
 ' Nothing or null if the new configuration already exists.
 '---------------------------------------------------------------------------
 Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim vConfigNameArr              As Variant
     Dim vConfigName                 As Variant
     Dim swConf                      As SldWorks.Configuration
     Dim swConfMgr                   As SldWorks.ConfigurationManager
     Dim swDerivConf                 As SldWorks.Configuration
     Dim bRet                        As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swConfMgr = swModel.ConfigurationManager
     Set swConf = swConfMgr.ActiveConfiguration
    vConfigNameArr = swModel.GetConfigurationNames
    For Each vConfigName In vConfigNameArr
         Set swConf = swModel.GetConfigurationByName(vConfigName)
        ' Nothing or null if (derived) configuration already exists
         Set swDerivConf = swConfMgr.AddConfiguration(swConf.Name + " Derived", "Derived comment", "Derived alternate name", 1, swConf.Name, "Derived description")
         bRet = swDerivConf.Select2(True, Nothing)
     Next

End Sub
```

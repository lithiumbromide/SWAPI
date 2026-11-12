---
title: "Get and Set Large Design Review Marks for Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Large_Design_Review_Marks_for_Configurations_Example_VB.htm"
---

# Get and Set Large Design Review Marks for Configurations Example (VBA)

This example shows how to get and set the Large Design Review marks for all of the configurations in an assembly.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the current Large Design Review marks for all configurations.
' 2. Sets the Large Design Review marks for all configurations to true.
' 3. Gets the modified Large Design Review marks for all configurations.
' 4. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swConf As SldWorks.Configuration
    Dim swConfMgr As SldWorks.ConfigurationManager
    Dim configNameArr As Variant
    Dim configName As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfMgr = swModel.ConfigurationManager
    configNameArr = swModel.GetConfigurationNames
```

```
    'Get current Large Design Review marks for all configurations
    Debug.Print "Current Large Design Review marks for configurations:"
    For Each configName In configNameArr
        Set swConf = swModel.GetConfigurationByName(configName)
        Debug.Print "  " & configName & ": " & swConf.LargeDesignReviewMark
    Next
```

```
    'Set Large Design Review marks for all configurations to true
    For Each configName In configNameArr
        Set swConf = swModel.GetConfigurationByName(configName)
        swConf.LargeDesignReviewMark = True
    Next
```

```
    'Get modified Large Design Review marks for all configurations
    Debug.Print "Modified Large Design Review marks for configurations:"
    For Each configName In configNameArr
        Set swConf = swModel.GetConfigurationByName(configName)
        Debug.Print "  " & configName & ": " & swConf.LargeDesignReviewMark
    Next
```

```
End Sub
```

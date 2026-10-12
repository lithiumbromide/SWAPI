---
title: "Get Dimension Values in All Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_Values_in_All_Configurations_Example_VB.htm"
---

# Get Dimension Values in All Configurations Example (VBA)

This example shows how to get the dimension values in all configurations of a model.

```
'----------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\multiconfig-part-2.sldprt.
' 2. Right-click Annotations and click Show Feature Dimensions.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConfig As SldWorks.Configuration
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDispDim As SldWorks.DisplayDimension
    Dim swDim As SldWorks.Dimension
    Dim vConfigNameArr As Variant
    Dim vConfigName As Variant
    Dim vDimValArr As Variant
    Dim vDimVal As Variant
    Dim sSpecConfigNameArr(0) As String
    Dim vSpecConfigNameArr As Variant
    Dim dimValue As Variant
    Dim status As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swSelMgr = swModel.SelectionManager
    status = swModel.Extension.SelectByID2("D1@Extrude1@multiconfig-part-2.SLDPRT", "DIMENSION", 2.16557439463763E-02, -1.85256458254496E-02, 1.15860942898448E-03, False, 0, Nothing, 0)
    Set swDispDim = swSelMgr.GetSelectedObject6(1, -1)
    Set swDim = swDispDim.GetDimension
    vConfigNameArr = swModel.GetConfigurationNames
```

```
    Debug.Print "File = " & swModel.GetPathName & "<" & swConfig.Name & ">"
    Debug.Print "  " & swDim.FullName & " [" & swDim.Name & "]"
    dimValue = swDim.GetSystemValue3(swThisConfiguration, vConfigNameArr(0))
    Debug.Print "    System value = " & dimValue(0)
    Debug.Print "    Is applied to all configurations? " & swDim.IsAppliedToAllConfigurations
    Debug.Print "    Driven state = " & swDim.DrivenState
    Debug.Print "    Is reference? " & swDim.IsReference
    Debug.Print "    Read only? " & swDim.ReadOnly
```

```
    Debug.Print "    Configuration names"
    For Each vConfigName In vConfigNameArr
        sSpecConfigNameArr(0) = vConfigName
        vSpecConfigNameArr = sSpecConfigNameArr
        vDimValArr = swDim.GetValue3(swSpecifyConfiguration, vSpecConfigNameArr): Debug.Assert 0 = UBound(vDimValArr)
        For Each vDimVal In vDimValArr
            Debug.Print "      " & vConfigName & " = " & vDimVal & " mm"
        Next vDimVal
    Next vConfigName
```

```
End Sub
```

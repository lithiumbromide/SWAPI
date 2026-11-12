---
title: "Get Dimension Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_Values_Example_VB.htm"
---

# Get Dimension Values Example (VBA)

This example shows how to get the dimension values in all configurations of a model.

```vb
'----------------------------------------
'
' Preconditions:
'                (1) Model document with dimensions is open.
'                (2) Dimension is selected.
'
' Postconditions: None
'
'-----------------------------------------
Option Explicit
Public Enum swDimensionDrivenState_e
    swDimensionDrivenUnknown = 0    '  the driven/driving state is unknown
    swDimensionDriven = 1           '  the dimension is a driven dimension
    swDimensionDriving = 2          '  the dimension is a driving dimension
End Enum
Public Enum swInConfigurationOpts_e
    swConfigPropertySuppressFeatures = 0
    swThisConfiguration = 1
    swAllConfiguration = 2
    swSpecifyConfiguration = 3
End Enum
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swConfigMgr                 As SldWorks.ConfigurationManager
    Dim swConfig                    As SldWorks.Configuration
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swDispDim                   As SldWorks.DisplayDimension
    Dim swDim                       As SldWorks.Dimension
    Dim vConfigNameArr              As Variant
    Dim vConfigName                 As Variant
    Dim vDimValArr                  As Variant
    Dim vDimVal                     As Variant
    Dim sSpecConfigNameArr(0)       As String
    Dim vSpecConfigNameArr          As Variant
    Dim dimValue                    As Variant
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    Set swSelMgr = swModel.SelectionManager
    Set swDispDim = swSelMgr.GetSelectedObject5(1)
    Set swDim = swDispDim.GetDimension
    vConfigNameArr = swModel.GetConfigurationNames

    Debug.Print "File = " & swModel.GetPathName & "<" & swConfig.Name & ">"
    Debug.Print "  " & swDim.FullName & " [" & swDim.Name & "]"
    dimValue = swDim.GetSystemValue3(swThisConfiguration, vConfigNameArr(0))
    Debug.Print "    SystemValue                      = " & dimValue(0)
    Debug.Print "    IsAppliedToAllConfigurations     = " & swDim.IsAppliedToAllConfigurations
    Debug.Print "    DrivenState                      = " & swDim.DrivenState
    Debug.Print "    IsReference                      = " & swDim.IsReference
    Debug.Print "    ReadOnly                         = " & swDim.ReadOnly

    For Each vConfigName In vConfigNameArr
        sSpecConfigNameArr(0) = vConfigName
        vSpecConfigNameArr = sSpecConfigNameArr
        vDimValArr = swDim.GetValue3(swSpecifyConfiguration, vSpecConfigNameArr): Debug.Assert 0 = UBound(vDimValArr)
        For Each vDimVal In vDimValArr
            Debug.Print "      " & vConfigName & " --> " & vDimVal
        Next vDimVal
    Next vConfigName
End Sub
'----------------------------------------
```

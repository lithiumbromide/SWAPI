---
title: "Get Custom Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_Example_VB.htm"
---

# Get Custom Properties Example (VBA)

This example shows how to get the custom properties for the configurations in a document.

```vb
'---------------------------------------------
Option Explicit

Public Enum swCustomInfoType_e
    swCustomInfoUnknown = 0
    swCustomInfoText = 30       '  VT_LPSTR
    swCustomInfoDate = 64       '  VT_FILETIME
    swCustomInfoNumber = 3      '  VT_I4
    swCustomInfoYesOrNo = 11    '  VT_BOOL
End Enum

Sub main()

    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swConfig                As SldWorks.Configuration
    Dim vConfName               As Variant
    Dim vPropName               As Variant
    Dim vPropValue              As Variant
    Dim vPropType               As Variant
    Dim nNumProp                As Long
    Dim i                       As Long
    Dim j                       As Long
    Dim bRet                    As Boolean
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc

    Debug.Print "File = " + swModel.GetPathName

    vConfName = swModel.GetConfigurationNames
    For i = 0 To UBound(vConfName)
        Set swConfig = swModel.GetConfigurationByName(vConfName(i))

        nNumProp = swConfig.GetCustomProperties(vPropName, vPropValue, vPropType)

        Debug.Print "  Config       = " & vConfName(i)
        For j = 0 To nNumProp - 1
            Debug.Print "    " & vPropName(j) & " <" & vPropType(j) & "> = " & vPropValue(j)
        Next j
        Debug.Print "  ---------------------------"
    Next i
End Sub
```

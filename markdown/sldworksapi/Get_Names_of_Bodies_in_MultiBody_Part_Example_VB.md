---
title: "Get Names of Bodies in Multibody Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm"
---

# Get Names of Bodies in Multibody Part Example (VBA)

This example shows how to get the names of the bodies in each multibody part in an assembly.

```
'-------------------------------------------------
' Preconditions:
' 1. Verify that the specified files exist:
'    * assembly document template
'    * both multibody part documents
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens both multibody parts.
' 2. Opens a new assembly document.
' 3. Adds the open multibody parts as components
'    to the assembly.
' 4. Traverses the components in the assembly and gets
'    and prints the names of the bodies in each
'    component.
' 5. Examine the Immediate window.
'
' NOTE: Because the multibody parts are used
' elsewhere, do not save changes.
'--------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim swComponent1 As SldWorks.Component2
Dim swComponent2 As SldWorks.Component2
Dim swPart As SldWorks.PartDoc
Dim multibodyPart1 As String
Dim multibodyPart2 As String
Dim errors As Long
Dim warnings As Long
Dim vBody As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open the multibody parts, new assembly document, and add
    'the multibody parts as components to the assembly
    multibodyPart1 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_bridge.sldprt"
    multibodyPart2 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
    Set swModel = swApp.OpenDoc6(multibodyPart1, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModel = swApp.OpenDoc6(multibodyPart2, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2014\templates\assembly.asmdot", swDwgPaperSizes_e.swDwgPaperA0size, 0, 0)
    Set swAssembly = swModel
    Set swComponent1 = swAssembly.AddComponent5(multibodyPart1, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -1.11307660915827E-04, 5.87355354468855E-05, -1)
    Set swComponent2 = swAssembly.AddComponent5(multibodyPart2, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -0.218915538687725, 0.115372315514833, 4.34772581793368E-02)
    swModel.ViewZoomtofit2
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    'Process assembly
    Select Case swModel.GetType
        Case swDocPART
            Set swPart = swModel
            'Solid bodies
            vBody = swPart.GetBodies2(swSolidBody, True)
            SelectBodies swApp, swModel, vBody, ""
            'Surface bodies
            vBody = swPart.GetBodies2(swSheetBody, True)
            SelectBodies swApp, swModel, vBody, ""
            'Assembly
        Case swDocASSEMBLY
            ProcessAssembly swApp, swModel
        Case Else
            Exit Sub
    End Select
```

```
End Sub
```

```
Sub SelectBodies(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vBody As Variant, sPadStr As String)
```

```
    Dim swModExt As SldWorks.ModelDocExtension
    Dim swBody As SldWorks.Body2
    Dim sBodySelStr  As String
    Dim sBodyTypeSelStr As String
    Dim i As Long
    Dim status As Boolean
```

```
    If IsEmpty(vBody) Then Exit Sub
    Set swModExt = swModel.Extension
```

```
    For i = 0 To UBound(vBody)
        Set swBody = vBody(i)
        sBodySelStr = swBody.GetSelectionId
        Debug.Print "  " & sPadStr & sBodySelStr
        Select Case swBody.GetType
            Case swSolidBody
                sBodyTypeSelStr = "SOLIDBODY"
            Case swSheetBody
                sBodyTypeSelStr = "SURFACEBODY"
            Case Else
                Debug.Assert False
        End Select
        status = swModExt.SelectByID2(sBodySelStr, sBodyTypeSelStr, 0#, 0#, 0#, True, 0, Nothing, swSelectOptionDefault)
    Next i
```

```
End Sub
```

```
Sub ProcessAssembly(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2)
```

```
    Dim swConfigMgr As SldWorks.ConfigurationManager
    Dim swConf As SldWorks.Configuration
    Dim swRootComp As SldWorks.Component2
```

```
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConf = swConfigMgr.ActiveConfiguration
    Set swRootComp = swConf.GetRootComponent
    ProcessComponent swApp, swModel, swRootComp, 1
```

```
End Sub
```

```
Sub ProcessComponent(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swComp As SldWorks.Component2, nLevel As Long)
```

```
    Dim vChildComp As Variant
    Dim swChildComp As SldWorks.Component2
    Dim sPadStr As String
    Dim vBody As Variant
    Dim i  As Long
```

```
    For i = 0 To nLevel - 1
        sPadStr = sPadStr + "  "
    Next i
```

```
    Debug.Print sPadStr & swComp.Name2 & " <" & swComp.ReferencedConfiguration & ">"
```

```
    'Solid bodies
    vBody = swComp.GetBodies2(swSolidBody)
    SelectBodies swApp, swModel, vBody, sPadStr
```

```
    'Surface bodies
    vBody = swComp.GetBodies2(swSheetBody)
    SelectBodies swApp, swModel, vBody, sPadStr
```

```
    'Components
    vChildComp = swComp.GetChildren
    For i = 0 To UBound(vChildComp)
        Set swChildComp = vChildComp(i)
        ProcessComponent swApp, swModel, swChildComp, nLevel + 1
    Next i
```

```
End Sub
```

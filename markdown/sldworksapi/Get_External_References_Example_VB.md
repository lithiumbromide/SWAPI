---
title: "Get External References (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_External_References_Example_VB.htm"
---

# Get External References (VBA)

This example shows how to get a list of the external references for a selected component, selected feature, or document.

```
'-------------------------------------------
'  Preconditions:
'  1. Open an assembly or part document.
'  2. Select:
'     * a component in an assembly document.
'       - or -
'     * a feature in an assembly or part document.
'       - or -
'     * Nothing in either type of document.
'
' Postconditions: Examine the Immediate window
' to see the name of the part or assembly document
' and the external references for the
' selected component, selected feature, or
' document.
'-------------------------------------------
```

```
Option Explicit
```

```
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swModDocExt             As SldWorks.ModelDocExtension
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swFeat                  As SldWorks.Feature
    Dim swComp                  As SldWorks.Component2
    Dim vModelPathName          As Variant
    Dim vComponentPathName      As Variant
    Dim vFeature                As Variant
    Dim vDataType               As Variant
    Dim vStatus                 As Variant
    Dim vRefEntity              As Variant
    Dim vFeatComp               As Variant
    Dim nConfigOpt              As Long
    Dim sConfigName             As String
    Dim vConfigOpt              As Variant
    Dim vConfigName             As Variant
    Dim nRefCount               As Long
    Dim nSelType                As Long
    Dim i                       As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    Set swModDocExt = swModel.Extension
    nSelType = swSelMgr.GetSelectedObjectType3(1, -1)
```

```
    Select Case nSelType
```

```
        ' Selected component in an assembly document
        Case swSelCOMPONENTS
            Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, -1)
            nRefCount = swComp.ListExternalFileReferencesCount
            swComp.ListExternalFileReferences2 vModelPathName, vComponentPathName, vFeature, vDataType, vStatus, vRefEntity, vFeatComp, nConfigOpt, sConfigName
            Set swModel = swComp.GetModelDoc2
```

```
     Debug.Print "Model name = " + swModel.GetPathName
    Debug.Print "    Reference count        = " + Str(nRefCount)
    Debug.Print ""
    For i = 0 To nRefCount - 1
        Debug.Print "    Model path + name      = " + vModelPathName(i)
        Debug.Print "    Component path + name  = " + vComponentPathName(i)
        Debug.Print "    Feature                = " + vFeature(i)
        Debug.Print "    Data type              = " + vDataType(i)
        Debug.Print "    Status                 = " + Str(vStatus(i))
        Debug.Print "    Reference entity       = " + vRefEntity(i)
        Debug.Print "    Feature component      = " + vFeatComp(i)
```

```
     Next i
        Debug.Print "    Configuration option   = " & nConfigOpt
        Debug.Print "    Configuration name     = " & sConfigName
        Debug.Print " "
```

```
        ' Selected feature in a part or assembly document
        Case swSelBODYFEATURES, swSelSKETCHES
            Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
            nRefCount = swFeat.ListExternalFileReferencesCount
            swFeat.ListExternalFileReferences2 vModelPathName, vComponentPathName, vFeature, vDataType, vStatus, vRefEntity, vFeatComp, nConfigOpt, sConfigName
```

```
     Debug.Print "    Reference count        = " + Str(nRefCount)
    Debug.Print ""
    For i = 0 To nRefCount - 1
        Debug.Print "    Model path + name      = " + vModelPathName(i)
        Debug.Print "    Component path + name  = " + vComponentPathName(i)
        Debug.Print "    Feature                = " + vFeature(i)
        Debug.Print "    Data type              = " + vDataType(i)
        Debug.Print "    Status                 = " + Str(vStatus(i))
        Debug.Print "    Reference entity       = " + vRefEntity(i)
        Debug.Print "    Feature component      = " + vFeatComp(i)
```

```
     Next i
        Debug.Print "    Configuration option   = " & nConfigOpt
        Debug.Print "    Configuration name     = " & sConfigName
        Debug.Print " "

        ' Part or assembly
        Case Else
            nRefCount = swModDocExt.ListExternalFileReferencesCount
            swModDocExt.ListExternalFileReferences2 vModelPathName, vComponentPathName, vFeature, vDataType, vStatus, vRefEntity, vFeatComp, vConfigOpt, vConfigName
```

```
     Debug.Print "Model name = " + swModel.GetPathName
    Debug.Print "    Reference count        = " + Str(nRefCount)
    Debug.Print ""
    For i = 0 To nRefCount - 1
        Debug.Print "    Model path + name      = " + vModelPathName(i)
        Debug.Print "    Component path + name  = " + vComponentPathName(i)
        Debug.Print "    Feature                = " + vFeature(i)
        Debug.Print "    Data type              = " + vDataType(i)
        Debug.Print "    Status                 = " + Str(vStatus(i))
        Debug.Print "    Reference entity       = " + vRefEntity(i)
        Debug.Print "    Feature component      = " + vFeatComp(i)
        Debug.Print "    Configuration option   = " & vConfigOpt(i)
        Debug.Print "    Configuration name     = " & vConfigName(i)
        Debug.Print " "
    Next i
```

```
End Select
```

```
End Sub
```

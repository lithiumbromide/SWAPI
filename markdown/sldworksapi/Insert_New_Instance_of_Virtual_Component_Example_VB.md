---
title: "Insert New Instance of Virtual Component (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Instance_of_Virtual_Component_Example_VB.htm"
---

# Insert New Instance of Virtual Component (VBA)

This example shows how to:

- create an assembly document.
- insert a new part as a virtual component in the assembly document.
- insert a new instance of the virtual component in the assembly document.

```
'-----------------------------------------------------
' Preconditions: None
'
' Postconditions:
' 1. An assembly document is created.
' 2. A virtual component is inserted in the assembly document.
' 3. A new instance of the virtual component is inserted
'    in the assembly document.
' 4. Examine the FeatureManager design tree to
'    verify steps 2 and 3.
' 5. Close the assembly document without saving the modified
'    documents.
'-----------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Set swApp = Application.SldWorks
```

```
    Dim asmTemplate As String
    asmTemplate = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplateAssembly)
```

```
    Dim swModel As SldWorks.ModelDoc2
    Set swModel = swApp.NewDocument(asmTemplate, 0, 0, 0)
```

```
    Dim swSelMgr As SldWorks.SelectionMgr
    Set swSelMgr = swModel.SelectionManager
```

```
    If swModel.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0) = False Then
        Debug.Print "Failed to select Front plane; check feature name."
        Exit Sub
    End If
```

```
    Dim swPlaneFeature As SldWorks.Feature
    Set swPlaneFeature = swSelMgr.GetSelectedObject6(1, -1)
    Dim swPlane As SldWorks.refPlane
    Set swPlane = swPlaneFeature.GetSpecificFeature2
```

```
    Dim swAssem As SldWorks.AssemblyDoc
    Set swAssem = swModel
```

```
    Dim lResult As Long
    Dim swVirtComp As SldWorks.Component2
    lResult = swAssem.InsertNewVirtualPart(swPlane, swVirtComp)
```

```
    If lResult = swInsertNewPartError_NoError Then
        Dim swSecondComp As SldWorks.Component2
        Set swSecondComp = swAssem.AddComponent5(swVirtComp.GetPathName, swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", 0.1, 0, 0)
    End If
```

```
End Sub
```

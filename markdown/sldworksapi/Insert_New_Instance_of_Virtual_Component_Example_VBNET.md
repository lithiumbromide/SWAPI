---
title: "Insert New Instance of Virtual Component (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Instance_of_Virtual_Component_Example_VBNET.htm"
---

# Insert New Instance of Virtual Component (VB.NET)

This example shows how to:

- create an assembly document.
- insert a new part as a virtual component in the assembly document.
- insert a new instance of the virtual component in the assembly document.

```vb
 '-----------------------------------------------------
 ' Preconditions: None
 '
 ' Postconditions:
 ' 1. An assembly document is created.
 ' 2. A virtual part is inserted in the assembly document.
 ' 3. A new instance of the virtual part is inserted
 '    in the assembly document.
 ' 4. Examine the FeatureManager design tree to
 '    verify steps 2 and 3.
 ' 5. Close the assembly document without saving the modified
 '    documents.
 '-----------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim asmTemplate As String
         asmTemplate = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplateAssembly)

         Dim swModel As ModelDoc2
         swModel = swApp.NewDocument(asmTemplate, 0, 0, 0)

         Dim swSelMgr As SelectionMgr
         swSelMgr = swModel.SelectionManager

         If swModel.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  False, 0,  Nothing, 0) = False Then
             Debug.Print("Failed to select Front plane; check feature name.")
             Exit Sub
         End If

         Dim swPlaneFeature As Feature
         swPlaneFeature = swSelMgr.GetSelectedObject6(1, -1)
         Dim swPlane As RefPlane
         swPlane = swPlaneFeature.GetSpecificFeature2

         Dim swAssem As AssemblyDoc
         swAssem = swModel

         Dim lResult As Integer
         Dim swVirtComp As Component2
         swVirtComp = Nothing
         lResult = swAssem.InsertNewVirtualPart(swPlane, swVirtComp)

         If lResult = swInsertNewPartErrorCode_e.swInsertNewPartError_NoError  Then
             Dim swSecondComp As Component2
             swSecondComp = swAssem.AddComponent5(swVirtComp.GetPathName, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", 0.1, 0, 0)
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```

---
title: "Add and Mate Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Component_and_Mate_Example_VB.htm"
---

# Add and Mate Component Example (VBA)

This example shows how to add a component to an assembly and mate it.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Copy and paste this code in the main module.
 ' 2. Click Insert > Class module and copy and paste this code in the class
 '    module.
 ' 3. Verify that these documents exist in public_documents\samples\tutorial\toolbox:
 '    * lens_mount.sldasm
 '    * camtest.sldprt
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens lens_mount.sldasm.
 ' 2. Adds the specified component, camtest.sldprt, to the assembly.
 ' 3. Fires the AddItemNotify event.
 ' 4. Makes the specified component virtual by saving it to the
 '    assembly with a new name.
 ' 5. Fires the RenameItemNotify event.
 ' 6. Adds a mate between the selected planes to the assembly.
 ' 7. Inspect the Immediate window and FeatureManager design tree.
 '
 ' NOTE: Because the models are used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
'Main module
Option Explicit
Dim swApp As New SldWorks.SldWorks
 Dim swModel As ModelDoc2
 Dim swDocExt As ModelDocExtension
 Dim swAssy As AssemblyDoc
 Dim swAssyEvents As Class1
 Dim tmpPath As String
 Dim tmpObj As SldWorks.ModelDoc2
 Dim boolstat As Boolean, stat As Boolean
 Dim strings As Variant
 Dim swcomponent As SldWorks.Component2
 Dim matefeature As SldWorks.Feature
 Dim MateName As String
 Dim FirstSelection As String
 Dim SecondSelection As String
 Dim strCompName As String
 Dim AssemblyTitle As String
 Dim AssemblyName As String
 Dim errors As Long
 Dim warnings As Long
 Dim mateError As Long
 Dim fileName As String

Sub main()
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\lens_mount.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

    ' Get title of assembly document
    AssemblyTitle = swModel.GetTitle
```

```vb
    ' Split the title into two strings using the period as the delimiter
     strings = Split(AssemblyTitle, ".")
    ' Use AssemblyName when mating the component with the assembly
     AssemblyName = strings(0)
    Debug.Print "Name of assembly: " & AssemblyName
    boolstat = True
     Dim strCompModelname As String
     strCompModelname = "camtest.sldprt"

    ' Because the component resides in the same folder as the assembly, get
     ' the assembly's path and use it when opening the component
     tmpPath = Left(swModel.GetPathName, InStrRev(swModel.GetPathName, "\"))

    ' Open the component
     Set tmpObj = swApp.OpenDoc6(tmpPath + strCompModelname, swDocPART, 0, "", errors, warnings)

    ' Check to see if the file is read-only or cannot be found; display error messages
     If warnings = swFileLoadWarning_ReadOnly Then
         MsgBox "This file is read-only."
         boolstat = False
     End If

    If tmpObj Is Nothing Then
         MsgBox "Cannot locate the file."
         boolstat = False
     End If

    ' Activate the assembly so that you can add the component to it
     Set swModel = swApp.ActivateDoc3(AssemblyTitle, True, swUserDecision, errors)

    ' Set up events
     Set swAssy = swModel
     Set swAssyEvents = New Class1
     Set swAssyEvents.swAssy = swApp.ActiveDoc

    ' Add the part to the assembly document
     Set swcomponent = swAssy.AddComponent5(strCompModelname, swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -1, -1, -1)

    ' Make the component virtual
     stat = swcomponent.MakeVirtual2(True)

    ' Get the name of the component for the mate
     strCompName = swcomponent.Name2()

    ' Create the name of the mate and the names of the planes to use for the mate
     MateName = "top_coinc_" + strCompName
     FirstSelection = "Top@" + strCompName & "@" + AssemblyName
     SecondSelection = "Front@" + AssemblyName

    swModel.ClearSelection2 (True)
     Set swDocExt = swModel.Extension

    ' Select the planes to mate
     boolstat = swDocExt.SelectByID2(FirstSelection, "PLANE", 0, 0, 0, True, 1, Nothing, swSelectOptionDefault)
     boolstat = swDocExt.SelectByID2(SecondSelection, "PLANE", 0, 0, 0, True, 1, Nothing, swSelectOptionDefault)

    ' Add the mate
     Set matefeature = swAssy.AddMate5(swMateCOINCIDENT, swMateAlignALIGNED, False, 0, 0, 0, 0, 0, 0, 0, 0, False, False, 0, mateError)
     matefeature.Name = MateName
     Debug.Print "Mate added: " & matefeature.Name

    swModel.ViewZoomtofit2
End Sub
Back to top
```

###### 'Class module

```vb
Option Explicit
Public WithEvents swAssy As SldWorks.AssemblyDoc

Private Function swAssy_AddItemNotify(ByVal EntityType As Long, ByVal itemName As String) As Long
     Debug.Print "Component added: " & itemName
 End Function
Private Function swAssy_RenameItemNotify(ByVal EntityType As Long, ByVal oldName As String, ByVal NewName As String) As Long
     Debug.Print "Virtual component name: " & NewName
 End Function

Back to top
```

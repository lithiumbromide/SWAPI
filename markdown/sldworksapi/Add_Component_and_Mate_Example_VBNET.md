---
title: "Add and Mate Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Component_and_Mate_Example_VBNET.htm"
---

# Add and Mate Component Example (VB.NET)

This example shows how to add a component to an assembly and mate it.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that these documents exist in public_documents\samples\tutorial\toolbox:
 '    * lens_mount.sldasm
 '    * camtest.sldprt
 ' 2. Open the Immediate window.
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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics
 Imports System.Collections

 Partial Class SolidWorksMacro

     Public WithEvents swAssemblyDoc As AssemblyDoc

     Dim swModel As ModelDoc2
     Dim swDocExt As ModelDocExtension
     Dim openAssem As Hashtable
     Dim tmpPath As String
     Dim tmpObj As ModelDoc2
     Dim boolstat As Boolean, stat As Boolean
     Dim strings As Object
     Dim swComponent As Component2
     Dim matefeature As Feature
     Dim MateName As String
     Dim FirstSelection As String
     Dim SecondSelection As String
     Dim strCompName As String
     Dim AssemblyTitle As String
     Dim AssemblyName As String
     Dim errors As Integer
     Dim warnings As Integer
     Dim mateError As Integer
     Dim fileName as String

     Sub Main()
```

' Open assembly
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\lens_mount.sldasm"
swModel = swApp.**OpenDoc6**(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

' Set up event
swAssemblyDoc = swModel
openAssem = New Hashtable
AttachEventHandlers()

' Get title of assembly document
AssemblyTitle = swModel.**GetTitle**()

' Split the title into two strings using the period as the delimiter
strings = Split(AssemblyTitle, ".")

' Use AssemblyName when mating the component with the assembly
AssemblyName = strings(0)

Debug.Print("Name of assembly: " & AssemblyName)

boolstat = True
Dim strCompModelname As String
strCompModelname = "camtest.sldprt"

' Because the component resides in the same folder as the assembly, get
' the assembly's path and use it when opening the component
tmpPath = Left(swModel.**GetPathName**, InStrRev(swModel.**GetPathName**, "\"))

' Open the component
tmpObj = swApp.**OpenDoc6**(tmpPath + strCompModelname, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

' Check to see if the file is read-only or cannot be found; display error
' messages if either
If warnings = swFileLoadWarning_e.swFileLoadWarning_ReadOnly Then
MsgBox("This file is read-only.")
boolstat = False
End If

If tmpObj Is Nothing Then
MsgBox("Cannot locate the file.")
boolstat = False
End If

' Activate the assembly so that you can add the component to it
swModel = swApp.**ActivateDoc3**(AssemblyTitle, True, swRebuildOnActivation_e.swUserDecision, errors)

' Add the camtest part to the assembly document
swComponent = swAssemblyDoc.**AddComponent5**(strCompModelname, swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -1, -1, -1)

' Make the component virtual
stat = swComponent.**MakeVirtual2**(True)

' Get the name of the component for the mate
strCompName = swComponent.**Name2**()

' Create the name of the mate and the names of the planes to use for the mate
MateName = "top_coinc_" + strCompName
FirstSelection = "Top@" + strCompName & "@" + AssemblyName
SecondSelection = "Front@" + AssemblyName

swModel.**ClearSelection2**(True)
swDocExt = swModel.**Extension**

' Select the planes for the mate
boolstat = swDocExt.**SelectByID2**(FirstSelection, "PLANE", 0, 0, 0, True, 1, Nothing, swSelectOption_e.swSelectOptionDefault)
boolstat = swDocExt.**SelectByID2**(SecondSelection, "PLANE", 0, 0, 0, True, 1, Nothing, swSelectOption_e.swSelectOptionDefault)

' Add the mate
matefeature = swAssemblyDoc.**AddMate5**(swMateType_e.swMateCOINCIDENT, swMateAlign_e.swMateAlignALIGNED, False, 0, 0, 0, 0, 0, 0, 0, 0, False, False, 0, mateError)
matefeature.**Name** = MateName
Debug.Print("Mate added: " & matefeature.**Name**)

swModel.**ViewZoomtofit2**()

End Sub

Sub AttachEventHandlers()
AttachSWEvents()
End Sub

Sub AttachSWEvents()
AddHandler swAssemblyDoc.**AddItemNotify**, AddressOf Me.swAssemblyDoc_AddItemNotify
AddHandler swAssemblyDoc.**RenameItemNotify**, AddressOf Me.swAssemblyDoc_RenameItemNotify
End Sub

Private Function swAssemblyDoc_AddItemNotify(ByVal EntityType As Integer, ByVal itemName As String) As Integer
Debug.Print("Component added: " & itemName)
End Function

Private Function swAssemblyDoc_RenameItemNotify(ByVal EntityType As Integer, ByVal oldName As String, ByVal NewName As String) As Integer
Debug.Print("Virtual component name: " & NewName)
End Function

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you
''' </summary>
Public swApp As SldWorks

End Class

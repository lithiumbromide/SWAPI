---
title: "Get Hidden Components Filenames Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hidden_Components_Filenames_Example_VBNET.htm"
---

# Get Hidden Components Filenames Example (VB.NET)

This example shows how to get the filenames of the hidden components in an assembly.

```
'-----------------------------------------------------------
' Preconditions:
' 1. In SOLIDWORKS Design, click File > Open, and browse to
'    public_documents\samples\tutorial\routing-pipes.
' 2. Click ball valve with flanges.sldasm > Mode >
'    Large Design Review > Open > OK.
'
'    NOTE: If the path to the Design Library does not exist,
'    then multiple dialogs informing you that SOLIDWORKS Design is unable
'    to locate might be displayed some components. Click No or OK
'    to close these dialogs.
'
' 3. Click ball valve-1 in the FeatureManager design tree
'    and click Selective Open > Selective Open > Selected components >
'    Open Selected > OK.
'
'    NOTE: Only the selected components are loaded. Components
'    not selected are not loaded and not visible in the
'    SOLIDWORKS Design graphics area.
'
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Does not load the slip on weld flange components because
'    they are hidden.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because this assembly elsewhere, do not save changes.
'-----------------------------------------------------------
```

```vb
Option Explicit On
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swAssembly As AssemblyDoc

        swAssembly = swApp.ActiveDoc
        If swAssembly.HasUnloadedComponents Then

            Dim oPaths As Object = Nothing
            Dim oRefdConfigs As Object = Nothing
            Dim oReasons As Object = Nothing
            Dim oDocTypes As Object = Nothing
            Dim oNames As Object = Nothing

            oNames = swAssembly.GetUnloadedComponentNames(oPaths, oRefdConfigs, oReasons, oDocTypes)

            Dim Paths() As String = Nothing
            Dim RefdConfigs() As String = Nothing
            Dim Reasons() As Integer = Nothing
            Dim DocTypes() As Integer = Nothing
            Dim Names() As String = Nothing

            Paths = oPaths
            RefdConfigs = oRefdConfigs
            Reasons = oReasons
            DocTypes = oDocTypes
            Names = oNames

            If Not (IsArray(Paths) And IsArray(RefdConfigs) And IsArray(Reasons) And IsArray(DocTypes) And IsArray(Names)) Then
                MsgBox("Error: Non-array parameter!")
                Debug.Assert(False)
                Exit Sub
            End If

            If (LBound(Paths) <> LBound(RefdConfigs)) Or (LBound(Paths) <> LBound(Reasons)) Or (LBound(Paths) <> LBound(DocTypes) Or (LBound(Paths) <> LBound(Names))) Then
                MsgBox("Error: Array lower bounds do not match!")
                Debug.Assert(False)
                Exit Sub
            End If

            If (UBound(Paths) <> UBound(RefdConfigs)) Or (UBound(Paths) <> UBound(Reasons)) Or (UBound(Paths) <> UBound(DocTypes) Or (UBound(Paths) <> UBound(Names))) Then
                MsgBox("Error: Array upper bounds do not match!")
                Debug.Assert(False)
                Exit Sub
            End If

            Dim index As Integer
            For index = LBound(Paths) To UBound(Paths)
                Dim debugMessage As String
                debugMessage = index & ": "

                Dim eDocType As swDocumentTypes_e
                eDocType = DocTypes(index)
                Select Case eDocType
                    Case swDocumentTypes_e.swDocNONE
                        debugMessage = debugMessage & "The document "
                    Case swDocumentTypes_e.swDocPART
                        debugMessage = debugMessage & "The part "
                    Case swDocumentTypes_e.swDocASSEMBLY
                        debugMessage = debugMessage & "The assembly "
                    Case swDocumentTypes_e.swDocDRAWING
                        debugMessage = debugMessage & "The drawing "
                    Case swDocumentTypes_e.swDocSDM
                        debugMessage = debugMessage & "The SDM "
                    Case Else
                        debugMessage = debugMessage & "The document is an unknown type "
                End Select

                debugMessage = debugMessage & Paths(index) & " was not loaded because it is "

                Dim bUnloadedBecauseHidden As Boolean
                bUnloadedBecauseHidden = Reasons(index)
                If bUnloadedBecauseHidden Then
                    debugMessage = debugMessage & "hidden."
                Else
                    debugMessage = debugMessage & "suppressed."
                End If

                Debug.Print(debugMessage)
            Next
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```

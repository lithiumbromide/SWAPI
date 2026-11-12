---
title: "Get Hidden Components Filenames Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hidden_Components_Filenames_Example_VB.htm"
---

# Get Hidden Components Filenames Example (VBA)

This example shows how to get the filenames of the components hidden in an assembly.

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Dim swAssembly As SldWorks.AssemblyDoc
    Set swAssembly = swApp.ActiveDoc
```

```
    If swAssembly.HasUnloadedComponents Then
        Dim vPaths As Variant
        Dim vRefdConfigs As Variant
        Dim vReasons As Variant
        Dim vDocTypes As Variant
        Dim vNames As Variant
```

```
        vNames = swAssembly.GetUnloadedComponentNames(vPaths, vRefdConfigs, vReasons, vDocTypes)
```

```
        If IsEmpty(vPaths) Or IsEmpty(vRefdConfigs) Or IsEmpty(vReasons) Or IsEmpty(vDocTypes) Or IsEmpty(vNames) Then
            MsgBox "Error: Empty VARIANT parameter!"
            Debug.Assert False
            Exit Sub
        End If
```

```
        If Not (IsArray(vPaths) And IsArray(vRefdConfigs) And IsArray(vReasons) And IsArray(vDocTypes) And IsArray(vNames)) Then
            MsgBox "Error: Non-array VARIANT parameter!"
            Debug.Assert False
            Exit Sub
        End If
```

```
        If (LBound(vPaths) <> LBound(vRefdConfigs)) Or (LBound(vPaths) <> LBound(vReasons)) Or (LBound(vPaths) <> LBound(vDocTypes)) Or (LBound(vPaths) <> LBound(vNames)) Then
            MsgBox "Error: Array lower bounds do not match!"
            Debug.Assert False
            Exit Sub
        End If
```

```
        If (UBound(vPaths) <> UBound(vRefdConfigs)) Or (UBound(vPaths) <> UBound(vReasons)) Or (UBound(vPaths) <> UBound(vDocTypes)) Or (UBound(vPaths) <> UBound(vNames)) Then
            MsgBox "Error: Array upper bounds do not match!"
            Debug.Assert False
            Exit Sub
        End If
```

```
        Dim index As Integer
        For index = LBound(vNames) To UBound(vNames)
            Dim debugMessage As String
            debugMessage = index & ": "
            Dim eDocType As swDocumentTypes_e
            eDocType = vDocTypes(index)
            Select Case eDocType
            Case swDocNONE
                debugMessage = debugMessage & "The document "
            Case swDocPART
                debugMessage = debugMessage & "The part "
            Case swDocASSEMBLY
               debugMessage = debugMessage & "The assembly "
            Case swDocDRAWING
                debugMessage = debugMessage & "The drawing "
            Case swDocSDM
                debugMessage = debugMessage & "The SDM "
            Case Else
               debugMessage = debugMessage & "The document of unknown type "
            End Select
```

```
          debugMessage = debugMessage & vPaths(index) & " was not loaded because it is "
```

```
            Dim bUnloadedBecauseHidden As Boolean
            bUnloadedBecauseHidden = vReasons(index)
            If bUnloadedBecauseHidden Then
                debugMessage = debugMessage & "hidden. "
            Else
                debugMessage = debugMessage & "suppressed."
            End If
            Debug.Print debugMessage
        Next
```

```
    End If
```

```
End Sub
```

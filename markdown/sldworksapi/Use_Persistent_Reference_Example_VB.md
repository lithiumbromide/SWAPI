---
title: "Use Persistent Reference Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Persistent_Reference_Example_VB.htm"
---

# Use Persistent Reference Example (VBA)

Persistent references are a means of returning to an item between sessions of SOLIDWORKS Design. Persistent references are similar to attributes, but are easier to use. In almost all cases, persistent references can, and should, be used in place of attributes.

This example:

- shows how to use persistent references.
- is primarily diagnostic code that determines whether the currently selected item has a persistent reference from which an object can be retrieved.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part, assembly, or drawing.
 ' 2. Select an entity.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the selected entity type and its PID.
 ' 2. Examine the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit

Function GetStringFromID(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vPIDarr As Variant) As String
    Dim vPID                        As Variant
     For Each vPID In vPIDarr
         Debug.Assert vbByte = VarType(vPID)
         GetStringFromID = GetStringFromID & Format(vPID, "###000")
     Next vPID
End Function
Function GetObjectFromString(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, IDstring As String) As Object
    Dim swModExt                    As SldWorks.ModelDocExtension
     Dim ByteStream()                As Byte
     Dim vPIDarr                     As Variant
     Dim nRetval                     As Long
     Dim i                           As Long
    Set swModExt = swModel.Extension
     ReDim ByteStream(Len(IDstring) / 3 - 1)
    For i = 0 To Len(IDstring) - 3 Step 3
         ByteStream(i / 3) = CByte(Mid(IDstring, i + 1, 3))
     Next i
    vPIDarr = ByteStream
    Set GetObjectFromString = swModExt.GetObjectByPersistReference3((vPIDarr), nRetval)
    Debug.Assert swPersistReferencedObject_Ok = nRetval
     Debug.Assert Not GetObjectFromString Is Nothing
End Function
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swModExt                    As SldWorks.ModelDocExtension
     Dim swSelMgr                    As SldWorks.SelectionMgr
     Dim swSelObj                    As Object
     Dim swObj                       As Object
     Dim vPIDarr                     As Variant
     Dim sIDstring                   As String
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
     Set swSelObj = swSelMgr.GetSelectedObject6(1, -1): Debug.Assert Not swSelObj Is Nothing
    vPIDarr = swModExt.GetPersistReference3(swSelObj): Debug.Assert Not IsEmpty(vPIDarr)
    Debug.Print "SelType = " & swSelMgr.GetSelectedObjectType3(1, -1)
    If IsEmpty(vPIDarr) Then
         Debug.Print "  ModelDocExtension::GetPersistReference3 broken"
         Exit Sub
     Else
         Debug.Print "  ModelDocExtension::GetPersistReference3 exists"
     End If
    sIDstring = GetStringFromID(swApp, swModel, vPIDarr)
    Debug.Print "  Persist Ref = " & sIDstring
    Set swObj = GetObjectFromString(swApp, swModel, sIDstring)
    If Not Nothing Is swObj Then
         Debug.Assert swSelObj Is swObj
         Debug.Print "  ModelDocExtension::GetObjectByPersistReference3 exists"
     Else
         Debug.Print "  ModelDocExtension::GetObjectByPersistReference3 broken"
     End If
End Sub
```

---
title: "Use Persistent Reference Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Persistent_Reference_Example_VBNET.htm"
---

# Use Persistent Reference Example (VB.NET)

Persistent references are a means of returning to an item between sessions of SOLIDWORKS Design. Persistent references are similar to attributes, but are easier to use. In almost all cases, persistent references can, and should, be used in place of attributes.

This example:

- shows how to use persistent references.
- is primarily diagnostic code that determines whether the currently selected item has a persistent reference from which an object can be retrieved.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part, assembly, or drawing.
 ' 2. Select an entity.
 '
 ' Postconditions:
 ' 1. Gets the selected entity type and its PID.
 ' 2. Examine the Immediate window.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Function GetStringFromID(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal vPIDarr As Object) As  String

         Dim vPID As Object
         For Each vPID In vPIDarr
             Debug.Assert(vbByte = VarType(vPID))
             GetStringFromID = GetStringFromID & Format(vPID,  "###000")
         Next vPID

     End Function

     Function GetObjectFromString(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal IDstring As String) As  Object

         Dim swModExt As ModelDocExtension
         Dim ByteStream() As Byte
         Dim vPIDarr As Object
         Dim nRetval As Long
         Dim i As  Long

         swModExt = swModel.Extension
         ReDim ByteStream(Len(IDstring) / 3 - 1)

         For i = 0 To Len(IDstring) - 3 Step 3
             ByteStream(i / 3) = CByte(Mid(IDstring, i + 1, 3))
         Next i

         vPIDarr = ByteStream

         GetObjectFromString = swModExt.GetObjectByPersistReference3((vPIDarr), nRetval)

         Debug.Assert(swPersistReferencedObjectStates_e.swPersistReferencedObject_Ok = nRetval)
         Debug.Assert(Not GetObjectFromString Is Nothing)

     End Function

     Sub main()

         Dim swModel As ModelDoc2
         Dim swModExt As ModelDocExtension
         Dim swSelMgr As SelectionMgr
         Dim swSelObj As Object
         Dim swObj As Object
         Dim vPIDarr As Object
         Dim sIDstring As String

         swModel = swApp.ActiveDoc
         swModExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         swSelObj = swSelMgr.GetSelectedObject6(1, -1) : Debug.Assert(Not swSelObj Is Nothing)

         vPIDarr = swModExt.GetPersistReference3(swSelObj) : Debug.Assert(Not IsNothing(vPIDarr))

         Debug.Print("SelType = " & swSelMgr.GetSelectedObjectType3(1, -1))

         If IsNothing(vPIDarr) Then
             Debug.Print("  ModelDocExtension::GetPersistReference3 broken")
             Exit Sub
         Else
             Debug.Print("  ModelDocExtension::GetPersistReference3 exists")
         End If

         sIDstring = GetStringFromID(swApp, swModel, vPIDarr)

         Debug.Print("  Persist Ref = " & sIDstring)

         swObj = GetObjectFromString(swApp, swModel, sIDstring)

         If Not  Nothing  Is swObj  Then
             Debug.Assert(swSelObj  Is swObj)
             Debug.Print("  ModelDocExtension::GetObjectByPersistReference3 exists")
         Else
             Debug.Print("  ModelDocExtension::GetObjectByPersistReference3 broken")
         End If

     End Sub

     Public swApp As SldWorks

 End  Class
```

---
title: "Get Paths and Titles of Parents of Virtual Component (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_VBNET.htm"
---

# Get Paths and Titles of Parents of Virtual Component (VB.NET)

This example shows how to get the paths and titles of the parent assembly components of a virtual component.

```vb
 '-----------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\assem2.sldasm
 ' 2. Open the Immediate window.
 '
 ' Postconditions: The paths and titles of the parent
 ' assembly components, up to and including the first non-virtual
 ' parent assembly component, are printed in the Immediate Window.
 '------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Diagnostics
 Imports System

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim doc As ModelDoc2
         doc = swApp.ActiveDoc
         If doc Is Nothing Then  Exit  Sub
         If doc.GetType <> swDocumentTypes_e.swDocASSEMBLY  Then  Exit  Sub

         Dim asm As AssemblyDoc
         asm = doc

         Dim components As Object
         components = asm.GetComponents(False)   ' Get all components

         If IsArray(components) Then
             Debug.Print("Virtual components in this assembly:")

             Dim compt As Object
             For Each compt In components
                 Dim comp As Component2
                 comp = compt

                 Dim compDoc As ModelDoc2
                 compDoc = comp.GetModelDoc2
                 If Not compDoc Is  Nothing  Then
                     Dim result3 As Boolean
                     Dim pathChain As Object = Nothing
                     Dim titleChain As Object = Nothing
                     result3 = compDoc.Extension.IsVirtualComponent3(pathChain, titleChain)

                     If result3 <> False Then
                         Debug.Print("  Virtual component name: " & comp.Name2)

                         Debug.Print("    " & "Paths:")
                         Dim path As Object
                         For Each path In pathChain
                             Debug.Print("      " & path)
                         Next

                         Debug.Print("    " & "Titles:")
                         Dim title As Object
                         For Each title In titleChain
                             Debug.Print("      " & title)
                         Next
                     End If
                 Else
                     Debug.Print(comp.Name2 & " <<< NOT LOADED >>>")
                 End If
             Next
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```

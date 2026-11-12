---
title: "Get Model Textures Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Texture_Example_VBNET.htm"
---

# Get Model Textures Example (VB.NET)

This example shows how to get the texture applied to components that are displayed in lightweight mode.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open in lightweight mode public_documents\samples\tutorial\api\TopAssembly1.SLDASM
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the textures of the
 ' lightweight components in the model.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDoc As ModelDoc2
     Dim swADoc As AssemblyDoc
     Dim varComp As Object
     Dim swTexture As Texture
     Sub main()

         swDoc = swApp.ActiveDoc
         swADoc = swDoc
         varComp = swADoc.GetComponents(True)

         Dim I As  Long
         Dim compName As String
         For I = LBound(varComp) To UBound(varComp)
             Dim swComp As Component2
             swComp = varComp(I)
             compName = swComp.ReferencedConfiguration

             swTexture = swComp.GetModelTexture(compName)
             If Not (swTexture Is  Nothing)  Then
                 Debug.Print(swComp.Name2 & "(" & I & ")" & "ConfigName : " & compName & "MatProp : ")
                 Debug.Print(swTexture.MaterialName)
                 Debug.Print("")
             End If
         Next I
         varComp = Nothing

     End Sub

     Public swApp As SldWorks

 End  Class
```

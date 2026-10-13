---
title: "Get Model Textures Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Texture_Example_VB.htm"
---

# Get Model Textures Example (VBA)

This example shows how to get the texture applied to components that are displayed in lightweight mode.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open in lightweight mode public_documents\samples\tutorial\api\TopAssembly1.SLDASM.
' 2. Open the Immediate window.
'
' Postconditions: Inspect the Immediate window for the textures of the
' lightweight components in the model.
'
' NOTE: Because the model is used elsewhere, do not save changes.
' ---------------------------------------------------------------------------
```

```vb
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swDoc As SldWorks.ModelDoc2
 Dim swADoc As SldWorks.AssemblyDoc
 Dim varComp As Variant
 Dim swTexture As SldWorks.Texture

Sub main()
```

```vb
Set swApp = Application.SldWorks
 Set swDoc = swApp.ActiveDoc
 Set swADoc = swDoc
 varComp = swADoc.GetComponents(True)
 Dim I As Long
 Dim compName As String
 For I = LBound(varComp) To UBound(varComp)
     Dim swComp As SldWorks.Component2
     Set swComp = varComp(I)
     compName = swComp.ReferencedConfiguration

    Set swTexture = swComp.GetModelTexture(compName)
     If Not (swTexture Is Nothing) Then
         Debug.Print (swComp.Name2 & "(" & I & ")" & "ConfigName : " & compName & "MatProp : ")
         Debug.Print (swTexture.MaterialName)
         Debug.Print ""

    End If
 Next I
 varComp = Empty
```

```vb
End Sub
```

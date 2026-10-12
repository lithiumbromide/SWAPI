---
title: "Get Face Hatch Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Face_Hatch_Data_Example_VBNET.htm"
---

# Get Face Hatch Data Example (VB.NET)

This example shows how to get the number of face hatches in a standard or derived (detail, section, projected, broken, etc.) drawing view and data.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Select Section View A-A in the FeatureManager design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets face hatch data.
' 2. Examine the Immediate window.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public
 Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swView As View
        Dim vFaceHatch As Object
        Dim swFaceHatch As FaceHatch
        Dim i As Long

        swApp = CreateObject("SldWorks.Application")
        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swView = swSelMgr.GetSelectedObject6(1,
 -1)
        Debug.Print("View   =
 " & swView.Name)
        Debug.Print("  Type =
 " & swView.Type)
```

```vb
         vFaceHatch = swView.GetFaceHatches
         If IsNothing(vFaceHatch) Then
             Debug.Print("  No face hatches in selected view.")
             Exit Sub
         End If
         Debug.Print("  Number of face hatches in this view = " & (UBound(vFaceHatch) + 1))
         If Not IsNothing(vFaceHatch) Then
             Debug.Print("  Face hatches =")
             Debug.Print("")
             For i = 0 To UBound(vFaceHatch)
                 swFaceHatch = vFaceHatch(i)
                 ' Get face hatch data
                 ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
                 Debug.Print("   Angle               = " & swFaceHatch.Angle * 57.3 & " degrees")
                 Debug.Print("   Color               = " & swFaceHatch.Color)
                 Debug.Print("   Definition          = " + swFaceHatch.Definition)
                 Debug.Print("   Layer               = " & swFaceHatch.Layer)
                 Debug.Print("   Pattern             = " + swFaceHatch.Pattern)
                 Debug.Print("   Scale               = " & swFaceHatch.Scale2)
                 Debug.Print("   SolidFill           = " & swFaceHatch.SolidFill)
                 Debug.Print("   Material crosshatch = " & swFaceHatch.UseMaterialHatch)
                 Debug.Print("   -----------------------")
             Next i
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```

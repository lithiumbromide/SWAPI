---
title: "Get Material Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Material_Properties_Example_VB.htm"
---

# Get Material Properties Example (VBA)

This example shows how to iterate over the faces and features of a model and get the displayed colors.

**NOTE:** When in shaded mode, colors can be allocated, in order of priority, at the model, feature, and face level. To correctly get the color a face, you must examine the color of the face at all of these levels. Also, several document-level preferences control how color is used. This example shows how to iterate over the faces and features of a model and correctly get the displayed color.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a part or fully resolved assembly.
' 2. If you opened an assembly, select any entity in the
'    the assembly.
' 3. Verify that c:\temp exists.
'
' Postconditions:
' 1. Writes the output to c:\ComponentMaterialPropertyValues.txt.
' 2. Examine c:\ComponentMaterialPropertyValues.txt.
'------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swPart As SldWorks.PartDoc
    Dim swComp As SldWorks.Component2
    Dim swBody As SldWorks.Body2
    Dim swFace As SldWorks.Face2
    Dim swFeat As SldWorks.Feature
    Dim vMatProp As Variant
    Dim vConfigNames As Variant
    Dim i As Long
    Dim bRet As Boolean
```

```
    ' Open output file for component material property values
    Open "c:\temp\ComponentMaterialPropertyValues.txt" For Output As #1
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    If swModel.GetType = swDocPART Then
        Set swPart = swModel
        Set swBody = swPart.Body
    Else
        Set swComp = swSelMgr.GetSelectedObjectsComponent2(1)
        Set swBody = swComp.GetBody
    End If
```

```
    Set swFace = swBody.GetFirstFace
```

```
    ' Get document default colors and settings
    Write #1, "Model Default [" & swModel.GetPathName & "]"
    Write #1, "  IgnoreFeatureColors  = " & swModel.GetUserPreferenceToggle(swIgnoreFeatureColors)
    Write #1, "  ColorRef             = " & swModel.GetUserPreferenceIntegerValue(swDocumentColorShading)
    Write #1, ""
```

```
    vMatProp = swModel.MaterialPropertyValues
    Write #1, "  RGB          = [" & vMatProp(0) & ", " & vMatProp(1) & ", " & vMatProp(2) & "]"
    Write #1, "  Ambient      = " & vMatProp(3)
    Write #1, "  Diffuse      = " & vMatProp(4)
    Write #1, "  Specular     = " & vMatProp(5)
    Write #1, "  Shininess    = " & vMatProp(6)
    Write #1, "  Transparency = " & vMatProp(7)
    Write #1, "  Emission     = " & vMatProp(8)
    Write #1, ""
```

```
    If Not swComp Is Nothing Then
        ' Component colors can override face colors
        vMatProp = swComp.MaterialPropertyValues
        If Not IsEmpty(vMatProp) Then
            Write #1, "Component Default [" & swComp.GetPathName & "]"
            Write #1, "  RGB          = [" & vMatProp(0) & ", " & vMatProp(1) & ", " & vMatProp(2) & "]"
            Write #1, "  Ambient      = " & vMatProp(3)
            Write #1, "  Diffuse      = " & vMatProp(4)
            Write #1, "  Specular     = " & vMatProp(5)
            Write #1, "  Shininess    = " & vMatProp(6)
            Write #1, "  Transparency = " & vMatProp(7)
            Write #1, "  Emission     = " & vMatProp(8)
            Write #1, ""
        End If
    End If
```

```
    While Not swFace Is Nothing
        ' Face colors can override part colors
        vMatProp = swFace.MaterialPropertyValues
        If Not IsEmpty(vMatProp) Then
            Write #1, "Face[" & i & "] overridden"
            Write #1, "  RGB          = [" & vMatProp(0) & ", " & vMatProp(1) & ", " & vMatProp(2) & "]"
            Write #1, "  Ambient      = " & vMatProp(3)
            Write #1, "  Diffuse      = " & vMatProp(4)
            Write #1, "  Specular     = " & vMatProp(5)
            Write #1, "  Shininess    = " & vMatProp(6)
            Write #1, "  Transparency = " & vMatProp(7)
            Write #1, "  Emission     = " & vMatProp(8)
            Write #1, ""
        End If
```

```
        ' Get feature associated with this face
        Set swFeat = swFace.GetFeature
        vConfigNames = swModel.GetConfigurationNames
```

```
       ' Face colors can override feature colors
        vMatProp = swFeat.GetMaterialPropertyValues2(swSpecifyConfiguration, (vConfigNames))
```

```
        If Not IsEmpty(vMatProp) Then
            Write #1, "Face[" & i & "] overridden by "; swFeat.Name
            Write #1, "  RGB          = [" & vMatProp(0) & ", " & vMatProp(1) & ", " & vMatProp(2) & "]"
            Write #1, "  Ambient      = " & vMatProp(3)
            Write #1, "  Diffuse      = " & vMatProp(4)
            Write #1, "  Specular     = " & vMatProp(5)
            Write #1, "  Shininess    = " & vMatProp(6)
            Write #1, "  Transparency = " & vMatProp(7)
            Write #1, "  Emission     = " & vMatProp(8)
            Write #1, ""
        End If
        i = i + 1
        Set swFace = swFace.GetNextFace
    Wend

    ' Close output file for component material property values
    Close

End Sub
```

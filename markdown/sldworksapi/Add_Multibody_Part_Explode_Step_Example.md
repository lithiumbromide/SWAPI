---
title: "Add Multibody Part Explode Step Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Multibody_Part_Explode_Step_Example.htm"
---

# Add Multibody Part Explode Step Example (VBA)

This example shows how to create an explode view of a multibody part.

```vb
  '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\multibody\multi_Inter.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Exploded View1 in ConfigurationManager.
 ' 2. Adds Chain1 to Exploded View1.
 ' 3. Displays the Exploded View1 in its exploded state.
 ' 4. Inspect the Immediate window, the ConfigurationManager,
 '    and the graphics area.
 '
 ' Note: Because the model is used elsewhere, do not save any changes.
  '----------------------------------------------------------------------------

 Option Explicit

 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.PartDoc
 Dim config As SldWorks.Configuration
 Dim configName As String
 Dim swMdl As SldWorks.ModelDoc2
 Dim explStep As SldWorks.PartExplodeStep
 Dim comp As SldWorks.Body2
 Dim var As Variant
 Dim varViews As Variant
```

Dim configVar As Variant

```vb
 Dim boolstatus As Boolean
 Dim i As Long
 Dim errCode As Long

 Sub main()

     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swMdl = swModel
```

configVar = swMdl.GetConfigurationNames

```vb
     Call swModel.CreateExplodedView

     varViews = swModel.GetExplodedViewNames(configVar(0))
     configName = swModel.GetExplodedViewConfigurationName(varViews(0))
     Set config = swMdl.GetConfigurationByName(configName)

     swModel.ShowExploded True, varViews(0)

     'Select the bodies to move
     boolstatus = swModel.Extension.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, True, 1, Nothing, 0)

     'Add an explode step without selecting an explode direction entity
     'Defaults to the Z-direction manipulator index
     Set explStep = config.AddPartExplodeStep("Exploded View1", 0.07, -1, False, True, errCode)

     Call swMdl.EditRebuild3

     'Get bodies moved in the explode step
     var = explStep.GetBodies()

     Debug.Print "Explode view: " & varViews(0)
     Debug.Print "Explode step: " & explStep.Name
     Debug.Print "Explode distance (m): " & explStep.ExplodeDistance
     Debug.Print "Reverse translation direction? " & explStep.ReverseTranslationDirection
     Debug.Print "Automatically space components on drag? " & explStep.AutoSpaceBodiesOnDrag

      Debug.Print "Bodies moved in the explode step:"
     For i = 0 To UBound(var)
         Set comp = var(i)
         Debug.Print "  " & comp.Name
     Next

 End Sub
```

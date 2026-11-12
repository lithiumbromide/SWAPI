---
title: "Get Explode Step Component Transform Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Explode_Step_Component_Transform_Example_VB.htm"
---

# Get Explode Step Component Transform Example (VBA)

This example shows how to get the transformation matrix of a component in a radial explode step and apply it to another component to overlap the components.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly with an explode view with at least one radial explode
' step with at least two components.
' 2. Activate the explode view.
' 3. Replace `component_name` in the code below with the name of a second
' component to overlap the first.
' 4. Open an Immediate window.
'
' Postconditions: For each explode step:
' 1. Gets the transformation matrix of a component in the radial explode step.
' 2. Selects another component to overlap.
' 3. Applies the transformation matrix to overlap the components.
' 4. Prints to the Immediate window the transformation matrix for the component.
'----------------------------------------------------------------------------

```vb
Dim swApp As SldWorks.SldWorks
 Dim assDoc As SldWorks.AssemblyDoc
 Dim c As SldWorks.Configuration
 Dim Part As MSldWorks.odelDoc2
 Dim es As SldWorks.ExplodeStep
 Dim comp As SldWorks.Component2
 Dim mathXForm As SldWorks.MathTransform
 Dim compXForm As SldWorks.MathTransform
 Dim obj As SldWorks.Component2
 Dim selMgr As SSldWorks.electionMgr
 Dim viewCount, nStep, i, j, k As Long
 Dim varComp, varXForm As Variant
 Dim MathUtility As SldWorks.MathUtility
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set assDoc = Part

    Set c = Part.GetActiveConfiguration

    nStep = c.GetNumberOfExplodeSteps

    For i = 0 To nStep - 1
         j = 1

        Set es = c.GetExplodeStep(i)
         varComp = es.GetComponents

        'Get the transformation matrix for the second component in the radial explode step
         Set comp = es.GetComponent(j)
         Debug.Print comp.Name2
         varXForm = es.GetStepComponentXForm(j)
         Set MathUtility = swApp.GetMathUtility
         Set mathXForm = MathUtility.CreateTransform(varXForm)

        'Select another component to overlap
         Set selMgr = Part.SelectionManager
         boolstatus = Part.Extension.SelectByID2("component_name", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
         Set obj = selMgr.GetSelectedObject6(1, -1)

        'Applies the transformation matrix to overlap the components
         Set compXForm = obj.Transform2
         Set compXForm = compXForm.Multiply(mathXForm)
         obj.Transform2 = compXForm

        Debug.Print es.Name & "  :  "
         For k = 0 To 15
             Debug.Print varXForm(k)
         Next k

        Call Part.EditRebuild3

    Next i

End Sub
```

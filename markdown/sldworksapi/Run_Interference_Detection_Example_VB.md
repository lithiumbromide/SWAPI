---
title: "Run Interference Detection Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Run_Interference_Detection_Example_VB.htm"
---

# Run Interference Detection Example (VBA)

This example shows how to run interference detection and observe the interferences in an assembly.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\advdrawings\bowl and chute.sldasm.
' 2. Ensure c:\temp exists.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the Interference Detection pane.
 ' 2. Gets interferences.
 ' 3. Gets interfering components and transforms.
 ' 4. Gets interference information.
 ' 5. In the Results list on the Interference Detection pane,
 '    click on each interference and observe it in the graphics area (red).
 ' 6. To close the Interference Detection pane, right-click the graphics area
 '    and select Cancel.
 ' 7. Inspect the Immediate window and c:\temp\IntDetReport.xlsx.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Option Explicit

 Sub main()
     Dim swApp As SldWorks.SldWorks
     Dim swModelDoc As SldWorks.ModelDoc2
     Dim swAssemblyDoc As SldWorks.AssemblyDoc
     Dim pIntMgr As SldWorks.InterferenceDetectionMgr
     Dim vInts As Variant
     Dim i As Long
     Dim j As Long
     Dim interference As IInterference
     Dim vComps As Variant
     Dim comp As Component2
     Dim vol As Double
     Dim vTrans As Variant
     Dim ret As Boolean

    Set swApp = Application.SldWorks
     Set swModelDoc = swApp.ActiveDoc
     Set swAssemblyDoc = swModelDoc

     'Open the Interference Detection pane
     swAssemblyDoc.ToolsCheckInterference

     Set pIntMgr = swAssemblyDoc.InterferenceDetectionManager

    'Specify the interference detection settings and options
     pIntMgr.TreatCoincidenceAsInterference = False
     pIntMgr.TreatSubAssembliesAsComponents = False
     pIntMgr.IncludeMultibodyPartInterferences = True
     pIntMgr.MakeInterferingPartsTransparent = True
     pIntMgr.CreateFastenersFolder = False
     pIntMgr.IgnoreHiddenBodies = False
     pIntMgr.ShowIgnoredInterferences = False
     pIntMgr.UseTransform = False

    'Specify how to display non-interfering components
     pIntMgr.NonInterferingComponentDisplay = swNonInterferingComponentDisplay_Wireframe

    'Run interference detection
     vInts = pIntMgr.GetInterferences
     Debug.Print "Number of interferences: " & pIntMgr.GetInterferenceCount

    'Get interfering components and transforms
     ret = pIntMgr.GetComponentsAndTransforms(vComps, vTrans)

    'Get interference information
     For i = 0 To UBound(vInts)
         Debug.Print "Interference " & (i + 1)
         Set interference = vInts(i)
         Debug.Print "  Number of components in this interference: " & interference.GetComponentCount
         vComps = interference.Components
         For j = 0 To UBound(vComps)
             Set comp = vComps(j)
             Debug.Print "    " & comp.Name2
         Next j
         vol = interference.Volume
         Debug.Print "  Interference volume is " & (vol * 1000000000) & " mm^3"
     Next i
    ret = pIntMgr.ExportResults("c:\temp\IntDetReport.xlsx", True)

    'Stop interference detection and close Interference Detection pane
    'pIntMgr.Done

End Sub
```

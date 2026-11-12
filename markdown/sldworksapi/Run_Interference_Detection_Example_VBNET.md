---
title: "Run Interference Detection Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Run_Interference_Detection_Example_VBNET.htm"
---

# Run Interference Detection Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics
 Partial  Class SolidWorksMacro
```

```vb
 Sub main()
```

```vb
 Dim swModelDoc As ModelDoc2
 Dim swAssemblyDoc As AssemblyDoc
 Dim pIntMgr As InterferenceDetectionMgr
 Dim vInts As Object
 Dim i As Long
 Dim j As Long
 Dim interference As IInterference
 Dim vComps As Object = Nothing
 Dim comp As Component2
 Dim vol As Double
 Dim vTrans As Object = Nothing
 Dim ret As Boolean
```

```vb
 swModelDoc = swApp.ActiveDoc
 swAssemblyDoc = swModelDoc

 'Open the Interference Detection pane
 swAssemblyDoc.ToolsCheckInterference

 pIntMgr = swAssemblyDoc.InterferenceDetectionManager
```

'Specify the interference detection settings and options
pIntMgr.**TreatCoincidenceAsInterference** = False
pIntMgr.**TreatSubAssembliesAsComponents** = False
**pIntMgr.IncludeMultibodyPartInterferences** = True
**pIntMgr.MakeInterferingPartsTransparent** = True
pIntMgr.**CreateFastenersFolder** = False
pIntMgr.**IgnoreHiddenBodies** = False
pIntMgr.**ShowIgnoredInterferences** = False
pIntMgr.**UseTransform** = False

'Specify how to display non-interfering components

pIntMgr.**NonInterferingComponentDisplay** = swNonInterferingComponentDisplay_e.swNonInterferingComponentDisplay_Wireframe

'Run interference detection
vInts = pIntMgr.**GetInterferences**
Debug.Print("# of interferences: " & pIntMgr.**GetInterferenceCount**)

```vb
 'Get interfering components and transforms
 ret = pIntMgr.GetComponentsAndTransforms(vComps, vTrans)
'Get interference information
 For i = 0 To UBound(vInts)
```

```vb
 Debug.Print("Interference " & (i + 1))
 interference = vInts(i)
 Debug.Print("  Number of components in this interference: " & interference.GetComponentCount)
 vComps = interference.Components
 For j = 0 To UBound(vComps)
```

```vb
comp = vComps(j)
 Debug.Print("   " & comp.Name2)
```

```vb
Next j
 vol = interference.Volume
 Debug.Print("  Interference volume is " & (vol * 1000000000)   " mm^3")
```

```vb
Next i
ret = pIntMgr.ExportResults("c:\temp\IntDetReport.xlsx", True)

 'Stop interference detection and close Interference Detection pane
 'pIntMgr.Done()
```

```vb
End Sub
```

```vb
    Public swApp As SldWorks
```

```vb
 End
```

Class

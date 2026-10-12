---
title: "Create Multibody Macro Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multibody_Macro_Feature_Example_VBNET.htm"
---

# Create Multibody Macro Feature Example (VB.NET)

This example shows how to create a multibody macro feature using a VB.NET SOLIDWORKS add-in.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 '  1. Contact SOLIDWORKS API Support to obtain API: C#\VB.NET Add-ins to Create a Macro Feature.
 '  2. Save InsertMacroFeature VB.NET Addin Mods for 64 bit.zip to a local drive.
 '  3. Unzip the file.
 '  4. Open Visual Studio 2015 and convert the VB.NET solution in Visual Studio.
 '  5. Modify the project references to point to your SOLIDWORKS primary interop
 '     assemblies.
 '  6. Double-click SwAddin.vb in the Solution Explorer.
 '  7. Replace Region ISwComFeature Implementation with  this.
 '  8. Replace AddMacroFeature() with this.
 '  9. Click Project > SwVBAddinTest Properties > Application and change
 '     Target framework to .NET FrameWork 4.
 ' 10. Click Compile > Build Events and replace the code in Post-build event
 '     command line with this.
 ' 11. Click Build > Build Solution.
 '     NOTE: The Output window notifies that types registered successfully.
 '     If that message does not appear in the Output window, repeat from
 '     step 1.
 ' 12. Open SOLIDWORKS Design.
 ' 13. Open public_documents\samples\tutorial\multibody\multi_local.sldprt.
 '
 ' Postconditions:
 '  1. Click OK in each message box.
 '  2. Displays  VB Addin on the Tools menu.
 '  3. Fires the ISldWorks_ActiveDocChangeNotify event and
 '     inserts the macro feature, MacroFeature1, in the
 '     FeatureManager design tree, which:
 '     * Consumes the part's solid bodies, Fillet5 and Fillet6.
 '     * Creates two solid bodies, MacroFeature1[1] and MacroFeature1[2].
 '  4. Examine the graphics area and FeatureManager design tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
'Region ISwComFeature Implementation
#Region "ISwComFeature Implementation"

     Function Edit(ByVal app As Object, ByVal modelDoc As Object, ByVal feature As Object) As Object Implements SwComFeature.Edit
         MsgBox("Macro feature edit")
         Return Nothing
     End Function

     Function Regenerate(ByVal app As Object, ByVal modelDoc As Object, ByVal feature As Object) As Object Implements SwComFeature.Regenerate
         Dim OutputBodies As New Collection
         Dim swBody As Body2
         Dim swBodies() As Body2
         Dim swMacroFeatData As MacroFeatureData
         swMacroFeatData = feature.GetDefinition
         swMacroFeatData.EnableMultiBodyConsume = True

         Dim swModeler As Modeler
         swModeler = app.GetModeler
         Dim dblData(8) As Double
         dblData(0) = 0 : dblData(1) = 0 : dblData(2) = 0
         dblData(3) = 1 : dblData(4) = 0 : dblData(5) = 0
         dblData(6) = 0.1 : dblData(7) = 0.1 : dblData(8) = 0.1

         'Output body 1
         swBody = swModeler.CreateBodyFromBox3(dblData)
         OutputBodies.Add(swBody)

         'Output body 2
         dblData(1) = 0.15
         swBody = swModeler.CreateBodyFromBox3(dblData)
         OutputBodies.Add(swBody)

         Dim i As Integer, j As Integer
         Dim vFaces As Object
         Dim vEdges As Object
         ReDim swBodies(OutputBodies.Count - 1)

         For i = 1 To OutputBodies.Count
             swBody = OutputBodies.Item(i)
             vEdges = swBody.GetEdges
             vFaces = swBody.GetFaces

             For j = 0 To UBound(vEdges)
                 swMacroFeatData.SetEdgeUserId(vEdges(j), j, 0)
             Next j
             For j = 0 To UBound(vFaces)
                 swMacroFeatData.SetFaceUserId(vFaces(j), j, 0)
             Next j

             swBodies(i - 1) = OutputBodies.Item(i)
         Next i

         Regenerate = swBodies
         MsgBox("Macro feature rebuild")

     End Function

     Function Security(ByVal app As Object, ByVal modelDoc As Object, ByVal feature As Object) As Object Implements SwComFeature.Security
         MsgBox("Macro feature security")
         Return Nothing
     End Function

 #End Region
```

[Back to top](#top)

```vb
'AddMacroFeature
    Function AddMacroFeature() As Boolean

         Dim moddoc As ModelDoc2
         Dim FeatMgr As FeatureManager
         Dim MacroFeature As Feature

         moddoc = Me.iSwApp.ActiveDoc
         FeatMgr = moddoc.FeatureManager

         'Collect input bodies
         Dim vBodies As Object
         vBodies = moddoc.GetBodies2(swBodyType_e.swAllBodies, False)

         'Create the macro feature
         MacroFeature = FeatMgr.InsertMacroFeature3("MacroFeature", "swVBAddinTest.SwAddin", Nothing, _
             Nothing, Nothing, Nothing, Nothing, Nothing, vBodies, Nothing, swMacroFeatureOptions_e.swMacroFeatureByDefault)

     End Function
```

[Back to top](#top)

IF EXIST "$(TargetDir)$(TargetName).bmp" (GOTO REGISTRATION)
XCOPY "$(ProjectDir)AddinIcon.bmp" "$(TargetDir)" /F
REN "$(TargetDir)AddinIcon.bmp" "$(TargetName).bmp"

:REGISTRATION
IF "$(TargetFrameworkVersion)"=="v4.0" GOTO NET40
IF "$(TargetFrameworkVersion)"=="v3.5" GOTO NET20
IF "$(TargetFrameworkVersion)"=="v3.0" GOTO NET20
IF "$(TargetFrameworkVersion)"=="v2.0" GOTO NET20
GOTO END

:NET40
set FMWK="v4.0.30319"
GOTO REG

:NET20
set FMWK="v2.0.50727"
GOTO REG

:REG
IF "$(PlatformName)" == "AnyCPU" GOTO ANYCPU
IF "$(PlatformName)" == "x64" GOTO X64
GOTO END

:ANYCPU
IF EXIST "%Windir%\Microsoft.NET\Framework64\%FMWK%\regasm.exe" "%Windir%\Microsoft.NET\Framework64\%FMWK%\regasm" /codebase "$(TargetPath)"
GOTO END

:X64
IF EXIST "%Windir%\Microsoft.NET\Framework64\%FMWK%\regasm.exe" "%Windir%\Microsoft.NET\Framework64\%FMWK%\regasm" /codebase "$(TargetPath)"
GOTO END

:END

[Back to top](#top)

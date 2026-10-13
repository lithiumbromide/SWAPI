---
title: "Get Mass Properties of Multibody Assembly Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm"
---

# Get Mass Properties of Multibody Assembly Component Example (VB.NET)

This example shows how to get the mass properties of a multibody assembly component in which an assembly cut-extrude feature is created.

**NOTES:**

-

  ```vb
  An assembly component, i.e., a part or subassembly, can contain  one or more assembly-level features. Some types of assembly features, e.g., cut extrude, can affect the mass properties. Assembly features are not present in the part or subassembly.
  ```
-

  ```vb
  Mass property values returned are relative to the component origin, not the assembly origin.
  ```

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified multibody part document
'    and assembly document template exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified multibody part document.
' 2. Creates an assembly using the specified multibody
'    part document.
' 3. Creates an assembly cut-extrude feature.
' 4. Selects the multibody component.
' 5. Gets the mass property values of the multibody
'    component.
' 6. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDocExt As ModelDocExtension
        Dim swAssembly As AssemblyDoc
        Dim swMass As MassProperty
        Dim swSelMgr As SelectionMgr
        Dim swComp As Component2
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeatMgr As FeatureManager
        Dim swFeat As Feature
        Dim vBodyInfo As Object = Nothing
        Dim vCoM() As Double
        Dim vMoI() As Double
        Dim vPrinAoIx() As Double
        Dim vPrinAoIy() As Double
        Dim vPrinAoIz() As Double
        Dim vPrinMoI() As Double
        Dim bRet As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        'Open multibody part document and create an assembly
        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2017\templates\Assembly.asmdot", 0, 0, 0)
        swAssembly = swModel
        swComp = swAssembly.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt", swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -0.0000926777909171506, 0, 0.000048904806817518)

        'Create an assembly cut-extrude feature
        swDocExt = swModel.Extension
        swSketchMgr = swModel.SketchManager
        swFeatMgr = swModel.FeatureManager
        bRet = swDocExt.SelectByID2("", "FACE", -0.0195381300573558, 0.0449999999998454, -0.00303401890568011, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchMgr.CreateCircle(0.0#, 0.0#, 0.0#, 0.002956, -0.004701, 0.0#)
        swModel.ClearSelection2(True)
        bRet = swDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        swFeat = swFeatMgr.FeatureCut3(True, False, False, 0, 0, 0.5, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
        swSelMgr = swModel.SelectionManager
        swSelMgr.EnableContourSelection = False

        'Select multibody component
        bRet = swDocExt.SelectByID2("multi_inter-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

        swMass = swDocExt.CreateMassProperty
        swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
        Dim vBodies(0) As Object
        vBodies = swComp.GetBodies3(swBodyType_e.swSolidBody, vBodyInfo)
        Dim dispArray() As DispatchWrapper
        dispArray = ObjectArrayToDispatchWrapperArray(vBodies)
        bRet = swMass.AddBodies(dispArray)

        'Get mass properties of selected component's bodies
        vCoM = swMass.CenterOfMass
        vMoI = swMass.GetMomentOfInertia(swMassPropertyMoment_e.swMassPropertyMomentAboutCenterOfMass)
        vPrinAoIx = swMass.PrincipleAxesOfInertia(0)
        vPrinAoIy = swMass.PrincipleAxesOfInertia(1)
        vPrinAoIz = swMass.PrincipleAxesOfInertia(2)
        vPrinMoI = swMass.PrincipleMomentsOfInertia
        Debug.Print("Component = " & swComp.Name2)
        Debug.Print("Configuration = " & swComp.ReferencedConfiguration)
        Debug.Print("Density = " & swMass.Density & " kg/m^3")
        Debug.Print("")
        Debug.Print("Center of mass = (" & vCoM(0) * 1000.0# & ", " & vCoM(1) * 1000.0# & ", " & vCoM(2) * 1000.0# & ") mm")
        Debug.Print("Volume = " & swMass.Volume * 1000000000.0# & " mm^3")
        Debug.Print("Area = " & swMass.SurfaceArea * 1000000.0# & " mm^2")
        Debug.Print("Mass = " & swMass.Mass & " kg")
        Debug.Print("Principle axes of inertia ")
        Debug.Print("  Ix = (" & vPrinAoIx(0) & ", " & vPrinAoIx(1) & ", " & vPrinAoIx(2) & ")")
        Debug.Print("  Iy = (" & vPrinAoIy(0) & ", " & vPrinAoIy(1) & ", " & vPrinAoIy(2) & ")")
        Debug.Print("  Iz = (" & vPrinAoIz(0) & ", " & vPrinAoIz(1) & ", " & vPrinAoIz(2) & ")")
        Debug.Print("Principle moments of inertia")
        Debug.Print("  Px = " & vPrinMoI(0) & " kg*m^2")
        Debug.Print("  Py = " & vPrinMoI(1) & " kg*m^2")
        Debug.Print("  Pz = " & vPrinMoI(2) & " kg*m^2")
        Debug.Print("Products of inerita")
        Debug.Print("  Lxx = " & vMoI(0) & " kg*m^2")
        Debug.Print("  Lxy = " & vMoI(1) & " kg*m^2")
        Debug.Print("  Lxz = " & vMoI(2) & " kg*m^2")
        Debug.Print("  Lyx = " & vMoI(3) & " kg*m^2")
        Debug.Print("  Lyy = " & vMoI(4) & " kg*m^2")
        Debug.Print("  Lyz = " & vMoI(5) & " kg*m^2")
        Debug.Print("  Lzx = " & vMoI(6) & " kg*m^2")
        Debug.Print("  Lzy = " & vMoI(7) & " kg*m^2")
        Debug.Print("  Lzz = " & vMoI(8) & " kg*m^2")

    End Sub

    Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()
        Dim ArraySize As Integer
        ArraySize = Objects.GetUpperBound(0)
        Dim d(ArraySize) As DispatchWrapper
        Dim ArrayIndex As Integer
        For ArrayIndex = 0 To ArraySize
            d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
        Next
        Return d
    End Function

    Public swApp As SldWorks

End Class
```

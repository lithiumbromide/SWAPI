---
title: "Get and Set Seed Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Seed_Components_Example_VBNET.htm"
---

# Get and Set Seed Components Example (VB.NET)

This example shows how to access the seed components of patterns in an assembly. It also shows that seed components can be replaced by either IComponent2 objects or IFeature objects representing those components.

```vb
 '------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified assembly exists.
 ' 2. Open the Immediate Window.
 '
 ' Postconditions:
 ' 1. Gets the names of the seed components.
 ' 2. Replaces the seed components by an IComponent2 object
 '    or an IFeature object representing the component.
 ' 3. Examine the Immediate window.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim dispWrapArr() As DispatchWrapper

         Dim fileName As String
         Dim errors As Long
         Dim warnings As Long
         fileName =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem2.sldasm"

         ' Open the model
         Dim swModel As ModelDoc2
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

         ' Verify that the model is active
         If swModel Is Nothing Then
             Debug.Print("No active model document")
             Exit Sub
         End If

         Debug.Print("Model: " & swModel.GetTitle)

         ' Get all of the features in the model
         Dim swFeatMgr As FeatureManager
         swFeatMgr = swModel.FeatureManager

         Dim vFeatures As Object
         vFeatures = swFeatMgr.GetFeatures(True)

         ' Iterate over all features
         Dim iFeat As Integer
         For iFeat = LBound(vFeatures) To UBound(vFeatures)
             Dim swFeature As Feature
             swFeature = vFeatures(iFeat)

             ' Is the current feature a patterned feature?
             Select Case UCase(swFeature.GetTypeName2)
                 Case "LOCALLPATTERN"
                     ' ILocalLinearPatternFeatureData
                     Debug.Print("    Linear Pattern: " & swFeature.Name)
                     Dim llpDefinition As LocalLinearPatternFeatureData
                     llpDefinition = swFeature.GetDefinition
                     Dim llpSeedComps() As Object
                     ReDim llpSeedComps(0)
                     If llpDefinition.AccessSelections(swModel,  Nothing)  Then
                         ' Get the seed components for this pattern
                         llpSeedComps = llpDefinition.SeedComponentArray
                         ReDim Preserve llpSeedComps(UBound(llpSeedComps))
                     End If

                     ' Arbitrarily decide whether to replace each seed component
                     ' with a component or a feature
                     ProcessSeedComponentArray(llpSeedComps)

                     dispWrapArr = ObjectArrayToDispatchWrapperArray(llpSeedComps)
                     llpDefinition.SeedComponentArray = dispWrapArr

                     ' Update the feature definition
                     swFeature.ModifyDefinition(llpDefinition, swModel, Nothing)

                 Case "LOCALCIRPATTERN"
                     ' ILocalCircularPatternFeatureData
                     Debug.Print("    Circular Pattern: " & swFeature.Name)
                     Dim cpDefinition As LocalCircularPatternFeatureData
                     cpDefinition = swFeature.GetDefinition
                     Dim cpSeedComps() As Object
                     ReDim cpSeedComps(0)
                     If cpDefinition.AccessSelections(swModel,  Nothing)  Then
                         ' Get the seed components for this pattern
                         cpSeedComps = cpDefinition.SeedComponentArray
                         ReDim Preserve cpSeedComps(UBound(cpSeedComps))
                     End If

                     ' Arbitrarily decide whether to replace each seed component
                     ' with a component or a feature
                     ProcessSeedComponentArray(cpSeedComps)

                     dispWrapArr = ObjectArrayToDispatchWrapperArray(cpSeedComps)
                     cpDefinition.SeedComponentArray = dispWrapArr

                     ' Update the feature definition
                     swFeature.ModifyDefinition(cpDefinition, swModel, Nothing)

                 Case "DERIVEDLPATTERN"
                     ' IDerivedPatternFeatureData
                     Debug.Print("    Derived Linear Pattern: " & swFeature.Name)
                     Dim dpDefinition As DerivedPatternFeatureData
                     dpDefinition = swFeature.GetDefinition
                     Dim dpSeedComps(0)
                     If dpDefinition.AccessSelections(swModel,  Nothing)  Then
                         ' Get the seed components for this pattern
                         dpSeedComps = dpDefinition.SeedComponentArray
                         ReDim Preserve dpSeedComps(UBound(dpSeedComps))
                     End If

                     ' Arbitrarily decide whether to replace each seed component
                     ' with a component or a feature
                     ProcessSeedComponentArray(dpSeedComps)

                     dispWrapArr = ObjectArrayToDispatchWrapperArray(dpSeedComps)
                     dpDefinition.SeedComponentArray = dispWrapArr

                     ' Update the feature definition
                     swFeature.ModifyDefinition(dpDefinition, swModel, Nothing)

                 Case "DERIVEDCIRPATTERN"
                     ' IDerivedPatternFeatureData
                     Debug.Print("    Derived Circular Pattern: " & swFeature.Name)
                     Dim dcpDefinition As DerivedPatternFeatureData
                     dcpDefinition = swFeature.GetDefinition
                     Dim dcpSeedComps() As Object
                     ReDim dcpSeedComps(0)
                     If dcpDefinition.AccessSelections(swModel,  Nothing)  Then
                         ' Get the seed components for this pattern
                         dcpSeedComps = dcpDefinition.SeedComponentArray
                         ReDim Preserve dcpSeedComps(UBound(dcpSeedComps))
                     End If

                     ' Arbitrarily decide whether to replace each seed component
                     ' with a component or a feature
                     ProcessSeedComponentArray(dcpSeedComps)

                     dispWrapArr = ObjectArrayToDispatchWrapperArray(dcpSeedComps)
                     dcpDefinition.SeedComponentArray = dispWrapArr

                     ' Update the feature definition
                     swFeature.ModifyDefinition(dcpDefinition, swModel, Nothing)

             End Select
         Next

     End Sub

     Private Sub ProcessSeedComponentArray(ByRef vSeedComps As Object())
         Dim replacementSeeds() As Object
         ReDim Preserve replacementSeeds(UBound(vSeedComps))

         ' Iterate over each seed component
         Dim iSeed As Integer
         For iSeed = LBound(vSeedComps) To UBound(vSeedComps)
             Dim swCompFeat As Feature
             swCompFeat = vSeedComps(iSeed)
             Debug.Print("        Seed " & iSeed & ": " & swCompFeat.Name)

             ' Access the seed component represented by the feature
             Dim swComp As Component2
             swComp = swCompFeat.GetSpecificFeature2

             ' Arbitrarily decide whether to replace this seed component
             ' with a component or a feature
             If iSeed Mod 2 = 0 Then
                 replacementSeeds(iSeed) = swComp
             Else
                 replacementSeeds(iSeed) = swCompFeat
             End If
         Next

         ' Replace the seed array
         vSeedComps = replacementSeeds

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

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```

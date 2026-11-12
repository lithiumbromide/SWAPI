---
title: "Get DimXpert Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Feature_Example_VBNET.htm"
---

# Get DimXpert Feature Example (VB.NET)

This example builds a part to demonstrate usage of the DimXpert API for the following DimXpert features:

* Cylinder

* Fillet

* Plane

* Slot

* Pattern

```vb
'-------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cover_plate.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars.
' 3. Click Auto Dimension Scheme on the DimXpert toolbar.
' 4. Ensure that all of the feature filters are selected.
' 5. Click the green check mark to accept the settings.
' 6. Observe the following DimXpert feature types on the DimXpertManager tab:
'    Cylinder, Fillet, Plane, Slot, Pattern.
' 7. Open the Immediate window.
' 8. Ensure that the latest SolidWorks.Interop.swdimXpert.dll interop assembly
'    is loaded (right-click project in Project Explorer and click Add Reference >
'    .NET tab).
'
' Postconditions: Compare the output in the Immediate Window
' with the features displayed on the DimXpertManager tab of the Management Panel.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swdimxpert
Imports SolidWorks.Interop.swconst
Imports System.Diagnostics
Imports System
Partial Class SolidWorksMacro
    Dim swModel As IModelDoc2
    Dim swModelDocExt As IModelDocExtension
    Dim swSelMgr As ISelectionMgr
    Dim swConfig As IConfiguration
    Dim swFeature As IFeature
    Dim swAnn As IFeature
    Dim swSchema As IDimXpertManager
    Dim swDXPart As IDimXpertPart
    Dim featureType As swDimXpertFeatureType_e
    Dim features As Object
    Dim appliedFeatures As Object
    Dim appliedAnnotations As Object
    Dim appliedAnnotation As IDimXpertAnnotation
    Dim feature As IDimXpertFeature
    Dim appliedFeature As IDimXpertFeature
    Dim msgStr As String
    Dim msgStr2 As String
    Dim msgStr3 As String
    Dim msgStr4 As String
    Dim n As Long
    Dim o As Long
    Dim p As Long
    Dim boolstatus As Boolean
    Sub main()
        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        ' Get the default DimXpert schema using IModelDocExtension.DimXpertManager()
        swSchema = swModelDocExt.DimXpertManager("Default", True)
        ' Get IDimXpertPart from the IDimXpertManager
        swDXPart = swSchema.DimXpertPart
        Dim featCount As Long
        featCount = swDXPart.GetFeatureCount
        msgStr = "Total of "
        msgStr2 = featCount
        msgStr = msgStr + msgStr2 + " features in " + (swSchema.SchemaName)
        Debug.Print("")
        Debug.Print(msgStr)
        ' Get IDimXpert features through IDimXpertPart
        features = swDXPart.GetFeatures
        msgStr = (swSchema.SchemaName) + " has the following features: "
        Debug.Print("")
        Debug.Print(msgStr)
        For n = 0 To UBound(features)
            ' Use IDimXpertFeature to get general feature data
            feature = features(n)
            Debug.Print("  " + "Feature name: " + (feature.Name))
            featureType = feature.Type
            Call GetPatternType(featureType, msgStr2)
            msgStr = "     Feature type "
            msgStr3 = " is suppressed on the DimXpertManager tab? "
            msgStr4 = feature.IsSuppressed()
            Debug.Print(msgStr + msgStr2 + msgStr3 + msgStr4)
            msgStr = "     " + "Model feature: "
            ' Use IFeature to get the Swift model feature corresponding to this geometric dimensioning and tolerance feature
            swFeature = feature.GetModelFeature()
            If Not (swFeature Is Nothing) Then
                msgStr2 = swFeature.GetTypeName2()
                Debug.Print(msgStr + msgStr2)
            End If
            msgStr = "     " + "Number of SOLIDWORKS face entities in this feature: "
            msgStr2 = feature.GetFaceCount
            Debug.Print(msgStr + msgStr2)
            msgStr = "     " + "Number of applied features: "
            msgStr2 = feature.GetAppliedFeatureCount()
            Debug.Print(msgStr + msgStr2)
            appliedFeatures = feature.GetAppliedFeatures()
            If Not (IsNothing(appliedFeatures)) Then
                For o = 0 To UBound(appliedFeatures)
                    appliedFeature = appliedFeatures(o)
                    Debug.Print("        " + "Applied feature name: " + (appliedFeature.Name))
                Next
            End If
            msgStr = "     " + "Number of applied annotations: "
            msgStr2 = feature.GetAppliedAnnotationCount()
            Debug.Print(msgStr + msgStr2)
            appliedAnnotations = feature.GetAppliedAnnotations()
            If Not (IsNothing(appliedAnnotations)) Then
                For p = 0 To UBound(appliedAnnotations)
                    appliedAnnotation = appliedAnnotations(p)
                    Debug.Print("        " + "Applied annotation name: " + (appliedAnnotation.Name))
                Next
            End If
            Debug.Print("     ")
        Next
        ' If you know the name of a DimXpert feature, you can get it directly using IDimXpertPart.GetFeature("name"),
        ' which can return a general IDimXpertFeature or a more specific interface on the feature
        Dim cylinderFeature As IDimXpertCylinderFeature
        cylinderFeature = swDXPart.GetFeature("Cylinder1")
        msgStr = cylinderFeature.Name + " is a DimXpert feature"
        Debug.Print("")
        Debug.Print(msgStr)
        ' Get the nominal top plane coordinates for Cylinder1
        Dim x As Double
        Dim y As Double
        Dim z As Double
        Dim i As Double
        Dim j As Double
        Dim k As Double
        boolstatus = cylinderFeature.GetNominalTopPlane(x, y, z, i, j, k)
        msgStr = "X-coordinate of nominal top plane of " + cylinderFeature.Name + " is "
        msgStr2 = x
        Debug.Print(msgStr + msgStr2)
        ' Get the thread for the cylinder, if it exists
        Dim isThreaded As Boolean
        Dim threadDesignation As String
        Dim threadDepth As Double
        boolstatus = cylinderFeature.GetThread(isThreaded, threadDesignation, threadDepth)
        msgStr = "The cylinder is threaded? "
        msgStr2 = isThreaded
        Debug.Print(msgStr + msgStr2)
        Debug.Print("")
        ' Get the radius of Fillet1
        Dim filletFeature As IDimXpertFilletFeature
        filletFeature = swDXPart.GetFeature("Fillet1")
        msgStr = filletFeature.Name + " is a DimXpert feature"
        Debug.Print("")
        Debug.Print(msgStr)
        Dim radius As Double
        radius = filletFeature.radius
        msgStr = "The fillet radius is "
        msgStr2 = radius
        Debug.Print(msgStr + msgStr2)
        Dim planeFeature As IDimXpertPlaneFeature
        planeFeature = swDXPart.GetFeature("Plane1")
        msgStr = planeFeature.Name + " is a DimXpert feature"
        Debug.Print("")
        Debug.Print(msgStr)
        ' Get the nominal top plane coordinates for Plane1
        boolstatus = planeFeature.GetNominalPlane(x, y, z, i, j, k)
        msgStr = "X-coordinate of nominal top plane of " + planeFeature.Name + " is "
        msgStr2 = x
        Debug.Print(msgStr + msgStr2)
        ' Get the nominal closed slot width for Slot1
        Dim slotFeature As IDimXpertCompoundClosedSlot3DFeature
        slotFeature = swDXPart.GetFeature("Slot1")
        msgStr = slotFeature.Name + " is a DimXpert feature"
        Debug.Print("")
        Debug.Print(msgStr)
        Dim width As Double
        Dim length As Double
        Dim longitudeI As Double
        Dim longitudeJ As Double
        Dim longitudeK As Double
        boolstatus = slotFeature.GetNominalClosedSlot(width, length, x, y, z, i, j, k, longitudeI, longitudeJ, longitudeK)
        msgStr = "Width of nominal closed slot is "
        msgStr2 = width
        Debug.Print(msgStr + msgStr2)
        ' Get the sub-features of Slot Pattern1
        Dim patternFeature As IDimXpertPatternFeature
        patternFeature = swDXPart.GetFeature("Slot Pattern1")
        msgStr = patternFeature.Name + " is a DimXpert feature"
        Debug.Print("")
        Debug.Print(msgStr)
        featureType = patternFeature.PatternType
        Call GetPatternType(featureType, msgStr2)
        Dim featureCount As Integer
        featureCount = patternFeature.GetSubFeatureCount()
        msgStr = "     Number of "
        msgStr3 = featureCount
        Debug.Print(msgStr + msgStr2 + " is " + msgStr3)
        Dim subfeatures As Object
        subfeatures = patternFeature.GetSubFeatures()
        Debug.Print("     Sub-features of Slot Pattern1:")
        For n = 0 To UBound(subfeatures)
            ' Use IDimXpertCompoundClosedSlot3DFeature to get the two planes of the slot
            ' The names of the planes are inherited from the Name property of the parent interface, IDimXpertFeature
            slotFeature = subfeatures(n)
            Debug.Print("        " + slotFeature.Name)
            Dim plane1 As IDimXpertPlaneFeature
            Dim plane2 As IDimXpertPlaneFeature
            boolstatus = slotFeature.GetPlaneFeatures(plane1, plane2)
            Debug.Print("          " + plane1.Name)
            Debug.Print("          " + plane2.Name)
        Next
    End Sub
    Public Sub GetPatternType(ByRef featureType As swDimXpertFeatureType_e, ByRef msgStr2 As String)
        If (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Plane) Then
            msgStr2 = "Plane"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Cylinder) Then
            msgStr2 = "Cylinder"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Cone) Then
            msgStr2 = "Cone"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Extrude) Then
            msgStr2 = "Boss"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Fillet) Then
            msgStr2 = "Fillet"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Chamfer) Then
            msgStr2 = "Chamfer"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundHole) Then
            msgStr2 = "CompoundHole"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundWidth) Then
            msgStr2 = "CompoundWidth"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundNotch) Then
            msgStr2 = "CompoundNotch"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_CompoundClosedSlot3D) Then
            msgStr2 = "CompoundClosedSlot3D"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectPoint) Then
            msgStr2 = "IntersectPoint"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectLine) Then
            msgStr2 = "IntersectLine"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectCircle) Then
            msgStr2 = "IntersectCircle"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_IntersectPlane) Then
            msgStr2 = "IntersectPlane"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Pattern) Then
            msgStr2 = "Pattern"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Sphere) Then
            msgStr2 = "Sphere"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_BestfitPlane) Then
            msgStr2 = "Bestfit plane"
        ElseIf (featureType = swDimXpertFeatureType_e.swDimXpertFeature_Surface) Then
            msgStr2 = "Surface"
        End If
    End Sub
    Public swApp As SldWorks
End Class
```

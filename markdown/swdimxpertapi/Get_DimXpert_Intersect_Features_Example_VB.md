---
title: "Get DimXpert Intersect Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Intersect_Features_Example_VB.htm"
---

# Get DimXpert Intersect Features Example (VBA)

This example shows how to build a part and get attributes for the following DimXpert features:

* Intersect Point

* Intersect Line

* Intersect Circle

* Intersect Plane

```vb
''---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\face_plate_ads_geo.sldprt..
' 2. Open the DimXpert toolbar from View > Toolbars.
' 3. Create an Intersect Point Dimxpert Feature:
'    a. Click Location Dimension on the DimXpert toolbar.
'    b. Select the front face of the part.
'    c. Select Create Intersection Point from the DimXpert shortcut menu.
'    d. Select a cylinder whose axis intersects the first face at a point.
'    e. Click the green check mark in the shortcut menu to create the
'       intersect point.
'    f. Select a feature on the part to dimension against the intersect point.
'    g. Click to position the dimension in the view.
'    h. Observe the new Dimxpert feature on the DimXpertManager tab:
'       Intersect Point1
' 4. Create an Intersect Line Dimxpert Feature:
'    a. Click Location Dimension on the DimXpert toolbar.
'    b. Select the front face of the part.
'    c. Select Create Intersection Line from the DimXpert shortcut menu.
'    d. Select a perpendicular plane that would intersect the first plane
'       if extended (e.g., a top or side face of the part).
'    e. Click the green check mark in the shortcut menu to create the
'       intersect line.
'    f. Select a feature on the part to dimension against the intersect line.
'    g. Click to position the dimension in the view.
'    h. Observe the new Dimxpert feature on the DimXpertManager tab:
'       Intersect Line1
' 5. Create an Intersect Circle Dimxpert Feature:
'    a. Click Size Dimension on the DimXpert toolbar.
'    b. Select the front face of the part.
'    c. Select Intersect Circle from the DimXpert shortcut menu.
'    d. Select the opening conical surface of a flat head machine screw
'       (LPattern1 or LPattern3) in the part.
'    e. Click the green check mark in the shortcut menu to finish the dimension.
'    f. Click to position the size dimension in the view.
'    g. Observe the new Dimxpert feature on the DimXpertManager tab:
'        Intersect Circle1
' 6. Create an Intersect Plane Dimxpert Feature:
'    a. Click Location Dimension on the DimXpert toolbar.
'    b. Zoom in on a flat head machine screw (LPattern1 or LPattern3).
'    c. Select the opening conical surface of a flat head machine screw
'       in the part.
'    d. Select Intersect Plane from the DimXpert shortcut menu.
'    e. Select the inner cylindrical bore face of the flat head machine screw.
'    f. Click the green check mark in the pop-up menu to create the
'       intersect plane.
'    g. Select the top face of one of the extruded entities.
'    h. Click to position the location dimension in the view.
'    i. Observe the new Dimxpert feature on the DimXpertManager tab:
'        Intersect Plane1
' 7. Open the Immediate window.
' 8. Ensure that the SOLIDWORKS DimXpert type library is loaded
'    in Tools > References.
'
' Postconditions: Compare the output in the Immediate Window with the features
' displayed on the DimXpertManager tab of the Management Panel.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As ModelDoc2
Dim swModelDocExt As ModelDocExtension
Dim swSelMgr As SelectionMgr
Dim swConfig As Configuration
Dim swFeature As feature
Dim swAnn As feature
Dim swSchema As DimXpertManager
Dim swDXPart As DimXpertPart
Dim featureType As swDimXpertFeatureType_e
Dim features As Variant
Dim appliedFeatures As Variant
Dim appliedAnnotations As Variant
Dim appliedAnnotation As DimXpertAnnotation
Dim feature As DimXpertFeature
Dim feature1 As DimXpertFeature
Dim feature2 As DimXpertFeature
Dim appliedFeature As DimXpertFeature
Dim msgStr As String
Dim msgStr2 As String
Dim msgStr3 As String
Dim msgStr4 As String
Dim n As Long
Dim o As Long
Dim p As Long
Dim x As Double
Dim y As Double
Dim z As Double
Dim i As Double
Dim j As Double
Dim k As Double
Dim radius As Double
Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc

    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager

    ' Get the default DimXpert schema using IModelDocExtension.DimXpertManager()

    Set swSchema = swModelDocExt.DimXpertManager("Default", True)

    ' Get IDimXpertPart from the IDimXpertManager
    Set swDXPart = swSchema.DimXpertPart

    Dim featCount As Long
    featCount = swDXPart.GetFeatureCount
    msgStr = "Total of "
    msgStr2 = featCount
    msgStr = msgStr + msgStr2 + " DimXpert features in " + (swSchema.SchemaName)
    Debug.Print ""
    Debug.Print msgStr

    ' Get IDimXpert features through IDimXpertPart

    features = swDXPart.GetFeatures

    msgStr = (swSchema.SchemaName) + " has the following features: "
    Debug.Print ""
    Debug.Print msgStr
    For n = 0 To UBound(features)
        Set feature = features(n)
        Debug.Print "  " + "Feature name: " + (feature.Name)

        featureType = feature.Type
        Call GetPatternType(featureType, msgStr2)

        msgStr = "     Feature type "
        msgStr3 = " is suppressed on the DimXpertManager tab? "
        msgStr4 = feature.IsSuppressed()
        Debug.Print msgStr + msgStr2 + msgStr3 + msgStr4

        msgStr = "     " + "Model feature: "
        Set swFeature = feature.GetModelFeature()
        If Not (swFeature Is Nothing) Then
            msgStr2 = swFeature.GetTypeName2()
            Debug.Print msgStr + msgStr2
        End If

        msgStr = "     " + "Number of SOLIDWORKS face entities in this feature: "
        msgStr2 = feature.GetFaceCount
        Debug.Print msgStr + msgStr2

        msgStr = "     " + "Number of applied features: "
        msgStr2 = feature.GetAppliedFeatureCount()
        Debug.Print msgStr + msgStr2

        appliedFeatures = feature.GetAppliedFeatures()
        If Not (IsEmpty(appliedFeatures)) Then
            For o = 0 To UBound(appliedFeatures)
                Set appliedFeature = appliedFeatures(o)
                Debug.Print "        " + "Applied feature name: " + (appliedFeature.Name)
            Next
        End If

        msgStr = "     " + "Number of applied annotations: "
        msgStr2 = feature.GetAppliedAnnotationCount()
        Debug.Print msgStr + msgStr2

        appliedAnnotations = feature.GetAppliedAnnotations()
        If Not (IsEmpty(appliedAnnotations)) Then
            For p = 0 To UBound(appliedAnnotations)
                Set appliedAnnotation = appliedAnnotations(p)
                Debug.Print "        " + "Applied annotation name: " + (appliedAnnotation.Name)
            Next
        End If

        Debug.Print "     "
    Next

    ' If you know the name of a DimXpert feature, you can get it directly using IDimXpertPart.GetFeature("name"),
    ' which can return a general IDimXpertFeature or a more specific interface on the feature

    ' Get IDimXpertIntersectCircleFeature for the Intersect Circle1 feature
    Dim iCircleFeature As IDimXpertIntersectCircleFeature
    Set iCircleFeature = swDXPart.GetFeature("Intersect Circle1")
    msgStr = iCircleFeature.Name + " is a DimXpert intersect circle feature"
    Debug.Print ""
    Debug.Print msgStr

    boolstatus = iCircleFeature.GetIntersectFeature(feature2)
    Debug.Print "Intersect feature: " + feature2.Name
```

```vb
    ' Get the nominal circle parameters
    boolstatus = iCircleFeature.GetNominalCircle(radius, x, y, z, i, j, k)
    If boolstatus Then
        msgStr = "   The nominal circle has the following parameters:"
        Debug.Print msgStr
        msgStr = "      Radius is "
        msgStr2 = radius
        Debug.Print msgStr + msgStr2
        msgStr = "      x-coordinate is "
        msgStr2 = x
        Debug.Print msgStr + msgStr2
        msgStr = "      y-coordinate is "
        msgStr2 = y
        Debug.Print msgStr + msgStr2
        msgStr = "      z-coordinate is "
        msgStr2 = z
        Debug.Print msgStr + msgStr2
        msgStr = "      i-component of pierce vector is "
        msgStr2 = i
        Debug.Print msgStr + msgStr2
        msgStr = "      j-component of pierce vector is "
        msgStr2 = j
        Debug.Print msgStr + msgStr2
        msgStr = "      k-component of pierce vector is "
        msgStr2 = k
        Debug.Print msgStr + msgStr2
    End If

     Dim plane As IDimXpertPlaneFeature
     boolstatus = iCircleFeature.GetPlaneFeature(plane)
    If boolstatus Then
        msgStr = "   The nominal circle has the following plane feature: "
        Debug.Print msgStr
        msgStr2 = plane.Name
        Debug.Print msgStr + msgStr2
    End If

    ' Get IDimXpertIntersectLineFeature for the Intersect Line1 feature
    Dim iLineFeature As IDimXpertIntersectLineFeature
    Set iLineFeature = swDXPart.GetFeature("Intersect Line1")
    msgStr = iLineFeature.Name + " is a DimXpert intersect line feature"
    Debug.Print ""
    Debug.Print msgStr

    ' Get the nominal line parameters
    boolstatus = iLineFeature.GetNominalLine(x, y, z, i, j, k)
    If boolstatus Then
        msgStr = "   The nominal line has the following parameters:"
        Debug.Print msgStr
        msgStr = "      x-coordinate is "
        msgStr2 = x
        Debug.Print msgStr + msgStr2
        msgStr = "      y-coordinate is "
        msgStr2 = y
        Debug.Print msgStr + msgStr2
        msgStr = "      z-coordinate is "
        msgStr2 = z
        Debug.Print msgStr + msgStr2
        msgStr = "      i-component of pierce vector is "
        msgStr2 = i
        Debug.Print msgStr + msgStr2
        msgStr = "      j-component of pierce vector is "
        msgStr2 = j
        Debug.Print msgStr + msgStr2
        msgStr = "      k-component of pierce vector is "
        msgStr2 = k
        Debug.Print msgStr + msgStr2
    End If

    Dim plane1 As IDimXpertPlaneFeature
    Dim plane2 As IDimXpertPlaneFeature

    boolstatus = iLineFeature.GetPlaneFeatures(plane1, plane2)
    If boolstatus Then
        msgStr = "   The nominal line has the following plane features:"
        Debug.Print msgStr
        msgStr = "      plane1 is "
        msgStr2 = plane1.Name
        Debug.Print msgStr + msgStr2
        msgStr = "      plane2 is "
        msgStr2 = plane2.Name
        Debug.Print msgStr + msgStr2

    End If

    ' Get IDimXpertIntersectPlaneFeature for the Intersect Plane1 feature
    Dim iPlaneFeature As IDimXpertIntersectPlaneFeature
    Set iPlaneFeature = swDXPart.GetFeature("Intersect Plane1")
    msgStr = iPlaneFeature.Name + " is a DimXpert intersect plane feature"
    Debug.Print ""
    Debug.Print msgStr

    ' Get the two features used to construct the intersect plane
    boolstatus = iPlaneFeature.GetFeatures(feature1, feature2)

        msgStr = "   The plane intersects the following DimXpert features:"
        Debug.Print msgStr
        msgStr = "      Feature1 is "
        msgStr2 = feature1.Name
        Debug.Print msgStr + msgStr2
        msgStr = "      Feature2 is "
        msgStr2 = feature2.Name
        Debug.Print msgStr + msgStr2

    ' Get IDimXpertIntersectPointFeature for the Intersect Point1 feature
    Dim iPointFeature As IDimXpertIntersectPointFeature
    Set iPointFeature = swDXPart.GetFeature("Intersect Point1")
    msgStr = iPointFeature.Name + " is a DimXpert intersect point feature"
    Debug.Print ""
    Debug.Print msgStr

    ' Get the nominal point
    boolstatus = iPointFeature.GetNominalPoint(x, y, z)
    If boolstatus Then
        msgStr = "   The nominal point has the following parameters:"
        Debug.Print msgStr
        msgStr = "      x-coordinate is "
        msgStr2 = x
        Debug.Print msgStr + msgStr2
        msgStr = "      y-coordinate is "
        msgStr2 = y
        Debug.Print msgStr + msgStr2
        msgStr = "      z-coordinate is "
        msgStr2 = z
        Debug.Print msgStr + msgStr2
    End If

End Sub
Public Sub GetPatternType(ByRef featureType, ByRef msgStr2)
    If (featureType = swDimXpertFeature_Plane) Then
            msgStr2 = "Plane"
    ElseIf (featureType = swDimXpertFeature_Cylinder) Then
            msgStr2 = "Cylinder"
    ElseIf (featureType = swDimXpertFeature_Cone) Then
            msgStr2 = "Cone"
    ElseIf (featureType = swDimXpertFeature_Extrude) Then
            msgStr2 = "Extrude"
    ElseIf (featureType = swDimXpertFeature_Fillet) Then
            msgStr2 = "Fillet"
    ElseIf (featureType = swDimXpertFeature_Chamfer) Then
            msgStr2 = "Chamfer"
    ElseIf (featureType = swDimXpertFeature_CompoundHole) Then
            msgStr2 = "CompoundHole"
    ElseIf (featureType = swDimXpertFeature_CompoundWidth) Then
            msgStr2 = "CompoundWidth"
    ElseIf (featureType = swDimXpertFeature_CompoundNotch) Then
            msgStr2 = "CompoundNotch"
    ElseIf (featureType = swDimXpertFeature_CompoundClosedSlot3D) Then
            msgStr2 = "CompoundClosedSlot3D"
    ElseIf (featureType = swDimXpertFeature_IntersectPoint) Then
            msgStr2 = "IntersectPoint"
    ElseIf (featureType = swDimXpertFeature_IntersectLine) Then
            msgStr2 = "IntersectLine"
    ElseIf (featureType = swDimXpertFeature_IntersectCircle) Then
            msgStr2 = "IntersectCircle"
    ElseIf (featureType = swDimXpertFeature_IntersectPlane) Then
            msgStr2 = "IntersectPlane"
    ElseIf (featureType = swDimXpertFeature_Pattern) Then
            msgStr2 = "Pattern"
    ElseIf (featureType = swDimXpertFeature_Sphere) Then
            msgStr2 = "Sphere"
    ElseIf (featureType = swDimXpertFeature_BestfitPlane) Then
            msgStr2 = "Bestfit Plane"
    ElseIf (featureType = swDimXpertFeature_Surface) Then
            msgStr2 = "Surface"
    End If

End Sub---
```

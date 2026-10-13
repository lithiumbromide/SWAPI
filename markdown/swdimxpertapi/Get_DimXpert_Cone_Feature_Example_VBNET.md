---
title: "Get DimXpert Cone Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Cone_Feature_Example_VBNET.htm"
---

# Get DimXpert Cone Feature Example (VB.NET)

This example shows how to build a part and get attributes for the DimXpert cone feature.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\shaft.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars.
' 3. Click the Auto Dimension Scheme icon in the DimXpert toolbar.
' 4. Ensure that the Cone Feature Filter is selected.
' 5. Click the green check mark to accept the settings.
' 6. Observe this DimXpert feature on the DimXpertManager tab
'    of the Management Panel: Cone1.
' 7. Open an Immediate window.
' 8. Ensure that the SolidWorks.Interop.swdimxpert.dll interop
'    is loaded (right-click project in the Project Explorer and
'    click Add Reference > .NET tab).
' 9. Step through this macro (press F8).
'
' Postconditions: Compare the output in the Immediate Window with
' the features displayed on the DimXpertManager tab of the Management Panel.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swdimxpert
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
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
            feature = features(n)
            Debug.Print("  " + "Feature name: " + (feature.Name))
            featureType = feature.Type
            Call GetPatternType(featureType, msgStr2)
            msgStr = "     Feature type "
            msgStr3 = " is suppressed on the DimXpertManager tab? "
            msgStr4 = feature.IsSuppressed()
            Debug.Print(msgStr + msgStr2 + msgStr3 + msgStr4)
            msgStr = "     " + "Model feature: "
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
        ' Get IDimXpertConeFeature for the Cone1 feature
        Dim coneFeature As IDimXpertConeFeature
        coneFeature = swDXPart.GetFeature("Cone1")
        msgStr = coneFeature.Name + " is a DimXpert feature"
        Debug.Print("")
        Debug.Print(msgStr)
        Debug.Print("")
        ' Get the nominal top plane coordinates for Cone1
        Dim x As Double
        Dim y As Double
        Dim z As Double
        Dim i As Double
        Dim j As Double
        Dim k As Double
        Dim angle As Double
        Debug.Print("Nominal top plane of Cone1")
        Debug.Print("")
        boolstatus = coneFeature.GetNominalTopPlane(x, y, z, i, j, k)
        msgStr = "X-coordinate is "
        msgStr2 = x
        Debug.Print(msgStr + msgStr2)
        msgStr = "Y-coordinate is "
        msgStr2 = y
        Debug.Print(msgStr + msgStr2)
        msgStr = "Z-coordinate is "
        msgStr2 = z
        Debug.Print(msgStr + msgStr2)
        msgStr = "I-component of unit vector is "
        msgStr2 = i
        Debug.Print(msgStr + msgStr2)
        msgStr = "J-component of unit vector is "
        msgStr2 = j
        Debug.Print(msgStr + msgStr2)
        msgStr = "K-component of unit vector is "
        msgStr2 = k
        Debug.Print(msgStr + msgStr2)
        Debug.Print("")
        ' Get the nominal bottom plane coordinates for Cone1
        Debug.Print("Nominal bottom plane of Cone1")
        Debug.Print("")
        boolstatus = coneFeature.GetNominalBottomPlane(x, y, z, i, j, k)
        msgStr = "X-coordinate is "
        msgStr2 = x
        Debug.Print(msgStr + msgStr2)
        msgStr = "Y-coordinate is "
        msgStr2 = y
        Debug.Print(msgStr + msgStr2)
        msgStr = "Z-coordinate is "
        msgStr2 = z
        Debug.Print(msgStr + msgStr2)
        msgStr = "I-component of unit vector is "
        msgStr2 = i
        Debug.Print(msgStr + msgStr2)
        msgStr = "J-component of unit vector is "
        msgStr2 = j
        Debug.Print(msgStr + msgStr2)
        msgStr = "K-component of unit vector is "
        msgStr2 = k
        Debug.Print(msgStr + msgStr2)
        Debug.Print("")
        ' Get the nominal cone angle and coordinates for Cone1
        Debug.Print("Nominal cone of Cone1")
        Debug.Print("")
        boolstatus = coneFeature.GetNominalCone(angle, x, y, z, i, j, k)
        msgStr = "Angle is "
        msgStr2 = (angle / 3.14159265358979) * 180
        msgStr3 = " degrees"
        Debug.Print(msgStr + msgStr2 + msgStr3)
        msgStr = "X-coordinate is "
        msgStr2 = x
        Debug.Print(msgStr + msgStr2)
        msgStr = "Y-coordinate is "
        msgStr2 = y
        Debug.Print(msgStr + msgStr2)
        msgStr = "Z-coordinate is "
        msgStr2 = z
        Debug.Print(msgStr + msgStr2)
        msgStr = "I-component of unit vector is "
        msgStr2 = i
        Debug.Print(msgStr + msgStr2)
        msgStr = "J-component of unit vector is "
        msgStr2 = j
        Debug.Print(msgStr + msgStr2)
        msgStr = "K-component of unit vector is "
        msgStr2 = k
        Debug.Print(msgStr + msgStr2)
        Debug.Print("")
        ' Is the cone feature for a hole or a pin?
        boolstatus = coneFeature.Inner
        msgStr = "The cone is a hole and not a pin: "
        msgStr2 = boolstatus
        Debug.Print(msgStr + msgStr2)
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

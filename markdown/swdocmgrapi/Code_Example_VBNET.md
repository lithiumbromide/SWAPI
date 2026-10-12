---
title: "DimXpert Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Code_Example_VBNET.htm"
---

# DimXpert Example (VB.NET)

This example shows how to call interfaces, methods, and properties in the SOLIDWORKS Document Manager API for parts with DimXpert features and annotations.

To learn how to build parts containing DimXpert features and annotations that work with a particular API, open the examples in the **Examples** section in the SOLIDWORKS Document Manager API topic of interest.

```vb
'-----------------------------------------------------------------------------
```

' Preconditions:

' 1. Create a part that contains DimXpert features and

' annotations (see NOTES below).

' 2. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference

' to the project:

' a. Right-click the project in Project Explorer.

' b. Click **Add Reference**.

' c. Click **Browse**.

' d. Click:

' install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll

' 3. Substitute `your_part_with_dimensions` with the path

' to the part you just created.

' 4. Substitute your_license_code with your license code.

' 5. Compile and run this program.

'

' Postconditions: Inspect the Immediate Window.

'

' **NOTES**:

' You must convert older parts to the latest supported

' version of SOLIDWORKS in order to get the DimXpert CAD identifiers

' for features and annotations using the API. To convert an older

' part to the latest supported version:

' 1. Open the part in a version of SOLIDWORKS that contains this API.

' 2. Save the part, clicking **OK** in the pop-up dialog to convert the part.

' NOTE: If you are using a tutorial part, be sure to

' save it to another name.

' 3. Close the part.

'---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports SolidWorks.Interop.swdocumentmgr

Imports System

Imports System.Diagnostics

Partial Class SolidWorksMacro

Sub Main()

Dim classfac As SwDMClassFactory

Dim docMgr As SwDMApplication

Dim swDoc As SwDMDocument5

Dim e As SwDmDocumentOpenError

classfac = CreateObject("SwDocumentMgr.SwDMClassFactory")

' Substitute your license code here:

docMgr = classfac.GetApplication("your_license_code")

Debug.Print("Latest supported file version: " & docMgr.**GetLatestSupportedFileVersion**)

Dim fileName As String

' Substitute the path to your DimXpert part here:

fileName = "`your_part_with_dimensions`"

swDoc = docMgr.**GetDocument**(fileName, SwDmDocumentType.swDmDocumentPart, True, e)

If (swDoc Is Nothing) Then

MsgBox(fileName & " not found")

Exit Sub

End If

Debug.Print(" Loaded document version: " & swDoc.**GetVersion**)

Debug.Print(" Loaded document name: " & fileName)

Debug.Print(" ")

Dim vConfigNames As Object

Dim configName As String

Dim configObj As SwDMConfiguration12

Dim index As Integer

Dim myDimXpertPart As SwDMDimXpertPart

Dim vFeatures As Object, myFeature As SwDMDimXpertFeature

Dim vAnnotations As Object, myAnnotation As SwDMDimXpertAnnotation

Dim myBlockTolerance As SwDMDimXpertBlockTolerances

Dim vObject As Object

Dim featureIndex As Integer, annoIndex As Integer, vObjectIndex As Integer

Dim tempFeature As SwDMDimXpertFeature, tempFeature1 As SwDMDimXpertFeature

Dim endFeature1 As SwDMDimXpertFeature, endFeature2 As SwDMDimXpertFeature

Dim planeFeature1 As SwDMDimXpertPlaneFeature, planeFeature2 As SwDMDimXpertPlaneFeature

Dim datum As swDmDimXpertDatum

Dim fosUsage As swDmDimXpertDistanceFosUsage_e

Dim modifier As swDmDimXpertMaterialConditionModifier_e

Dim bltType As swDmDimXpertBlockToleranceType_e

Dim X As Double, Y As Double, Z As Double

Dim i As Double, j As Double, k As Double

Dim longi As Double, longj As Double, longk As Double

Dim width As Double, length As Double, angle As Double, Distance As Double

Dim Tolerance As Double, Value As Double

Dim isMax As Boolean, Enabled As Boolean

Dim feattype As swDmDimXpertFeatureType_e, annotype As swDmDimXpertAnnotationType_e

Dim myGeoTol As SwDMDimXpertGeometricTolerance

Dim myDimTol As SwDMDimXpertDimensionTolerance

Dim myOriTol As SwDMDimXpertOrientationGeoTol

Dim plusTol As Double, minusTol As Double, lowerTol As Double, upperTol As Double

Dim boolstatus As Boolean

vConfigNames = swDoc.**ConfigurationManager**.**GetConfigurationNames**()

If Not (IsNothing(vConfigNames)) Then

For index = LBound(vConfigNames) To UBound(vConfigNames)

configName = vConfigNames(index)

configObj = swDoc.**ConfigurationManager**.**GetConfigurationByName**(configName)

If Not configObj Is Nothing Then

myDimXpertPart = configObj.DimXpertPart

If Not myDimXpertPart Is Nothing Then

vFeatures = myDimXpertPart.**GetFeatures**()

If Not (IsNothing(vFeatures)) Then

Debug.Print(" ")

Debug.Print(myDimXpertPart.**GetFeatureCount** & " DimXpert features:")

Debug.Print(" ")

For featureIndex = LBound(vFeatures) To UBound(vFeatures)

myFeature = vFeatures(featureIndex)

Debug.Print(featureIndex & " : " & "Feature name = " & myFeature.**Name**)

feattype = myFeature.**type**

Select Case feattype

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Plane

Debug.Print(" Type = Plane")

Dim myPlaneFeature As SwDMDimXpertPlaneFeature

myPlaneFeature = myFeature

boolstatus = myPlaneFeature.**GetNominalPlane**(X, Y, Z, i, j, k)

Debug.Print(" NomPlane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_BestfitPlane

Debug.Print(" Type = Best fit plane")

Dim myBestFitPlaneFeature As SwDMDimXpertBestFitPlaneFeature

myBestFitPlaneFeature = myFeature

boolstatus = myBestFitPlaneFeature.**GetNominalPlane**(X, Y, Z, i, j, k)

Debug.Print(" NominalPlane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Debug.Print(" Number of sub-features: " & myBestFitPlaneFeature.**GetSubFeatureCount**)

If myBestFitPlaneFeature.GetSubFeatureCount > 0 Then

Debug.Print(" Sub-features:")

vObject = myBestFitPlaneFeature.**GetSubFeatures**

For vObjectIndex = LBound(vObject) To UBound(vObject)

tempFeature = vObject(vObjectIndex)

Debug.Print(" " & tempFeature.**Name**)

Next vObjectIndex

End If

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Chamfer

Debug.Print(" Type = Chamfer")

Dim myChamferFeature As SwDMDimXpertChamferFeature

myChamferFeature = myFeature

Debug.Print(" Chamfer angle: " & myChamferFeature.**Angle**)

Debug.Print(" Chamfer angle type (swDmDimXpertChamferAngleType_e): " & myChamferFeature.**AngleType**)

Debug.Print(" Chamfer type (swDmDimXpertChamferType_e): " & myChamferFeature.**ChamferType**)

Debug.Print(" Distance 1: " & myChamferFeature.**Distance1**)

Debug.Print(" Distance 2: " & myChamferFeature.**Distance2**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_CompoundClosedSlot3D

Debug.Print(" Type = Compound closed slot 3D")

Dim myClosedSlotFeature As SwDMDimXpertCompoundClosedSlot3dFeature

myClosedSlotFeature = myFeature

tempFeature = myClosedSlotFeature.**GetBottomFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Bottom feature: " & tempFeature.**Name**)

End If

endFeature1 = Nothing

endFeature2 = Nothing

planeFeature1 = Nothing

planeFeature2 = Nothing

boolstatus = myClosedSlotFeature.**GetEndFeatures**(endFeature1, endFeature2)

If Not endFeature1 Is Nothing And Not endFeature2 Is Nothing Then

Debug.Print(" End features: " & endFeature1.**Name** & ", " & endFeature2.**Name**)

End If

boolstatus = myClosedSlotFeature.**GetNominalBottomPlane**(X, Y, Z, i, j, k)

Debug.Print(" Bottom plane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myClosedSlotFeature.**GetNominalClosedSlot**(width, length, X, Y, Z, i, j, k, longi, longj, longk)

Debug.Print(" Closed slot(width,length,x,j,z,i,j,k,longi,longj,longk): " & Format(width, "0.0####") & ", " & Format(length, "0.0####") & ", " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####") & ", " & Format(longi, "0.0#####") & ", " & Format(longj, "0.0#####") & ", " & Format(longk, "0.0#####"))

boolstatus = myClosedSlotFeature.**GetNominalTopPlane**(X, Y, Z, i, j, k)

Debug.Print(" Top plane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myClosedSlotFeature.**GetPlaneFeatures**(planeFeature1, planeFeature2)

If Not planeFeature1 Is Nothing And Not planeFeature2 Is Nothing Then

Debug.Print(" Plane features: " & planeFeature1.**Name** & ", " & planeFeature2.**Name**)

End If

Debug.Print(" Closed slot is blind and not through all: " & myClosedSlotFeature.**Blind**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_CompoundHole

Debug.Print(" Type = Compound hole")

Dim myHole As SwDMDimXpertCompoundHoleFeature

myHole = myFeature

Debug.Print(" Hole is blind and not through all: " & myHole.**Blind**)

Dim bottomFeature As SwDMDimXpertFeature

bottomFeature = myHole.**GetBottomFeature**()

If Not (bottomFeature Is Nothing) Then

Debug.Print(" Bottom feature type (swDmDimXpertFeatureType_e) = " & bottomFeature.**type**)

End If

Dim refFeature As SwDMDimXpertFeature

refFeature = myHole.**GetReferenceFeature**()

If Not (refFeature Is Nothing) Then

Debug.Print(" Reference feature type (swDmDimXpertFeatureType_e) = " & refFeature.**type**)

End If

If myHole.**GetSubFeatureCount** > 0 Then

vObject = myHole.**GetSubFeatures**

Debug.Print(" Sub-features: ")

For vObjectIndex = LBound(vObject) To UBound(vObject)

tempFeature = vObject(vObjectIndex)

Debug.Print(" " & tempFeature.**Name**)

Next vObjectIndex

End If

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_CompoundNotch

Debug.Print(" Type = Compound notch")

Dim myNotchFeature As SwDMDimXpertCompoundNotchFeature

myNotchFeature = myFeature

tempFeature = myNotchFeature.**GetBottomFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Bottom feature: " & tempFeature.**Name**)

End If

endFeature1 = myNotchFeature.**GetEndFeature**

If Not endFeature1 Is Nothing Then

Debug.Print(" End feature: " & endFeature1.**Name**)

End If

boolstatus = myNotchFeature.**GetNominalBottomPlane**(X, Y, Z, i, j, k)

Debug.Print(" Bottom plane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myNotchFeature.**GetNominalNotch**(width, length, X, Y, Z, i, j, k, longi, longj, longk)

Debug.Print(" Notch(width,length,x,j,z,i,j,k,longi,longj,longk): " & Format(width, "0.0####") & ", " & Format(length, "0.0####") & ", " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####") & ", " & Format(longi, "0.0#####") & ", " & Format(longj, "0.0#####") & ", " & Format(longk, "0.0#####"))

tempFeature = myNotchFeature.**GetOpenSideReferenceFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Open side reference feature: " & tempFeature.**Name**)

End If

tempFeature = myNotchFeature.**GetTopReferenceFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Top reference feature: " & tempFeature.**Name**)

End If

planeFeature1 = Nothing

planeFeature2 = Nothing

boolstatus = myNotchFeature.**GetPlaneFeatures**(planeFeature1, planeFeature2)

If Not planeFeature1 Is Nothing And Not planeFeature2 Is Nothing Then

Debug.Print(" Plane features: " & planeFeature1.**Name** & ", " & planeFeature2.**Name**)

End If

Debug.Print(" Notch is blind and not through all: " & myNotchFeature.**Blind**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_CompoundWidth

Debug.Print(" Type = Compound width")

Dim myWidthFeature As SwDMDimXpertCompoundWidthFeature

myWidthFeature = myFeature

boolstatus = myWidthFeature.**GetNominalCompoundWidth**(width, X, Y, Z, i, j, k)

Debug.Print(" Compound width(width,x,j,z,i,j,k): " & Format(width, "0.0####") & ", " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myWidthFeature.**GetNominalLongitude**(i, j, k)

Debug.Print(" Nominal longitude(longi, longj, longk): " & Format(longi, "0.0#####") & ", " & Format(longj, "0.0#####") & ", " & Format(longk, "0.0#####"))

Debug.Print(" Compound width is for a hole and not a pin: " & myWidthFeature.**Inner**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Cone

Debug.Print(" Type = Cone")

Dim myConeFeature As SwDMDimXpertConeFeature

myConeFeature = myFeature

boolstatus = myConeFeature.**GetNominalBottomPlane**(X, Y, Z, i, j, k)

Debug.Print(" Nominal bottom plane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myConeFeature.**GetNominalCone**(angle, X, Y, Z, i, j, k)

Debug.Print(" Cone(angle,x,j,z,i,j,k): " & Format(angle, "0.0####") & ", " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myConeFeature.**GetNominalTopPlane**(X, Y, Z, i, j, k)

Debug.Print(" Nominal top plane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Debug.Print(" Cone is a hole and not a pin: " & myConeFeature.**Inner**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Cylinder

Debug.Print(" Type = Cylinder")

Dim myCylinder As SwDMDimXpertCylinderFeature

myCylinder = myFeature

boolstatus = myCylinder.**GetNominalTopPlane**(X, Y, Z, i, j, k)

Debug.Print(" TopPlane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myCylinder.**GetNominalCylinder**(angle, X, Y, Z, i, j, k)

Debug.Print(" Cylinder(radius,x,j,z,i,j,k): " & Format(angle, "0.0####") & ", " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

boolstatus = myCylinder.**GetNominalBottomPlane**(X, Y, Z, i, j, k)

Debug.Print(" BottomPlane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Dim isThreaded As Boolean, threadDesignation As String, threadDepth As Double

threadDesignation = Nothing

boolstatus = myCylinder.**GetThread**(isThreaded, threadDesignation, threadDepth)

Debug.Print(" Cylinder is threaded: " & isThreaded)

If (isThreaded) Then

Debug.Print(" Cylinder thread designation: " & threadDesignation)

Debug.Print(" Cylinder thread depth: " & threadDepth)

End If

Debug.Print(" Cylinder is a hole and not a pin: " & myCylinder.**Inner**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Extrude

Debug.Print(" Type = Extrude")

Dim myExtrude As SwDMDimXpertExtrudeFeature

myExtrude = myFeature

tempFeature = myExtrude.**GetBottomFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Bottom feature: " & tempFeature.**Name**)

End If

tempFeature = myExtrude.**GetBottomBlends**

If Not tempFeature Is Nothing Then

Debug.Print(" Bottom blends: " & tempFeature.**Name**)

End If

tempFeature = myExtrude.**GetTopBlends**

If Not tempFeature Is Nothing Then

Debug.Print(" Top blends: " & tempFeature.**Name**)

End If

tempFeature = myExtrude.**GetReferenceFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Reference feature: " & tempFeature.**Name**)

End If

Debug.Print(" Number of sub-features: " & myExtrude.**GetSubFeatureCount**)

If myExtrude.**GetSubFeatureCount** > 0 Then

Debug.Print(" Sub-features:")

vObject = myExtrude.**GetSubFeatures**

For vObjectIndex = LBound(vObject) To UBound(vObject)

tempFeature = vObject(vObjectIndex)

Debug.Print(" " & tempFeature.**Name**)

Next vObjectIndex

End If

Debug.Print(" Extrude is blind and not through all: " & myExtrude.**Blind**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Fillet

Debug.Print(" Type = Fillet")

Dim myFillet As SwDMDimXpertFilletFeature

myFillet = myFeature

Debug.Print(" Fillet is for a hole and not a pin: " & myFillet.**Inner**)

Debug.Print(" Radius = " & myFillet.**Radius**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_IntersectCircle

Debug.Print(" Type = Intersect circle")

Dim myICircle As SwDMDimXpertIntersectCircleFeature

myICircle = myFeature

tempFeature = myICircle.**GetIntersectFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Intersect feature: " & tempFeature.**Name**)

End If

tempFeature = myICircle.**GetPlaneFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Plane feature: " & tempFeature.**Name**)

End If

boolstatus = myICircle.**GetNominalCircle**(angle, X, Y, Z, i, j, k)

Debug.Print(" Intersect circle(radius,x,y,z,i,j,k): " & Format(angle, "0.0####") & ", " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_IntersectLine

Debug.Print(" Type = Intersect line")

Dim myILine As SwDMDimXpertIntersectLineFeature

myILine = myFeature

tempFeature = Nothing

tempFeature1 = Nothing

boolstatus = myILine.**GetPlaneFeatures**(tempFeature, tempFeature1)

If Not tempFeature Is Nothing And Not tempFeature1 Is Nothing Then

Debug.Print(" Plane feature 1: " & tempFeature.**Name**)

Debug.Print(" Plane feature 2: " & tempFeature1.**Name**)

End If

boolstatus = myILine.**GetNominalLine**(X, Y, Z, i, j, k)

Debug.Print(" Intersect line(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_IntersectPlane

Debug.Print(" Type = Intersect plane")

Dim myIPlane As SwDMDimXpertIntersectPlaneFeature

myIPlane = myFeature

tempFeature = Nothing

tempFeature1 = Nothing

boolstatus = myIPlane.**GetFeatures**(tempFeature, tempFeature1)

If Not tempFeature Is Nothing And Not tempFeature1 Is Nothing Then

Debug.Print(" Feature 1: " & tempFeature.**Name**)

Debug.Print(" Feature 2: " & tempFeature1.**Name**)

End If

boolstatus = myIPlane.**GetNominalPlane**(X, Y, Z, i, j, k)

Debug.Print(" Intersect plane(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_IntersectPoint

Debug.Print(" Type = Intersect point")

Dim myIPoint As SwDMDimXpertIntersectPointFeature

myIPoint = myFeature

tempFeature = Nothing

tempFeature1 = Nothing

boolstatus = myIPoint.**GetFeatures**(tempFeature, tempFeature1)

If Not tempFeature Is Nothing And Not tempFeature1 Is Nothing Then

Debug.Print(" Feature 1: " & tempFeature.**Name**)

Debug.Print(" Feature 2: " & tempFeature1.**Name**)

End If

boolstatus = myIPoint.**GetNominalPoint**(X, Y, Z)

boolstatus = myIPoint.**GetNominalVector**(i, j, k)

Debug.Print(" Intersect point(x,y,z,i,j,k): " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Pattern

Debug.Print(" Type = Pattern")

Dim myPattern As SwDMDimXpertPatternFeature

myPattern = myFeature

Debug.Print(" Number of sub-features: " & myPattern.**GetSubFeatureCount**)

If myPattern.**GetSubFeatureCount** > 0 Then

Debug.Print(" Sub-features:")

vObject = myPattern.**GetSubFeatures**

For vObjectIndex = LBound(vObject) To UBound(vObject)

tempFeature = vObject(vObjectIndex)

Debug.Print(" " & tempFeature.**Name**)

Next vObjectIndex

End If

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Sphere

Debug.Print(" Type = Sphere")

Dim mySphere As SwDMDimXpertSphereFeature

mySphere = myFeature

boolstatus = mySphere.**GetNominalSphere**(angle, X, Y, Z)

Debug.Print(" Sphere(radius,x,j,z): " & Format(angle, "0.0####") & ", " & Format(X, "0.0#####") & ", " & Format(Y, "0.0#####") & ", " & Format(Z, "0.0#####"))

Debug.Print(" Sphere is for a hole and not a pin: " & mySphere.**Inner**)

Case swDmDimXpertFeatureType_e.swDmDimXpertFeature_Surface

Debug.Print(" Type = Surface")

Case Else

Debug.Print(" Type = <unknown>")

End Select

Debug.Print(" CAD identifier count = " & myFeature.**GetCadIdentifierCount**)

If myFeature.GetCadIdentifierCount > 0 Then

Debug.Print(" CAD Identifiers:")

vObject = myFeature.**GetCadIdentifiers**

For vObjectIndex = LBound(vObject) To UBound(vObject)

Debug.Print(" " & vObject(vObjectIndex))

Next vObjectIndex

End If

Debug.Print(" Suppressed = " & myFeature.**IsSuppressed**)

Debug.Print(" ")

Next featureIndex

End If

myBlockTolerance = myDimXpertPart.**GetBlockTolerances**

Debug.Print(" DimXpert block tolerance settings:")

Debug.Print(" ")

Dim linear1 As Double, linear2 As Double, linear3 As Double, angular As Double

Dim linear1Prec As Integer, linear2Prec As Integer, linear3Prec As Integer

bltType = myBlockTolerance.**type**

Select Case bltType

Case swDmDimXpertBlockToleranceType_e.swDmDimXpertBlockToleranceType_ASMEInch

boolstatus = myBlockTolerance.**GetToleranceValues**(linear1, linear1Prec, linear2, linear2Prec, linear3, linear3Prec, angular)

Debug.Print(" ASMEInch Dimension 1 tolerance: " & linear1)

Debug.Print(" ASMEInch Dimension 1 tolerance precision: " & linear1Prec)

Debug.Print(" ASMEInch Dimension 2 tolerance: " & linear2)

Debug.Print(" ASMEInch Dimension 2 tolerance precision: " & linear2Prec)

Debug.Print(" ASMEInch Dimension 3 tolerance: " & linear3)

Debug.Print(" ASMEInch Dimension 3 tolerance precision: " & linear3Prec)

Debug.Print(" ASMEInch Angular tolerance: " & angular)

Case swDmDimXpertBlockToleranceType_e.swDmDimXpertBlockToleranceType_ISO2768

Dim ISO2768Type As swDmDimXpertISO2768PartType_e

boolstatus = myBlockTolerance.**GetISO2768PartType**(ISO2768Type)

Debug.Print(" ISO 2768 part type (swDmDimXpertISO2768PartType_e): " & ISO2768Type)

Case swDmDimXpertBlockToleranceType_e.swDmDimXpertBlockToleranceType_unknown

Debug.Print(" Block tolerance unknown")

End Select

vAnnotations = myDimXpertPart.**GetAnnotations**()

If Not (IsNothing(vAnnotations)) Then

Debug.Print(" ")

Debug.Print(myDimXpertPart.**GetAnnotationCount** & " DimXpert annotations:")

Debug.Print(" ")

For annoIndex = LBound(vAnnotations) To UBound(vAnnotations)

myDimTol = Nothing

myGeoTol = Nothing

myOriTol = Nothing

myAnnotation = vAnnotations(annoIndex)

Debug.Print(annoIndex & " : " & "Annotation name = " & myAnnotation.**Name**)

annotype = myAnnotation.**type**

Select Case annotype

Case swDmDimXpertAnnotationType_e.swDmDimXpertDatum

Debug.Print(" Type = Datum")

Dim myDatum As swDmDimXpertDatum

myDatum = myAnnotation

Debug.Print(" ID = " & myDatum.**Identifier**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_AngleBetween

Debug.Print(" Type = Angle-between dimension tolerance")

Dim myAngBetDimTol As SwDMDimXpertAngleBetweenDimTol

myAngBetDimTol = myAnnotation

boolstatus = myAngBetDimTol.**GetDirectionVector**(i, j, k)

Debug.Print(" DirectionVector(i,j,k): " & i & ", " & j & ", " & k)

Debug.Print(" Feature of origin: " & myAngBetDimTol.**OriginFeature**.**Name**)

Debug.Print(" Calculate supplement angle? " & myAngBetDimTol.**Supplement**)

myDimTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_ChamferDimension

Debug.Print(" Type = Chamfer dimension tolerance")

myDimTol = myAnnotation

Dim myChamferDimTol As SwDMDimXpertChamferDimTol

myChamferDimTol = myAnnotation

Debug.Print(" Chamfer dimension type (swDmDimXpertChamferDimensionType_e): " & myChamferDimTol.**ChamferType**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_CompositeDistanceBetween

Debug.Print(" Type = Composite distance-between dimension tolerance")

myDimTol = myAnnotation

Dim myCompDistBetDimTol As SwDMDimXpertCompositeDistanceBetweenDimTol

myCompDistBetDimTol = myAnnotation

boolstatus = myCompDistBetDimTol.**GetDirectionVector**(i, j, k)

Debug.Print(" Direction vector(i,j,k): " & i & ", " & j & ", " & k)

tempFeature1 = Nothing

boolstatus = myCompDistBetDimTol.**GetFeature**(tempFeature1, fosUsage)

If Not tempFeature1 Is Nothing Then

Debug.Print(" Composite distance-between dimension tolerance feature: " & tempFeature1.**Name**)

Debug.Print(" Feature of size usage (swDmDimXpertDistanceFosUsage_e): " & fosUsage)

End If

boolstatus = myCompDistBetDimTol.**GetIntraFeature**(tempFeature1, fosUsage)

If Not tempFeature1 Is Nothing Then

Debug.Print(" Feature-locating feature: " & tempFeature1.**Name**)

Debug.Print(" Feature of size usage for feature-locating(swDmDimXpertDistanceFosUsage_e): " & fosUsage)

End If

boolstatus = myCompDistBetDimTol.**GetOriginFeature**(tempFeature1, fosUsage)

If Not tempFeature1 Is Nothing Then

Debug.Print(" Feature of origin for this dimension tolerance: " & tempFeature1.**Name**)

Debug.Print(" Feature of size usage (swDmDimXpertDistanceFosUsage_e): " & fosUsage)

End If

Debug.Print(" Type of dimension tolerance for feature-locating (swDmDimXpertDimensionToleranceType_e): " & myCompDistBetDimTol.**DimensionTypeIntraFeature**)

Debug.Print(" Tolerance for feature-locating: " & myCompDistBetDimTol.**GetNominalValueIntraFeature**)

boolstatus = myCompDistBetDimTol.**GetPlusAndMinusToleranceIntraFeature**(plusTol, minusTol)

Debug.Print(" Plus / Minus limit for feature-locating: " & plusTol & " / " & minusTol)

boolstatus = myCompDistBetDimTol.**GetUpperAndLowerLimitIntraFeature**(upperTol, lowerTol)

Debug.Print(" Upper / Lower limit for feature-locating: " & upperTol & " / " & lowerTol)

Debug.Print(" Block tolerance precision for feature-locating: " & myCompDistBetDimTol.**BlockToleranceDecimalPlacesIntraFeature**)

Debug.Print(" Limits and fits code for feature-locating: " & myCompDistBetDimTol.**LimitsAndFitsCodeIntraFeature**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_ConeAngle

Debug.Print(" Type = Cone angle dimension tolerance")

myDimTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_CounterBore

Debug.Print(" Type = Counterbore dimension tolerance")

myDimTol = myAnnotation

Dim myCounterBoreDimTol As SwDMDimXpertCounterBoreDimTol

myCounterBoreDimTol = myAnnotation

tempFeature = myCounterBoreDimTol.**ReferenceFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Reference Feature for this dimension tolerance: " & tempFeature.**Name**)

End If

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_CounterSinkAngle

Debug.Print(" Type = Countersink angle dimension tolerance")

myDimTol = myAnnotation

Dim myCounterSinkAngleDimTol As SwDMDimXpertCounterSinkAngleDimTol

myCounterSinkAngleDimTol = myAnnotation

tempFeature = myCounterSinkAngleDimTol.**ReferenceFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Reference Feature for this dimension tolerance: " & tempFeature.**Name**)

End If

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_CounterSinkDiameter

Debug.Print(" Type = Countersink diameter dimension tolerance")

myDimTol = myAnnotation

Dim myCounterSinkDiameterDimTol As SwDMDimXpertCounterSinkDiameterDimTol

myCounterSinkDiameterDimTol = myAnnotation

tempFeature = myCounterSinkDiameterDimTol.**ReferenceFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Reference Feature for this dimension tolerance: " & tempFeature.**Name**)

End If

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_Depth

Debug.Print(" Type = Depth dimension tolerance")

myDimTol = myAnnotation

Dim myDepthDimTol As SwDMDimXpertDepthDimTol

myDepthDimTol = myAnnotation

Debug.Print(" Tolerance is for thread depth: " & myDepthDimTol.**IsThreadDepth**)

tempFeature = myDepthDimTol.**ReferenceFeature**

If Not tempFeature Is Nothing Then

Debug.Print(" Reference Feature for this dimension tolerance: " & tempFeature.**Name**)

End If

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_Diameter

Debug.Print(" Type = Diameter dimension tolerance")

myDimTol = myAnnotation

Dim myDiameterDimTol As SwDMDimXpertDiameterDimTol

myDiameterDimTol = myAnnotation

Debug.Print(" Pattern treatment type (swDmDimXpertPatternTreatmentType_e): " & myDiameterDimTol.**PatternTreatment**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_DistanceBetween

Debug.Print(" Type = Distance-between dimension tolerance")

myDimTol = myAnnotation

Dim myDistBetDimTol As SwDMDimXpertDistanceBetweenDimTol

myDistBetDimTol = myAnnotation

boolstatus = myDistBetDimTol.**GetDirectionVector**(i, j, k)

Debug.Print(" Direction vector(i,j,k): " & i & ", " & j & ", " & k)

tempFeature1 = Nothing

boolstatus = myDistBetDimTol.GetFeature(tempFeature1, fosUsage)

If Not tempFeature1 Is Nothing Then

Debug.Print(" Distance-between dimension tolerance feature: " & tempFeature1.**Name**)

Debug.Print(" Feature of size usage (swDmDimXpertDistanceFosUsage_e): " & fosUsage)

End If

boolstatus = myDistBetDimTol.GetOriginFeature(tempFeature1, fosUsage)

If Not tempFeature1 Is Nothing Then

Debug.Print(" Feature of origin for this dimension tolerance: " & tempFeature1.**Name**)

Debug.Print(" Feature of size usage(swDmDimXpertDistanceFosUsage_e): " & fosUsage)

End If

Debug.Print(" Pattern treatment type (swDmDimXpertPatternTreatmentType_e): " & myDistBetDimTol.**PatternTreatment**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_Length

Debug.Print(" Type = Length dimension tolerance")

myDimTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_Radius

Debug.Print(" Type = Radius dimension tolerance")

myDimTol = myAnnotation

Dim myRadiusDimTol As SwDMDimXpertRadiusDimTol

myRadiusDimTol = myAnnotation

Debug.Print(" Pattern treatment type (swDmDimXpertPatternTreatmentType_e): " & myRadiusDimTol.**PatternTreatment**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertDimTol_Width

Debug.Print(" Type = Width dimension tolerance")

myDimTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Angularity

Debug.Print(" " & annoIndex & " : Type = Angularity geometric tolerance")

myGeoTol = myAnnotation

myOriTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Circularity

Debug.Print(" Type = Circularity geometric tolerance")

myGeoTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_CircularRunout

Debug.Print(" Type = Circular runout geometric tolerance")

myGeoTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_CompositeLineProfile

Debug.Print(" Type = Composite line profile geometric tolerance")

myGeoTol = myAnnotation

Dim myCompLineProfileGeoTol As SwDMDimXpertCompositeLineProfileGeoTol

myCompLineProfileGeoTol = myAnnotation

boolstatus = myCompLineProfileGeoTol.**GetPlanarZoneVector**(i, j, k)

Debug.Print(" Planar zone vector(i,j,k): " & i & ", " & j & ", " & k)

Debug.Print(" Outer tolerance value: " & myCompLineProfileGeoTol.**OuterToleranceValue**)

Debug.Print(" Outer tolerance value in the lower tier: " & myCompLineProfileGeoTol.**OuterToleranceValueLowerTier**)

Debug.Print(" Primary datum repeated in lower tier: " & myCompLineProfileGeoTol.**PrimaryInLowerTier**)

Debug.Print(" Secondary datum repeated in lower tier: " & myCompLineProfileGeoTol.**SecondaryInLowerTier**)

Debug.Print(" Tertiary datum repeated in lower tier: " & myCompLineProfileGeoTol.**TertiaryInLowerTier**)

Debug.Print(" Tolerance in lower tier: " & myCompLineProfileGeoTol.**ToleranceLowerTier**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_CompositePosition

Debug.Print(" Type = Composite position geometric tolerance")

myGeoTol = myAnnotation

Dim myCompPosGeoTol As SwDMDimXpertCompositePositionGeoTol

myCompPosGeoTol = myAnnotation

boolstatus = myCompPosGeoTol.**GetMaxTolerance**(isMax, Tolerance)

Debug.Print(" Maximum tolerance is set: " & isMax)

If isMax Then

Debug.Print(" Maximum tolerance: " & Tolerance)

End If

boolstatus = myCompPosGeoTol.**GetMaxToleranceLowerTier**(isMax, Tolerance)

Debug.Print(" Maximum tolerance is set in lower tier: " & isMax)

If isMax Then

Debug.Print(" Maximum tolerance in lower tier: " & Tolerance)

End If

boolstatus = myCompPosGeoTol.**GetPlanarZoneVector**(i, j, k)

Debug.Print(" Planar zone vector(i,j,k): " & i & ", " & j & ", " & k)

boolstatus = myCompPosGeoTol.**GetProjectedZone**(Enabled, Value)

Debug.Print(" Projected zone is in force: " & Enabled)

If Enabled Then

Debug.Print("Value: " & Value)

End If

Debug.Print(" Material condition modifier (swDmDimXpertMaterialConditionModifier_e): " & myCompPosGeoTol.**Modifier**)

Debug.Print(" Material condition modifier in lower tier (swDmDimXpertMaterialConditionModifier_e): " & myCompPosGeoTol.ModifierLowerTier)

Debug.Print(" Primary datum repeated in lower tier: " & myCompPosGeoTol.**PrimaryInLowerTier**)

Debug.Print(" Secondary datum repeated in lower tier: " & myCompPosGeoTol.**SecondaryInLowerTier**)

Debug.Print(" Tertiary datum repeated in lower tier: " & myCompPosGeoTol.**TertiaryInLowerTier**)

Debug.Print(" Tolerance in lower tier: " & myCompPosGeoTol.**ToleranceLowerTier**)

Debug.Print(" Position zone type (swDmDimXpertPositionZoneType_e): " & myCompPosGeoTol.**ZoneType**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_CompositeSurfaceProfile

Debug.Print(" Type = Composite surface profile geometric tolerance")

myGeoTol = myAnnotation

Dim myCompSurfProfGeoTol As SwDMDimXpertCompositeSurfaceProfileGeoTol

myCompSurfProfGeoTol = myAnnotation

Debug.Print(" Outer tolerance: " & myCompSurfProfGeoTol.**OuterToleranceValue**)

Debug.Print(" Outer tolerance in lower tier: " & myCompSurfProfGeoTol.**OuterToleranceValueLowerTier**)

Debug.Print(" Primary datum repeated in lower tier: " & myCompSurfProfGeoTol.**PrimaryInLowerTier**)

Debug.Print(" Secondary datum repeated in lower tier: " & myCompSurfProfGeoTol.**SecondaryInLowerTier**)

Debug.Print(" Tertiary datum repeated in lower tier: " & myCompSurfProfGeoTol.**TertiaryInLowerTier**)

Debug.Print(" Tolerance in lower tier: " & myCompSurfProfGeoTol.**ToleranceLowerTier**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Concentricity

Debug.Print(" Type = Concentricity geometric tolerance")

myGeoTol = myAnnotation

Dim myConcentricityGeoTol As SwDMDimXpertConcentricityGeoTol

myConcentricityGeoTol = myAnnotation

boolstatus = myConcentricityGeoTol.**GetMaxTolerance**(isMax, Tolerance)

Debug.Print(" Maximum tolerance is set: " & isMax)

If isMax Then

Debug.Print(" Maximum tolerance: " & Tolerance)

End If

Debug.Print(" Material condition modifier (swDmDimXpertMaterialConditionModifier_e): " & myConcentricityGeoTol.**Modifier**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Cylindricity

Debug.Print(" Type = Cylindricity geometric tolerance")

myGeoTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Flatness

Debug.Print(" Type = Flatness geometric tolerance")

myGeoTol = myAnnotation

Dim myFlatnessGeoTol As SwDMDimXpertFlatnessGeoTol

myFlatnessGeoTol = myAnnotation

boolstatus = myFlatnessGeoTol.**GetPerUnitArea**(Enabled, length, width, i, j, k)

Debug.Print(" Per unit area(enabled,width,length,i,j,k): " & Enabled & ", " & Format(length, "0.0####") & ", " & Format(width, "0.0####") & ", " & Format(i, "0.0#####") & ", " & Format(j, "0.0#####") & ", " & Format(k, "0.0#####"))

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_LineProfile

Debug.Print(" Type = Line profile geometric tolerance")

myGeoTol = myAnnotation

Dim myLineProfileGeoTol As SwDMDimXpertLineProfileGeoTol

myLineProfileGeoTol = myAnnotation

boolstatus = myLineProfileGeoTol.**GetPlanarZoneVector**(i, j, k)

Debug.Print(" Planar zone vector(i,j,k): " & i & ", " & j & ", " & k)

Debug.Print(" Outer tolerance value: " & myLineProfileGeoTol.**OuterToleranceValue**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Parallelism

Debug.Print(" Type = Parallelism geometric tolerance")

myGeoTol = myAnnotation

myOriTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Perpendicularity

Debug.Print(" Type = Perpendicularity geometric tolerance")

myGeoTol = myAnnotation

myOriTol = myAnnotation

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Position

Debug.Print(" Type = Position geometric tolerance")

myGeoTol = myAnnotation

Dim myPosGeoTol As SwDMDimXpertPositionGeoTol

myPosGeoTol = myAnnotation

boolstatus = myPosGeoTol.**GetMaxTolerance**(isMax, Tolerance)

Debug.Print(" Maximum tolerance is set: " & isMax)

If isMax Then

Debug.Print(" Maximum tolerance: " & Tolerance)

End If

boolstatus = myPosGeoTol.**GetPlanarZoneVector**(i, j, k)

Debug.Print(" Planar zone vector(i,j,k): " & i & ", " & j & ", " & k)

boolstatus = myPosGeoTol.**GetProjectedZone**(Enabled, Value)

Debug.Print(" Projected zone is in force: " & Enabled)

If Enabled Then

Debug.Print(" Value: " & Value)

End If

Debug.Print(" Material condition modifier (swDmDimXpertMaterialConditionModifier_e): " & myPosGeoTol.**Modifier**)

Debug.Print(" Position zone type (swDmDimXpertPositionZoneType_e): " & myPosGeoTol.**ZoneType**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Straightness

Debug.Print(" Type = Straightness geometric tolerance")

myGeoTol = myAnnotation

Dim myStraightnessGeoTol As SwDMDimXpertStraightnessGeoTol

myStraightnessGeoTol = myAnnotation

boolstatus = myStraightnessGeoTol.**GetMaxTolerance**(isMax, Tolerance)

Debug.Print(" Maximum tolerance is set: " & isMax)

If isMax Then

Debug.Print(" Maximum tolerance: " & Tolerance)

End If

boolstatus = myStraightnessGeoTol.**GetPerUnitLength**(Enabled, Distance)

Debug.Print(" Per unit length(enabled,distance): " & Enabled & ", " & Format(Distance, "0.0####"))

boolstatus = myStraightnessGeoTol.**GetPlanarZoneVector**(i, j, k)

Debug.Print(" Planar zone vector(i,j,k): " & i & ", " & j & ", " & k)

Debug.Print(" Material condition modifier (swDmDimXpertMaterialConditionModifier_e): " & myStraightnessGeoTol.**Modifier**)

Debug.Print(" Position zone type (swDmDimXpertStraightnessZoneType_e): " & myStraightnessGeoTol.**ZoneType**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_SurfaceProfile

Debug.Print(" Type = SurfaceProfile geometric tolerance")

myGeoTol = myAnnotation

Dim mySurfProfGeoTol As SwDMDimXpertSurfaceProfileGeoTol

mySurfProfGeoTol = myAnnotation

Debug.Print(" Outer tolerance: " & mySurfProfGeoTol.**OuterToleranceValue**)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Symmetry

Debug.Print(" Type = Symmetry geometric tolerance")

myGeoTol = myAnnotation

Dim mySymmetryGeoTol As SwDMDimXpertSymmetryGeoTol

mySymmetryGeoTol = myAnnotation

boolstatus = mySymmetryGeoTol.**GetMaxTolerance**(isMax, Tolerance)

Debug.Print(" Maximum tolerance is set: " & isMax)

Debug.Print(" Maximum tolerance: " & Tolerance)

boolstatus = mySymmetryGeoTol.**GetZoneDirection**(i, j, k)

Debug.Print(" Zone direction(i,j,k): " & i & ", " & j & ", " & k)

modifier = mySymmetryGeoTol.**Modifier**

Debug.Print(" Modifier (swDmDimXpertMaterialConditionModifier_e): " & modifier)

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_Tangency

Debug.Print(" Type = Tangency geometric tolerance")

Dim myTangencyGeoTol As SwDMDimXpertTangencyGeoTol

myTangencyGeoTol = myAnnotation

tempFeature = Nothing

boolstatus = myTangencyGeoTol.**GetOriginFeature**(tempFeature)

If Not tempFeature Is Nothing Then

Debug.Print(" Feature of origin for this geometric tolerance: " & tempFeature.**Name**)

End If

Case swDmDimXpertAnnotationType_e.swDmDimXpertGeoTol_TotalRunout

Debug.Print(" Type = Total runout geometric tolerance")

myGeoTol = myAnnotation

Case Else

Debug.Print(" Type = <unknown>")

End Select

' Annotation Information

Debug.Print(" Annotation Information:")

Debug.Print(" CAD identifier count = " & myAnnotation.**GetCadIdentifierCount**)

If myAnnotation.**GetCadIdentifierCount** > 0 Then

Debug.Print(" CAD Identifiers:")

vObject = myAnnotation.GetCadIdentifiers

For vObjectIndex = LBound(vObject) To UBound(vObject)

Debug.Print(" " & vObject(vObjectIndex))

Next vObjectIndex

End If

Debug.Print(" Free state = " & myAnnotation.**IsFreeState**)

Debug.Print(" Statistical = " & myAnnotation.**IsStatistical**)

Debug.Print(" Suppressed = " & myAnnotation.**IsSuppressed**)

Debug.Print(" To be inspected = " & myAnnotation.**IsToBeInspected**)

If (myAnnotation.**Feature** Is Nothing) Then

Debug.Print(" Is not associated with a feature")

Else

Debug.Print(" Is associated with a feature")

End If

' Geometric Tolerance Information for Orientation Dimensions

If Not myOriTol Is Nothing Then

Debug.Print(" Orientation Geometric Tolerance Information:")

boolstatus = myOriTol.**GetMaxTolerance**(isMax, Tolerance)

Debug.Print(" Maximum tolerance is set: " & isMax)

If isMax Then

Debug.Print(" Maximum tolerance: " & Tolerance)

End If

boolstatus = myOriTol.**GetPlanarZoneVector**(i, j, k)

Debug.Print(" Planar zone vector(i,j,k): " & i & ", " & j & ", " & k)

boolstatus = myOriTol.**GetProjectedZone**(Enabled, Value)

Debug.Print(" Projected zone is in force: " & Enabled)

If Enabled Then

Debug.Print("Value: " & Value)

End If

Debug.Print(" Material condition modifier (swDmDimXpertMaterialConditionModifier_e): " & myOriTol.**Modifier**)

Debug.Print(" Position zone type (swDmDimXpertOrientationZoneType_e): " & myOriTol.**ZoneType**)

End If

' Geometric Tolerance Information

If Not myGeoTol Is Nothing Then

Debug.Print(" Geometric Tolerance Information:")

Debug.Print(" Number of primary datums: " & myGeoTol.**GetPrimaryDatumCount**)

If myGeoTol.**GetPrimaryDatumCount** > 0 Then

Debug.Print(" Primary Datum modifiers:")

vObject = myGeoTol.**GetPrimaryDatumModifiers**

For vObjectIndex = LBound(vObject) To UBound(vObject)

modifier = vObject(vObjectIndex)

Debug.Print(" Primary datum modifier (swDmDimXpertMaterialConditionModifier_e): " & modifier)

Next vObjectIndex

Debug.Print(" Primary datums:")

vObject = myGeoTol.**GetPrimaryDatums**

For vObjectIndex = LBound(vObject) To UBound(vObject)

datum = vObject(vObjectIndex)

Debug.Print(" Primary datum : " & datum.**Identifier**)

Next vObjectIndex

End If

Debug.Print(" Number of secondary datums: " & myGeoTol.**GetSecondaryDatumCount**)

If myGeoTol.**GetSecondaryDatumCount** > 0 Then

Debug.Print(" Secondary Datum modifiers:")

vObject = myGeoTol.**GetSecondaryDatumModifiers**

For vObjectIndex = LBound(vObject) To UBound(vObject)

modifier = vObject(vObjectIndex)

Debug.Print(" Secondary datum modifier (swDmDimXpertMaterialConditionModifier_e): " & modifier)

Next vObjectIndex

Debug.Print(" Secondary datums:")

vObject = myGeoTol.**GetSecondaryDatums**

For vObjectIndex = LBound(vObject) To UBound(vObject)

datum = vObject(vObjectIndex)

Debug.Print(" Secondary datum : " & datum.**Identifier**)

Next vObjectIndex

End If

Debug.Print(" Number of tertiary datums: " & myGeoTol.**GetTertiaryDatumCount**)

If myGeoTol.**GetTertiaryDatumCount** > 0 Then

Debug.Print(" Tertiary Datum modifiers:")

vObject = myGeoTol.**GetTertiaryDatumModifiers**

For vObjectIndex = LBound(vObject) To UBound(vObject)

modifier = vObject(vObjectIndex)

Debug.Print(" Tertiary datum modifier (swDmDimXpertMaterialConditionModifier_e): " & modifier)

Next vObjectIndex

Debug.Print(" Tertiary datums:")

vObject = myGeoTol.**GetTertiaryDatums**

For vObjectIndex = LBound(vObject) To UBound(vObject)

datum = vObject(vObjectIndex)

Debug.Print(" Tertiary datum : " & datum.**Identifier**)

Next vObjectIndex

End If

Debug.Print(" Geometric Tolerance = " & myGeoTol.**Tolerance**)

End If

' Dimension Tolerance Information

If Not myDimTol Is Nothing Then

Debug.Print(" Dimension Tolerance Information:")

Debug.Print(" Dimension tolerance type (swDmDimXpertDimensionToleranceType_e)= " & myDimTol.**DimensionType**)

Debug.Print(" Dimension tolerance = " & myDimTol.**GetNominalValue**())

boolstatus = myDimTol.**GetPlusAndMinusTolerance**(plusTol, minusTol)

Debug.Print(" Plus / Minus " & plusTol & " / " & minusTol)

boolstatus = myDimTol.**GetUpperAndLowerLimit**(upperTol, lowerTol)

Debug.Print(" Upper / Lower " & upperTol & " / " & lowerTol)

Debug.Print(" Block tolerance precision = " & myDimTol.**BlockToleranceDecimalPlaces**)

Debug.Print(" Limits and fits code = " & myDimTol.**LimitsAndFitsCode**)

End If

Debug.Print(" ")

Next annoIndex

End If

End If

End If

Next index

End If

End Sub

Public swApp As SldWorks

End Class

---
title: "Add Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Components_Example_VBNET.htm"
---

# Add Components Example (VB.NET)

This example shows how to add multiple components to an assembly.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a new part document.
 '    a. Extrude a rectangular block and cut-extrude a diagonal section
'        off one face of the block.
 '    b. Click Insert > Reference Geometry > Coordinate System.
 '    c. Select a corner of the block for the origin of the new coordinate system.
 '    d. Select an edge for the Z axis of the coordinate system.
 '    e. Click the green check mark to save the coordinate system.
 '       Coordinate System1 appears in the FeatureManager design tree.
 '    f. Save and minimize the part.
 ' 2. Replace <component_name> in the code with the full path name of
'      the new part.
 ' 3. Create a new assembly document.
 '    a. Create a line segment sketch originating at some distance
'       from the default origin of the assembly document.
 '    b. Click Insert > Reference Geometry > Coordinate System.
 '    c. Select one end point of the line segment for the origin of
'       the new coordinate system.
 '    d. Select the line segment for the X axis of the coordinate system.
 '    e. Click the green check mark to save the coordinate system.
 '       Coordinate System1 appears in the FeatureManager design tree.
 '    f. Right-click on Coordinate System1 in the FeatureManager design tree,
'       select Feature Properties, and rename the coordinate system
'       and its description to differ from Coordinate System1.
 '    g. Save the assembly.
 ' 4. Open an Immediate window.
 ' 5. Activate the assembly document.
 '
 ' Postconditions:
 ' Component part is inserted into the assembly such that
 ' the part's Coordinate System1 is coincident (no translation or rotation)
 ' with the assembly's default (not user-defined) coordinate system.
 '---------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Dim assemb As Object
     Dim compNames(0) As String
     Dim compXforms(15) As Double
     Dim compCoordSysNames(0) As String
     Dim vcompNames As Object
     Dim vcompXforms As Object
     Dim vcompCoordSysNames As Object
     Dim vcomponents As Object

     Sub main()

         assemb = swApp.ActiveDoc

         If (Not assemb Is  Nothing)  Then

             compNames(0) = "<component_name>"

             ' Define the transformation matrix for the component. See the IMathTransform API documentation.

             ' Add a rotational diagonal unit matrix to the transformation matrix (zero rotation)
             compXforms(0) = 1.0
             compXforms(1) = 0.0
             compXforms(2) = 0.0
             compXforms(3) = 0.0
             compXforms(4) = 1.0
             compXforms(5) = 0.0
             compXforms(6) = 0.0
             compXforms(7) = 0.0
             compXforms(8) = 1.0

             ' Add a translation vector to the transformation matrix (zero translation)
             compXforms(9) = 0.0
             compXforms(10) = 0.0
             compXforms(11) = 0.0

             ' Add a scaling factor to the transformation matrix
             compXforms(12) = 0.0
            ' The last three elements of the transformation matrix are unused

             ' Add a coordinate system name assigned to each component
             compCoordSysNames(0) =  "Coordinate System1"

             ' Add the components to the assembly.
             vcompNames = compNames
             vcompXforms = compXforms
             'vcompXforms = Nothing  ' you can also pass a null transform to achieve zero rotation and translation
             vcompCoordSysNames = compCoordSysNames
             vcomponents = assemb.AddComponents3((vcompNames), (vcompXforms), (vcompCoordSysNames))

         End If

     End Sub

     Public swApp As SldWorks

 End  Class
```

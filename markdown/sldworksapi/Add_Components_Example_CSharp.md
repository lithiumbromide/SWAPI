---
title: "Add Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Components_Example_CSharp.htm"
---

# Add Components Example (C#)

This example shows how to add multiple components to an assembly.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Create a new part document.
 //    a. Extrude a rectangular block and cut-extrude a diagonal section
 //       off one face of the block.
 //    b. Click Insert > Reference Geometry > Coordinate System.
 //    c. Select a corner of the block for the origin of
 //       the new coordinate system.
 //    d. Select an edge for the Z axis of the coordinate system.
 //    e. Click the green check mark to save the coordinate system.
 //        Coordinate System1 appears in the FeatureManager design tree.
 //    f. Save and minimize the part.
 // 2. Replace part_path in the code with the full path name
 //     of the new part.
 // 3. Create a new assembly document.
 //    a. Create a line segment sketch originating at some distance
 //       from the default origin of the assembly document.
 //    b. Click Insert > Reference Geometry > Coordinate System.
 //    c. Select one end point of the line segment for the origin of
 //       the new coordinate system.
 //    d. Select the line segment for the X axis of the coordinate system.
 //    e. Click the green check mark to save the coordinate system.
 //       Coordinate System1 appears in the FeatureManager design tree.
 //    f. Right-click on Coordinate System1 in the FeatureManager design tree,
 //       select Feature Properties, and rename the coordinate system
 //       and its description to differ from Coordinate System1.
 //    g. Save the assembly and keep it open.
 // 4. Change the namespace to match your project's name.
 //
 // Postconditions:
 // Component part is inserted into the assembly such that
 // the part's Coordinate System1 is coincident (no translation or rotation)
 // with the assembly's default (not user-defined) coordinate system.
 //
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace AddComponents3_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         AssemblyDoc assemb;
         string[] compNames = new string[1];
         double[] compXforms = new double[16];
         string[] compCoordSysNames = new string[1];
         object vcompNames;
         object vcompXforms;
         object vcompCoordSysNames;
         object vcomponents;

         public void Main()
         {
             assemb = (AssemblyDoc)swApp.ActiveDoc;

             if (((assemb != null)))
             {
                 compNames[0] = "part_path";

                 // Define the transformation matrix. See the IMathTransform API documentation.

                 // Add a rotational diagonal unit matrix (zero rotation) to the transform
                 // x-axis components of rotation
                 compXforms[0] = 1.0;
                 compXforms[1] = 0.0;
                 compXforms[2] = 0.0;
                 // y-axis components of rotation
                 compXforms[3] = 0.0;
                 compXforms[4] = 1.0;
                 compXforms[5] = 0.0;
                 // z-axis components of rotation
                 compXforms[6] = 0.0;
                 compXforms[7] = 0.0;
                 compXforms[8] = 1.0;

                 // Add a translation vector to the transform (zero translation)
                 compXforms[9] = 0.0;
                 compXforms[10] = 0.0;
                 compXforms[11] = 0.0;

                 // Add a scaling factor to the transform
                 compXforms[12] = 0.0;

                 // The last three elements in the transformation matrix are unused

                 // Register the coordinate system name for the component
                 compCoordSysNames[0] = "Coordinate System1";

                 // Add the components to the assembly.
                 vcompNames = compNames;
                 vcompXforms = compXforms;
                 //vcompXforms = Nothing   //also achieves zero rotation and translation of the component
                 vcompCoordSysNames = compCoordSysNames;

                 vcomponents = assemb.AddComponents3((vcompNames), (vcompXforms), (vcompCoordSysNames));

             }
         }

         public SldWorks swApp;

     }
 }
```

---
title: "Get DimXpert Intersect Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Intersect_Features_Example_CSharp.htm"
---

# Get DimXpert Intersect Features Example (C#)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert features:

* Intersect Point

* Intersect Line

* Intersect Circle

* Intersect Plane

```vb
 //--------------------------------------------------------------------------
// 1. Open public_documents\samples\tutorial\api\face_plate_ads_geo.sldprt.
// 2. Open the DimXpert toolbar from View > Toolbars
//    (select the first instance of Toolbars on the View menu).
// 3. Create a DimXpert Intersect Point Feature:
//    a. Click Location Dimension on the DimXpert toolbar.
//    b. Select the front face of the part.
//    c. Click Create Intersection Point on the DimXpert pop-up menu.
//    d. Select a cylinder whose axis intersects the first face at a point.
//    e. Click the green check mark in the pop-up menu to create the
//       intersect point.
//    f. Select a feature on the part to dimension against the intersect point.
//    g. Click outside the part to position the dimension in the view.
//    h. Observe the new DimXpert feature on the DimXpertManager tab:
//       Intersect Point1
// 4. Create a DimXpert Intersect Line Feature:
//    a. Click Location Dimension on the DimXpert toolbar.
//    b. Select the front face of the part.
//    c. Click Create Intersection Line on the DimXpert pop-up menu.
//    d. Select a perpendicular plane that would intersect the first plane
//       if extended (e.g., a top or side face of the part)
//    e. Click the green check mark in the pop-up menu to create the
//       intersect line.
//    f. Select a feature on the part to dimension against the intersect line.
//    g. Click outside the part to position the dimension in the view.
//    h. Observe the new DimXpert feature on the DimXpertManager tab:
//        Intersect Line1
// 5. Create a DimXpert Intersect Circle Feature:
//    a. Click Size Dimension on the DimXpert toolbar.
//    b. Select the front face of the part.
//    c. Click Intersect Circle on the DimXpert pop-up menu.
//    d. Select the opening conical surface of a flat head machine screw
//       (LPattern1 or LPattern3) in the part.
//    e. Click the green check mark in the pop-up menu to finish the dimension.
//    f. Click outside the part to position the size dimension in the view.
//    g. Observe the new DimXpert feature on the DimXpertManager tab:
//       Intersect Circle1
// 6. Create a DimXpert Intersect Plane Feature:
//    a. Click Location Dimension on the DimXpert toolbar.
//    b. Zoom in on a flat head machine screw (LPattern1 or LPattern3).
//    c. Select the opening conical surface of a flat head machine screw
//       in the part.
//    d. Click Intersect Plane on the DimXpert pop-up menu.
//    e. Select the inner cylindrical bore face of the flat head machine screw.
//    f. Click the green check mark in the pop-up menu to create the
//       intersect plane.
//    g. Select the top face of one of the extruded entities.
//    h. Click outside the part to position the location dimension in the view.
//    i. Observe the new DimXpert feature on the DimXpertManager tab:
//       Intersect Plane1
// 7. Close the part, saving it to another name.
//    NOTE: Because this part is used in a SOLIDWORKS online tutorial,
//          do not save any changes to the original file name.
// 8. Read how to load and run Code_Example_CSharp with this part.
 //---------------------------------------------------------------------------
```

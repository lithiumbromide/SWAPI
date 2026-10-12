---
title: "Get DimXpert Features and Annotations in a Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm"
---

# Get DimXpert Features and Annotations in a Model Example (C#)

This application shows you how to get all of the DimXpert feature and annotation objects in a model.

This application is more advanced than other examples, because it involves multiple class modules.

```vb
 //--------------------------------------------------------------------------
// Preconditions:
// 1. Create a new C# macro using SOLIDWORKS VSTA.
// 2. Name the project DimXpert_text_v2_cs.
// 3. Save the project.
// 4. Copy and paste the Main module into the code window.
// 5. Right-click on the project in Project Explorer and click Add > Class.
// 6. Select the Class template and type DimXpertFeatureData.cs
//    in the Name field.
// 7. Click Add.
// 8. Copy and paste the DimXpertFeatureData class module into the code window.
// 9. Right-click on the project in Project Explorer and click Add > Class.
// 10. Select the Class template and type DimXpertAnnotationData.cs
//     in the Name field.
// 11. Click Add.
// 12. Copy and paste the DimXpertAnnotationData class module
//     into the code window.
// 13. Ensure that the latest SolidWorks.Interop.swdimxpert.dll interop assembly
//     is loaded (right-click on the project in Project Explorer,
//     click Add Reference, choose the DimXpert assembly on the .NET tab).
// 14. Ensure that the Microsoft Scripting Runtime library is loaded
//     (right-click on the project in Project Explorer, click Add Reference,
//      choose the library on the COM tab).
// 15. Open a part that contains DimXpert features and/or annotations.
//     (You may want to go through the online DimXpert Tutorial
//      to learn how to create DimXpert features and annotations.
//      From the ? help menu, click SOLIDWORKS Tutorials > All SOLIDWORKS
//      Tutorials (Set 1) > DimXpert Tutorials)
// 16. Open an Immediate Window in the IDE.
// 17. Run this macro (F5).
//
// Postconditions:
// 1. The output of this macro is logged in c:\temp\dimXpertInfo.txt.
// 2. Inspect the Immediate Window.
//--------------------------------------------------
```

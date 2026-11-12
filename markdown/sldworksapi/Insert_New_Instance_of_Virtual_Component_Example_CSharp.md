---
title: "Insert New Instance of Virtual Component (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_New_Instance_of_Virtual_Component_Example_CSharp.htm"
---

# Insert New Instance of Virtual Component (C#)

This example shows how to:

- create an assembly document.
- insert a new part as a virtual component in the assembly document.
- insert a new instance of the virtual component in the assembly document.

```vb
 //-----------------------------------------------------
 // Preconditions: None
 //
 // Postconditions:
 // 1. An assembly document is created.
 // 2. A virtual part is inserted in the assembly document.
 // 3. A new instance of the virtual part is inserted
 //    in the assembly document.
 // 4. Examine the FeatureManager design tree to
 //    verify steps 2 and 3.
 // 5. Close the assembly document without saving the modified
 //    documents.
 //-----------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace AddNewVirtualPartsCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             string asmTemplate = null;
             asmTemplate = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplateAssembly);

             ModelDoc2 swModel = default(ModelDoc2);
             swModel = (ModelDoc2)swApp.NewDocument(asmTemplate, 0, 0, 0);

             SelectionMgr swSelMgr = default(SelectionMgr);
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             if (swModel.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  false, 0,  null, 0) ==  false)
             {
                 Debug.Print("Failed to select Front plane; check feature name.");
                 return;
             }

             Feature swPlaneFeature = default(Feature);
             swPlaneFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             RefPlane swPlane = default(RefPlane);
             swPlane = (RefPlane)swPlaneFeature.GetSpecificFeature2();

             AssemblyDoc swAssem = default(AssemblyDoc);
             swAssem = (AssemblyDoc)swModel;

             int lResult = 0;
             Component2 swVirtComp = default(Component2);
             lResult = swAssem.InsertNewVirtualPart(swPlane,  out swVirtComp);

             if (lResult == (int)swInsertNewPartErrorCode_e.swInsertNewPartError_NoError)
             {
                 Component2 swSecondComp =  default(Component2);
                 swSecondComp = (Component2)swAssem.AddComponent5(swVirtComp.GetPathName(), (int)swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", false, "", 0.1, 0, 0);
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```

---
title: "Get Types of Entities Attached to Selected Annotation Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Types_of_Entities_for_Selected_Dimension_Example_CSharp.htm"
---

# Get Types of Entities Attached to Selected Annotation Example (C#)

This example shows how to get the types of entities attached to a selected annotation.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part with annotations.
 // 2. Select an annotation for which you want to get attached entities.
 // 3. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
 //-----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace GetAttachedEntities_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Note swSelObj = null;
             Annotation swAnn = default(Annotation);
             int[] vAttEntTypeArr = null;
             object[] vAttEntArr = null;
             int i = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelObj = (Note)swSelMgr.GetSelectedObject6(1, -1);
             swAnn = (Annotation)swSelObj.GetAnnotation();

             Debug.Print("Name = " + swAnn.GetName());
             Debug.Print("  Selection Type as defined in swSelectType_e = " + swSelMgr.GetSelectedObjectType3(1, -1));
             Debug.Print("  Annotation Type as defined in swAnnotationType_e = " + swAnn.GetType());

             vAttEntArr = (object[])swAnn.GetAttachedEntities3();
             vAttEntTypeArr = (int[])swAnn.GetAttachedEntityTypes2();

             if ((vAttEntTypeArr != null))
             {
                 for (i = 0; i <= vAttEntTypeArr.GetUpperBound(0); i++)
                 {
                     // A dangling annotation has at least one entity of type swSelNOTHING
                     Debug.Print("  Type of attached entity(" + i +  ") as defined in swSelectType_e  = " + vAttEntTypeArr[i]);
                 }
             }

         }

         public SldWorks swApp;

     }
 }
```

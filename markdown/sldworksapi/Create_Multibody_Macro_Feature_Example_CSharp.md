---
title: "Create Multibody Macro Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multibody_Macro_Feature_Example_CSharp.htm"
---

# Create Multibody Macro Feature Example (C#)

This example shows how to create a multibody macro feature using a Visual C# SOLIDWORKS add-in.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 //  1. Contact SOLIDWORKS API Support to obtain C#\VB.NET Add-ins to Create a Macro Feature.
 //  2. Copy SwCSharpAddinMF.zip to a local drive.
 //  3. Unzip the file.
 //  4. Open Visual Studio 2015 and convert the Visual C# solution in Visual Studio.
 //  5. Modify the project references to point to your SOLIDWORKS primary
 //     interop assemblies.
 //  6. Right-click the project name in the Solution Explorer, click
 //     Add Reference, click Assemblies > Framework, click
 //     Microsoft.VisualBasic, select its check box, click Microsoft.CSharp, select
 /      its check box, and click OK.
 //  7. Double-click SwAddin.cs in the Solution Explorer.
 //  8. Replace region ISwComFeature Implementation with  this.
 //  9. Replace AddMacroFeature() with this.
 // 10. Click Project > SwCSharpAddinMF Properties > Application and change
 //     Target framework to .NET FrameWork 4.
 // 11. Add using Microsoft.VisualBasic; to the top of SwAddIn.cs.
 // 12. Click Build > Build Solution.
 //     NOTE: The Output window notifies that types registered successfully.
 //     If that message does not appear in the Output window, repeat from
 //     step 1.
 // 13. Open SOLIDWORKS Design.
 // 14. Open public_documents\samples\tutorial\multibody\multi_local.sldprt.
 //
 // Postconditions:
 //  1. Click OK in each message box.
 //  2. Displays C# Addin on the Tools menu.
 //  3. Fires the ISldWorks_ActiveDocChangeNotify event and inserts
 //     the macro feature, MacroFeature1, in the FeatureManager design tree,
 //     which:
 //     * Consumes the part's solid bodies, Fillet5 and Fillet6.
 //     * Creates two solid bodies, MacroFeature1[1] and MacroFeature1[2].
 //  4. Examine the graphics area and FeatureManager design tree.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //----------------------------------------------------------------------------
//Region ISwComFeature Implementation
 #region "ISwComFeature Implementation"

         public object Edit(object app, object modelDoc, object feature)
         {
             Interaction.MsgBox("Macro feature edit");
             return null;
         }

         public object Regenerate(object app, object modelDoc, object feature)
         {
             object functionReturnValue = null;
             Collection OutputBodies = new Collection();
             Body2 swBody = default(Body2);
             Body2[] swBodies = null;
             MacroFeatureData swMacroFeatData = default(MacroFeatureData);
             swMacroFeatData = (MacroFeatureData)((Feature)feature).GetDefinition();
             swMacroFeatData.EnableMultiBodyConsume = true;

             Modeler swModeler = default(Modeler);
             swModeler = (Modeler)((SldWorks)app).GetModeler();
             double[] dblData = new double[9];
             dblData[0] = 0;
             dblData[1] = 0;
             dblData[2] = 0;
             dblData[3] = 1;
             dblData[4] = 0;
             dblData[5] = 0;
             dblData[6] = 0.1;
             dblData[7] = 0.1;
             dblData[8] = 0.1;

             //Output body 1
             swBody = swModeler.CreateBodyFromBox3(dblData);
             OutputBodies.Add(swBody);

             //Output body 2
             dblData[1] = 0.15;
             swBody = swModeler.CreateBodyFromBox3(dblData);
             OutputBodies.Add(swBody);

             int i = 0;
             int j = 0;
             object[] vFaces = null;
             object[] vEdges = null;

             for (i = 1; i <= OutputBodies.Count; i++)
             {
                 swBody = (Body2)OutputBodies[i];
                 vEdges = (object[])swBody.GetEdges();
                 vFaces = (object[])swBody.GetFaces();

                 for (j = 0; j <= Information.UBound(vEdges); j++)
                 {
                     swMacroFeatData.SetEdgeUserId((Edge)vEdges[j], j, 0);
                 }
                 for (j = 0; j <= Information.UBound(vFaces); j++)
                 {
                     swMacroFeatData.SetFaceUserId((Face2)vFaces[j], j, 0);
                 }

                 swBodies[i - 1] = (Body2)OutputBodies[i];
             }

             functionReturnValue = swBodies;
             Interaction.MsgBox("Macro feature rebuild");
             return functionReturnValue;

         }

         public object Security(object app, object modelDoc, object feature)
         {
             Interaction.MsgBox("Macro feature security");
             return null;
         }

         #endregion
```

[Back to top](#top)

```vb
//AddMacroFeature
       public bool AddMacroFeature()
       {

             ModelDoc2 moddoc = default(ModelDoc2);
             FeatureManager FeatMgr = default(FeatureManager);
             Feature MacroFeature = default(Feature);

             moddoc = (ModelDoc2)this.iSwApp.ActiveDoc;
             FeatMgr = moddoc.FeatureManager;

             //Collect input bodies
             object vBodies = null;
             vBodies = ((PartDoc)moddoc).GetBodies2((int)swBodyType_e.swAllBodies, false);

             //Create the macro feature
  MacroFeature = FeatMgr.InsertMacroFeature3("MacroFeature", "SwVBAddinTest.SwAddin", null, null, null, null, null, null, vBodies, null,
             (int)swMacroFeatureOptions_e.swMacroFeatureByDefault);

             return true;
        }
```

[Back to top](#top)

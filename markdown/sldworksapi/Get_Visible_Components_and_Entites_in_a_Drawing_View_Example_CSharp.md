---
title: "Get Visible Components and Entities in Drawing View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Visible_Components_and_Entites_in_a_Drawing_View_Example_CSharp.htm"
---

# Get Visible Components and Entities in Drawing View Example (C#)

This example shows how to get the visible components and entities in a drawing view.

```vb
 //------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 // 2. Select Drawing View2.
 //
 // Postconditions:
 // 1. Gets the visible entities in Drawing View2.
 // 2. Inspect the Immediate window.
 //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace GetSilhouetteEdges_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             DrawingDoc swDrawing = default(DrawingDoc);
             View drView = default(View);
             Component2 Comp = default(Component2);
             SelectData selData = default(SelectData);
             Entity ent = default(Entity);
             int itr = 0;
             int CompCount = 0;
             object[] vComps = null;
             object[] vEdges = null;
             object[] vVerts = null;
             object[] vFaces = null;
             object[] vSilhouetteEdges = null;
             int i = 0;
             bool boolstatus = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDrawing = (DrawingDoc)swModel;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             drView = (View)swDrawing.ActiveDrawingView;

             Debug.Assert((drView != null));
             Debug.Print("Name of drawing view: " + drView.GetName2());
             Debug.Print("");

             CompCount = drView.GetVisibleComponentCount();

             Debug.Assert(CompCount != 0);
             Debug.Print("Number of visible components = " + CompCount);

             vComps = (object[])drView.GetVisibleComponents();

             Debug.Assert((vComps != null));

             for (i = vComps.GetLowerBound(0); i <= vComps.GetUpperBound(0); i++)
             {
                 swModel.ClearSelection2(true);
                 Debug.Print("");
                 Debug.Print("Component " + i +  " name is " + ((Component2)vComps[i]).Name2);

                 Comp = (Component2)vComps[i];

                 //Get all edges of this component that are visible in this drawing view
                 vEdges = (object[])drView.GetVisibleEntities2(Comp, (int)swViewEntityType_e.swViewEntityType_Edge);

                 selData = swSelMgr.CreateSelectData();

                 selData.View = drView;

                 if ((vEdges == null))
                 {
                     Debug.Print("   No edges.");
                 }
                 else
                 {
                     Debug.Print("   This component has " + vEdges.GetUpperBound(0) + 1 + " visible edges in this view.");
                     for (itr = 0; itr <= vEdges.GetUpperBound(0); itr++)
                     {
                         ent = (Entity)vEdges[itr];
                         boolstatus = ent.Select4(false, selData);
                     }
                 }

                 //Get all vertices of this component that are visible in this drawing view
                 vVerts = (object[])drView.GetVisibleEntities2(Comp, (int)swViewEntityType_e.swViewEntityType_Vertex);

                 if ((vVerts == null))
                 {
                     Debug.Print("   No vertices.");
                 }
                 else
                 {
                     Debug.Print("   This component has " + vVerts.GetUpperBound(0) + 1 + " visible vertices in this view.");
                     for (itr = 0; itr <= vVerts.GetUpperBound(0); itr++)
                     {
                         ent = (Entity)vVerts[itr];
                         boolstatus = ent.Select4(false, selData);
                     }
                 }

                 swModel.ClearSelection2(true);

                 //Get all faces of this component that are visible in this drawing view
                 vFaces = (object[])drView.GetVisibleEntities2(Comp, (int)swViewEntityType_e.swViewEntityType_Face);

                 if ((vFaces == null))
                 {
                     Debug.Print("   No faces.");
                 }
                 else
                 {
                     Debug.Print("   This component has " + vFaces.GetUpperBound(0) + 1 + " visible faces in this view.");
                     for (itr = 0; itr <= vFaces.GetUpperBound(0); itr++)
                     {
                         ent = (Entity)vFaces[itr];
                         boolstatus = ent.Select4(false, selData);
                     }
                 }

                 //Get all silhouette edges of this component that are visible in this drawing view
                 vSilhouetteEdges = (object[])drView.GetVisibleEntities2(Comp, (int)swViewEntityType_e.swViewEntityType_SilhouetteEdge);

                 SilhouetteEdge silEdge = default(SilhouetteEdge);
                 if ((vSilhouetteEdges == null))
                 {
                     Debug.Print("   No silhouette edges.");
                 }
                 else
                 {
                     Debug.Print("   This component has " + vSilhouetteEdges.GetUpperBound(0) + 1 + " visible silhouette edges in this view.");
                     for (itr = 0; itr <= vSilhouetteEdges.GetUpperBound(0); itr++)
                     {
                         silEdge = (SilhouetteEdge)vSilhouetteEdges[itr];
                         boolstatus = silEdge.Select(false, selData);
                     }
                 }
             }

         }

         public SldWorks swApp;

     }

 }
```

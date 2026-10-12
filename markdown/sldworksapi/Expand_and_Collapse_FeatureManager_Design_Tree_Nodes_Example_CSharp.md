---
title: "Expand or Collapse FeatureManager Design Tree Nodes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm"
---

# Expand or Collapse FeatureManager Design Tree Nodes Example (C#)

This example shows how to traverse, expand, and collapse the nodes of a FeatureManager design tree.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part or assembly document.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Expands all of the FeatureManager design tree nodes.
 // 2. Click OK to collapse all nodes.
 // 3. Inspect the Immediate window.
 //--------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;
 namespace ExpandCollapseFMDesignTree_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         int traverseLevel;
         bool expandThis;

         public void Main()
         {
             int i = 0;

             ModelDoc2 myModel = default(ModelDoc2);
             FeatureManager featureMgr = default(FeatureManager);
             TreeControlItem rootNode = default(TreeControlItem);

             myModel = (ModelDoc2)swApp.ActiveDoc;
             featureMgr = myModel.FeatureManager;
             rootNode = featureMgr.GetFeatureTreeRootItem2((int)swFeatMgrPane_e.swFeatMgrPaneBottom);

             expandThis = true;

             for (i = 0; i <= 1; i++)
             {
                 if ((rootNode != null))
                 {
                     Debug.Print("");
                     traverseLevel = 0;
                     traverse_node(rootNode);
                 }

                 expandThis = false;

                 if (i == 0)
                 {
                     MessageBox.Show("OK to collapse all nodes?");
                 }
             }
         }

         private void traverse_node(TreeControlItem node)
         {
             TreeControlItem childNode = default(TreeControlItem);
             Feature featureNode = default(Feature);
             Component2 componentNode = default(Component2);
             int nodeObjectType = 0;
             object nodeObject = null;
             string restOfString = "";
             string indent = "";
             int i = 0;
             bool displayNodeInfo = false;
             string compName = null;
             int suppr = 0;
             string supprString = "";
             int vis = 0;
             string visString = "";
             string notfloatingString = "";
             bool notfloating = false;
             object componentDoc = null;
             string docString = "";
             string refConfigName = "";

             displayNodeInfo = false;
             nodeObjectType = node.ObjectType;
             nodeObject = node.Object;

             switch (nodeObjectType)
             {
                 case (int)swTreeControlItemType_e.swFeatureManagerItem_Feature:

                     displayNodeInfo = true;
                     if ((nodeObject != null))
                     {
                         featureNode = (Feature)nodeObject;
                         restOfString =  "[FEATURE: " + featureNode.Name + "]";
                     }
                     else
                     {
                         restOfString =  "[FEATURE: object Null?!]";
                     }

                     break;
                 case (int)swTreeControlItemType_e.swFeatureManagerItem_Component:

                     displayNodeInfo = true;

                     if ((nodeObject != null))
                     {
                         componentNode = (Component2)nodeObject;
                         compName = componentNode.Name2;

                         if ((string.IsNullOrEmpty(compName)))
                         {
                             compName =  "???";
                         }

                         suppr = componentNode.GetSuppression();

                         switch ((suppr))
                         {

                             case (int)swComponentSuppressionState_e.swComponentFullyResolved:
                                 supprString =  "Resolved";

                                 break;
                             case (int)swComponentSuppressionState_e.swComponentLightweight:
                                 supprString =  "Lightweight";

                                 break;
                             case (int)swComponentSuppressionState_e.swComponentSuppressed:
                                 supprString =  "Suppressed";

                                 break;
                         }

                         vis = componentNode.Visible;

                         switch ((vis))
                         {

                             case (int)swComponentVisibilityState_e.swComponentHidden:
                                 visString =  "Hidden";

                                 break;
                             case (int)swComponentVisibilityState_e.swComponentVisible:
                                 visString =  "Visible";

                                 break;
                         }

                         notfloating = componentNode.IsFixed();

                         if (notfloating == false)
                         {
                             notfloatingString =  "Floating";
                         }
                         else
                         {
                             notfloatingString =  "Fixed";
                         }

                         componentDoc = componentNode.GetModelDoc2();

                         if (componentDoc == null)
                         {
                             docString = "NotLoaded";
                         }
                         else
                         {
                             docString =  "Loaded";
                         }

                         refConfigName = componentNode.ReferencedConfiguration;

                         if ((string.IsNullOrEmpty(refConfigName)))
                         {
                             refConfigName =  "???";
                         }

                         restOfString =  "[COMPONENT: " + compName +  " " + docString + " " + supprString + " " + visString + " " + refConfigName + "]";
                     }
                     else
                     {
                         restOfString =  "[COMPONENT: object Null?!]";
                     }

                     break;
                 default:

                     displayNodeInfo = true;

                     if ((nodeObject != null))
                     {
                         restOfString =  "[object type not handled]";
                     }
                     else
                     {
                         restOfString =  "[object Null?!]";
                     }

                     break;
             }

             for (i = 1; i <= traverseLevel; i++)
             {
                 indent = indent + "  ";
             }

             if ((displayNodeInfo))
             {
                 Debug.Print(indent + node.Text + " : " + restOfString);
             }

             // Expand the node
             node.Expanded = expandThis;
             traverseLevel = traverseLevel + 1;
             childNode = node.GetFirstChild();

             while ((childNode != null))
             {
                 Debug.Print(indent + "Node is expanded: " + childNode.Expanded);
                 traverse_node(childNode);
                 childNode = childNode.GetNext();
             }

             traverseLevel = traverseLevel - 1;

         }

         public SldWorks swApp;

     }

 }
```

---
title: "Get and Set Block Definitions, Block Instances, and BlockAttribute Instances Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Block_Definitions_Block_Instances_and_BlockAttribute_Instances_Example_CSharp.htm"
---

# Get and Set Block Definitions, Block Instances, and BlockAttribute Instances Example (C#)

This example shows how to get and set Block definitions, Block instances, and BlockAttribute instances.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
// 4. Add references to System and System.Windows.Forms.
// 5. Start DraftSight and open a document.
// 6. Review the code to see how Block definitions,
//    Block instances, and BlockAttribute instances
//    are modified.
// 7. Start debugging the project.
//
// Postconditions: Block definitions, Block instances, and
// BlockAttribute instances are modified. Message
// boxes pop up when a Block-related entity does not exist.
// Read the text in each message box before clicking OK to close it.
//----------------------------------------------------------------
using DraftSight.Interop.dsAutomation;
using System;
using System.Windows.Forms;
using System.Runtime.InteropServices;
```

```
static class Module1
{
```

```
    public static void Main()
	{
        	DraftSight.Interop.dsAutomation.Application dsApp;
		Document dsDoc = default(Document);
```

```
		//Connect to DraftSight application
        	dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");

		dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
		//Get active document
		dsDoc = (Document)dsApp.GetActiveDocument();
```

```
		if (dsDoc != null)
                {
			//Test Block definitions
			TestBlockDefinitions(dsDoc);
```

```
		}
                else
                {
			MessageBox.Show("There are no open documents in DraftSight.");
		}
	}
```

```
    public static void TestBlockDefinitions(Document dsDoc)
    {
        object[] dsVarBlkDefinitions = null;
        BlockDefinition dsBlkDefinition = default(BlockDefinition);
        ExternalReference dsExtRef = default(ExternalReference);
        int index = 0;
```

```
        //Get all Block definitions in the drawing
        dsVarBlkDefinitions = (object[])dsDoc.GetBlockDefinitions();
```

```
        //Check if there are any Block definitions
        if (dsVarBlkDefinitions != null)
        {
            for (index = 0; index <= dsVarBlkDefinitions.Length - 1; index++)
            {
                for (index = dsVarBlkDefinitions.GetLowerBound(0); index <= dsVarBlkDefinitions.GetUpperBound(0); index++)
                {
                    dsBlkDefinition = (BlockDefinition)dsVarBlkDefinitions[index];
```

```
                    //Check if Block definition is a reference
                    dsExtRef = dsBlkDefinition.GetExternalReference();
                    if (dsExtRef != null)
                    {
                        MessageBox.Show(dsBlkDefinition.GetName() + " block definition is a reference.");
                    }
                    else
                    {
                        MessageBox.Show(dsBlkDefinition.GetName() + " block definition isn't a reference.");
                    }
```

```
                    //Test BlockAttribute definitions
                    TestAttributeDefinitions(dsBlkDefinition);
```

```
                    //Test Block instances
                    TestBlockInstances(dsBlkDefinition);
```

```
                }
```

```
            }
        }
        else
        {
            MessageBox.Show("There are no Block definitions in \"" + dsDoc.GetPathName() + "\" document.");
        }
    }
    public static void TestAttributeDefinitions(BlockDefinition dsBlkDefinition)
    {
        object[] dsVarAttrDefinitions = null;
        AttributeDefinition dsAttrDefinition = default(AttributeDefinition);
        int index = 0;
        string attrDefCaption = null;
        string attrDefValue = null;
        string attrDefName = null;
        string newAttrCaptionValue = null;
        string newAttrDefValue = null;
        string newAttrDefName = null;
```

```
        //Get all BlockAttribute definitions in Block definition
        dsVarAttrDefinitions = (object[])dsBlkDefinition.GetAttributeDefinitions();
```

```
        //Check if there are any BlockAttribute definition
```

```
        if (dsVarAttrDefinitions != null)
        {
```

```
            for (index = dsVarAttrDefinitions.GetLowerBound(0); index <= dsVarAttrDefinitions.GetUpperBound(0); index++)
            {
                dsAttrDefinition = (AttributeDefinition)dsVarAttrDefinitions[index];
```

```
                //Get BlockAttribute definition caption and change
                attrDefCaption = dsAttrDefinition.Caption;
```

```
                //Change caption value
                newAttrCaptionValue = dsAttrDefinition.Caption + "_Changed";
                dsAttrDefinition.Caption = newAttrCaptionValue;
```

```
                if (newAttrCaptionValue != dsAttrDefinition.Caption)
                {
                    MessageBox.Show("The caption of '" + dsAttrDefinition.Name + "' BlockAttribute definition wasn't changed from '" + attrDefCaption + "' to '" + newAttrCaptionValue + "'.");
                }
```

```
                //Get BlockAttribute definition value
                attrDefValue = dsAttrDefinition.Value;
```

```
                //Change BlockAttribute definition value
                newAttrDefValue = dsAttrDefinition.Value + "_Changed";
                dsAttrDefinition.Value = newAttrDefValue;
```

```
                if (newAttrDefValue != dsAttrDefinition.Value)
                {
                    MessageBox.Show("The value of '" + dsAttrDefinition.Name + "' BlockAttribute definition wasn't changed from '" + attrDefValue + "' to '" + newAttrDefValue + "'.");
                }
```

```
                //Get BlockAttribute definition name
                attrDefName = dsAttrDefinition.Name;
```

```
                //Change BlockAttribute definition name
                newAttrDefName = dsAttrDefinition.Name + "_Changed";
                dsAttrDefinition.Name = newAttrDefName;
```

```
                if (newAttrDefName != dsAttrDefinition.Name)
                {
                    MessageBox.Show("The name of '" + dsAttrDefinition.Name + "' BlockAttribute definition wasn't changed from '" + attrDefName + "' to '" + newAttrDefName + "'.");
                }
```

```
            }
```

```
        }
        else
        {
            MessageBox.Show("There are no BlockAttribute definitions in \"" + dsBlkDefinition.GetName() + "\" block definition.");
        }
    }
    public static void TestBlockInstances(BlockDefinition dsBlkDefinition)
    {
        object[] dsVarBlockInstances = null;
        BlockInstance dsBlockInstance = default(BlockInstance);
        BlockDefinition dsBlockDefinition = default(BlockDefinition);
        object Workspace = null;
        dsObjectType_e workSpaceType = default(dsObjectType_e);
        Sheet dsSheet = default(Sheet);
        Model dsModel = default(Model);
        int index = 0;
```

```
        //Get Block instances of Block definition
        dsVarBlockInstances = (object[])dsBlkDefinition.GetBlockInstances();
```

```
        //Check if there are any Block instances
```

```
        if (dsVarBlockInstances != null)
        {
```

```
            for (index = dsVarBlockInstances.GetLowerBound(0); index <= dsVarBlockInstances.GetUpperBound(0); index++)
            {
                dsBlockInstance = (BlockInstance)dsVarBlockInstances[index];
```

```
                //Test attribute instances
                TestAttributeInstances(dsBlockInstance);
```

```
                //Get Block definition from Block instance
                dsBlockDefinition = dsBlockInstance.GetBlockDefinition();
                if (dsBlockDefinition == null)
                {
                    MessageBox.Show("GetBlockDefinition method returns Nothing for Block instance with ID=\"" + dsBlockInstance.GetID() + ".");
                }
```

```
                //Get working space
                dsBlockInstance.GetWorkingSpace(out workSpaceType, out Workspace);
```

```
                if (Workspace != null)
                {
                    //If work space is sheet
                    if (workSpaceType == dsObjectType_e.dsSheetType)
                    {
                        dsSheet = (Sheet)Workspace;
```

```
                        if (dsSheet == null)
                        {
                            MessageBox.Show("GetWorkingSpace method returns dsSheetType type, but sheet object is Nothing.");
                        }
```

```
                    }
                    else if (workSpaceType == dsObjectType_e.dsModelType)
                    {
                        dsModel = (Model)Workspace;
```

```
                        if (dsModel == null)
                        {
                            MessageBox.Show("GetWorkingSpace method returns dsModelType type, but model object is Nothing.");
                        }
```

```
                    }
```

```
                }
                else
                {
                    MessageBox.Show("GetWorkingSpace method returns Nothing for Block instance.");
                }
```

```
            }
```

```
        }
        else
        {
            MessageBox.Show("There are no Block instances of \"" + dsBlkDefinition.GetName() + "\" Block definition.");
        }
    }
```

```
    public static void TestAttributeInstances(BlockInstance dsBlockInstance)
    {
        object[] dsVarAttrInstances = null;
        AttributeInstance dsAttrInstance = default(AttributeInstance);
        int index = 0;
        string attrInstanceName = null;
        string attrInstanceValue = null;
        string newAttrInstanceValue = null;
```

```
        //Get BlockAttribute instances
        dsVarAttrInstances = dsBlockInstance.GetAttributeInstances();
```

```
        //Check if there are any BlockAttribute instances
```

```
        if (dsVarAttrInstances != null)
        {
```

```
            for (index = dsVarAttrInstances.GetLowerBound(0); index <= dsVarAttrInstances.GetUpperBound(0); index++)
            {
                dsAttrInstance = (AttributeInstance)dsVarAttrInstances[index];
```

```
                //Get BlockAttribute instance name
                attrInstanceName = dsAttrInstance.GetName();
```

```
                //Get BlockAttribute instance value
                attrInstanceValue = dsAttrInstance.Value;
```

```
                //Change BlockAttribute instance value
                newAttrInstanceValue = dsAttrInstance.Value + "_Changed";
                dsAttrInstance.Value = newAttrInstanceValue;
```

```
                if (newAttrInstanceValue != dsAttrInstance.Value)
                {
                    MessageBox.Show("The value of the '" + dsAttrInstance.GetName() + "' instance wasn't changed from '" + attrInstanceValue + "' to '" + newAttrInstanceValue + "'.");
                }
```

```
                //Test general properties
                TestAttributeInstanceGeneralProperties(dsAttrInstance);
```

```
                //Select BlockAttribute instance
                dsAttrInstance.Select(true);
```

```
                //Deselect BlockAttribute instance
                dsAttrInstance.Select(false);
```

```
            }
```

```
        }
        else
        {
```

```
            MessageBox.Show("There are no BlockAttribute instances in \"" + dsBlockInstance.GetBlockDefinition().GetName() + "\" Block instance.");
        }
```

```
    }
    public static void TestAttributeInstanceGeneralProperties(AttributeInstance dsAttrInstance)
    {
        string layer = null;
        string lineStyle = null;
        double lineScale = 0;
        double newLineScale = 0;
        double precision = 0;
        dsLineWeight_e lineWeight = default(dsLineWeight_e);
        dsLineWeight_e newLineWeight = default(dsLineWeight_e);
        bool visible = false;
        bool newVisibleValue = false;
```

```
        //Get layer name
        layer = dsAttrInstance.Layer;
```

```
        //Set the same layer
        dsAttrInstance.Layer = layer;
```

```
        //Get line scale
        lineScale = dsAttrInstance.LineScale;
```

```
        //Set line scale
        newLineScale = 8.6;
        dsAttrInstance.LineScale = newLineScale;
```

```
        precision = 1E-09;
        if (Math.Abs(newLineScale - dsAttrInstance.LineScale) > precision)
        {
            MessageBox.Show("The line scale of '" + dsAttrInstance.GetName() + "' attribute instance wasn't changed from '" + lineScale + "' to '" + newLineScale + "'.");
        }
```

```
        //Get line style
        lineStyle = dsAttrInstance.LineStyle;
```

```
        //Set the same line style
        dsAttrInstance.LineStyle = lineStyle;
```

```
        //Get line weight
        lineWeight = dsAttrInstance.LineWeight;
```

```
        //Set new line weight
        newLineWeight = dsLineWeight_e.dsLnWt_015;
        dsAttrInstance.LineWeight = newLineWeight;
        if (newLineWeight != dsAttrInstance.LineWeight)
        {
            MessageBox.Show("The line weight of '" + dsAttrInstance.GetName() + "' attribute instance wasn't changed from '" + lineWeight + "' to '" + newLineWeight + "'.");
        }
```

```
        //Get visible property
        visible = dsAttrInstance.Visible;
```

```
        //Set visible property
        newVisibleValue = !visible;
        dsAttrInstance.Visible = newVisibleValue;
        if (newVisibleValue != dsAttrInstance.Visible)
        {
            MessageBox.Show("The visible property of '" + dsAttrInstance.GetName() + "' attribute instance wasn't changed from '" + visible + "' to '" + newVisibleValue + "'.");
        }
```

```
    }
```

```
}
```

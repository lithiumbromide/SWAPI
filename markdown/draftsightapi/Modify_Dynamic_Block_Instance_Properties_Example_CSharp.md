---
title: "Modify Dynamic Block Instance Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Modify_Dynamic_Block_Instance_Properties_Example_CSharp.htm"
---

# Modify Dynamic Block Instance Properties Example (C#)

```vb
  This example demonstrates how to modify a dynamic block in a drawing using a DraftSight add-in.
  Read the Microsoft Visual Studio DraftSight API templates and add-ins > Creating a C# add-in using the template section in the Getting Started topic in the DraftSight API help. Other C# add-in examples are installed in   DraftSight_install_dir\APISDK\samples which you may use as a reference when developing this add-in.
```

//-----------------------------------------------------------------------------------------
// Preconditions:
`// 1. In Visual Studio, use the Visual C# DraftSight add-in template, DSAddinCSharpPremium, // to create a Visual C# add-in, Type DynBlockInstance_Sample in the Name field. // 2. Copy the code after these comments into your add-in’s respective .cs files. // 3. Modify the project’s references to include your installation’s DraftSight.Interop.dsAddin // and DraftSight.Interop.dsAutomation. // 4. Select Release in the Solution Configurations dropdown in the toolbar. // 5. Create an x64 solution platform by selecting Configuration Manager in the Solution Platforms // dropdown in the toolbar. In the Configuration Manager dialog, select New in the // Active solution platform dropdown. Select x64 and click OK in the New Solution Platform dialog. // 6. Modify the project’s properties (right-click project and select Properties): // a. On the Application tab, click Assembly Information, and select Make assembly COM-Visible // in the dialog. Click OK. // b. On the Debug tab, select Start external program, click Browse, and navigate to // and select your installation’s DraftSight.exe. // 7. Remove DSAddinDocument.cs from the project. // 8. Ensure that your add-in’s config file exists in C:\ProgramData\Dassault Systemes\DraftSight\addinConfigs. // If it doesn't, create one using an existing config file as a model. // 9. Click Start on the toolbar or press F5.`
//
// Postconditions:
`// 1. Open a drawing with a dynamic block. // 2. Select the dynamic block in the drawing and select` **DynBlockInstance_SampleCommand** on the DynBlockInstance_Sample menu.
`// 3. Click Yes in the dialog to modify the properties of the dynamic block. // 4. Inspect the Command Window to see which properties were modified.`
//----------------------------------------------------------------

```vb
 //DSAddin.cs:

  using System;
  using System.Collections.Generic;
  using System.Linq;
  using System.Text;
  using System.Runtime.InteropServices;
  using System.Reflection;
  using DraftSight.Interop.dsAddin;
  using DraftSight.Interop.dsAutomation;

  namespace DynBlockInstance_Sample
 {
      [Guid("ab3e2b13-b642-42c3-a16e-985ea8e920f0"), ComVisible(true)]
       public  class  DynBlockInstance_Sample : DsAddin
      {
            string AddinGuid =   "";
           DraftSight.Interop.dsAutomation.Application dsApp =   null;
           List<DSAddinCommand> AddinCommands =  new List<DSAddinCommand>();
           BitmapHandler iBmp;

            public DynBlockInstance_Sample()
           {
              AddinGuid =   this.GetType().GUID.ToString();
           }

            #region Class Properties
            public  string GUID
           {
              get
              {  return AddinGuid; }
           }

            public DraftSight.Interop.dsAutomation.Application dsApplication
           {
               get
              {  return dsApp; }
           }

            #endregion

            public  bool ConnectToDraftSight(object DsApp,   int Cookie)
           {
              dsApp = (DraftSight.Interop.dsAutomation.Application)DsApp;

               // Create commands and UI to launch them
              CreateUserInterfaceAndCommands();

               return  true;
           }

            public  bool DisconnectFromDraftSight()
           {
               // Dispose of Commands added to DraftSight by this addin
              DisposeCommands();

               // Remove any UI created in DraftSight by this Addin
              dsApp.RemoveUserInterface(AddinGuid);

               //Dispose of the bitmap handler
              iBmp.Dispose();

              dsApp =   null;

               return  true;
           }

            public  bool HasSignedByDraftSight(out   string id1,   out   int id2,   out   int key1,   out   int key2)
           {
              id1 = AddinGuid;
              id2 = 0;
              key1 = 0;
              key2 = 0;

               return  true;
           }

            private  void CreateUserInterfaceAndCommands()
           {
               // Create object to handle addin's images
               if (iBmp ==  null)
                  iBmp =   new BitmapHandler();

               // Create image files needed for UI, from embedded resources
              Assembly thisAssembly;
              thisAssembly = System.Reflection.Assembly.GetAssembly(this.GetType());
               string lgBmp = iBmp.CreateFileFromResourceBitmap("DynBlockInstance_Sample.ToolBar_Large.png", thisAssembly);
               string smBmp = iBmp.CreateFileFromResourceBitmap("DynBlockInstance_Sample.ToolBar_Small.png", thisAssembly);

               //Add a user defined menu to the DraftSight user interface
               int position = 1;
               const  int MENU_POSITION = 9;   //New menu should be at the end   of the menu bar in 3D mode
              MenuItem myMenu = dsApp.AddMenu(AddinGuid, dsUIState_e.dsUIState_Document, MENU_POSITION,   "DynBlockInstance_Sample");

               // Add a new command to DraftSight
              DSAddinCommand cmdCommand =   new DSAddinCommand(this,   "DynBlockInstance_Sample_Command");
               if (cmdCommand.IsUserCommandValid())
              {
                   // Keep a list of all commands this add-in added to DraftSight
                  AddinCommands.Add(cmdCommand);

                   //  Add a new user command to create menu items and toolbar buttons
                  DSAddinUserCommand userCmdCommand =  new DSAddinUserCommand(this, cmdCommand,   "DynBlockInstance_Sample_Command",   "DynBlockInstance_SampleCommand", smBmp, lgBmp);
                  myMenu.InsertMenuItem(AddinGuid, dsMenuItemType_e.dsMenuItemType_UserCommand, 1,   "DynBlockInstance_SampleCommand", userCmdCommand.GetUserCommandID());

                   // Add a toolbar for this add-in
                  Toolbar dsToolbar = dsApp.AddToolbar(AddinGuid, dsUIState_e.dsUIState_Document,   "DynBlockInstance_Sample Toolbar");

                   //  Add a new item to the addin's toolbar
                  ToolbarItem dsToolbarItem = dsToolbar.InsertToolbarItem(AddinGuid, dsToolbarItemType_e.dsToolBarItemType_UserCommand, position,   "DynBlockInstance_SampleCommand", userCmdCommand.GetUserCommandID());
              }
           }

            private  void DisposeCommands()
           {
               while (AddinCommands.Count > 0)
              {
                  AddinCommands[0].Dispose();
                  AddinCommands.RemoveAt(0);
              }
           }
      }
 }
```

// DSAddinUserCommand.cs:

```vb
  using System;
  using System.Collections.Generic;
  using System.Linq;
  using System.Text;
  using DraftSight.Interop.dsAddin;
  using DraftSight.Interop.dsAutomation;

  namespace DynBlockInstance_Sample
 {
       class  DSAddinUserCommand
      {

           DynBlockInstance_Sample myAddin =   null;
           DraftSight.Interop.dsAutomation.Application dsApp =   null;
           UserCommand myUserCommand =   null;

            public DSAddinUserCommand(DynBlockInstance_Sample pAddin, DSAddinCommand addinCmd,
               string CommandString,   string Description,   string SmallIcon,   string LargeIcon)
           {
              myAddin = pAddin;
              dsApp = myAddin.dsApplication;

              dsCreateCommandError_e commandErr;
              myUserCommand = dsApp.CreateUserCommand(myAddin.GUID, addinCmd.CommandString, CommandString, Description, SmallIcon, LargeIcon, dsUIState_e.dsUIState_Document,   out commandErr);

           }

            public  bool IsUserCommandValid()
           {
               return myUserCommand !=   null;
           }

            public  string GetUserCommandID()
           {
               if (IsUserCommandValid())
                   return myUserCommand.GetID();
               else
                   return   "";
           }
      }
 }
```

//DSAddinCommand.cs:

```vb
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using DraftSight.Interop.dsAddin;
 using DraftSight.Interop.dsAutomation;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace DynBlockInstance_Sample
 {
      class DSAddinCommand : IDisposable
      {
           DynBlockInstance_Sample myAddin = null;
           DraftSight.Interop.dsAutomation.Application dsApp = null;
           Command myCommand = null;
           string cmdString = "ASD";
           private bool isDisposed = false;

           public string CommandString
           {
              get
              { return cmdString; }
           }

           public DSAddinCommand(DynBlockInstance_Sample pAddin, string CommandString)
           {
              myAddin = pAddin;
              dsApp = myAddin.dsApplication;
              cmdString = CommandString;

              // Create new DraftSight Command
              dsCreateCommandError_e commandErr;
              myCommand = dsApp.CreateCommand(myAddin.GUID, CommandString, out commandErr);

              // Add event handler for this new command
              // The handler is the method that will be run when the command is run from DraftSight
              if (IsUserCommandValid())
                  myCommand.ExecuteNotify += new _ICommandEvents_ExecuteNotifyEventHandler(ExecuteCommand);

           }

           public bool IsUserCommandValid()
           {
              return myCommand != null;
           }

           public void ExecuteCommand()
           {
              //Get active document
              Document dsDoc = dsApp.GetActiveDocument();
              if (dsDoc == null)
                  return;

              //Get command message object
              CommandMessage dsCommandMessage = dsApp.GetCommandMessage();
              if (dsCommandMessage == null)
                  return;

              SelectionManager dsSelectionManager = dsDoc.GetSelectionManager();
              SelectionFilter dsSelectionFilter = dsSelectionManager.GetSelectionFilter();
              dsSelectionFilter.Clear();

              dsSelectionFilter.AddEntityType(dsObjectType_e.dsBlockInstanceType);

              dsSelectionFilter.Active = true;
               dsSelectionManager.ClearSelections(dsSelectionSetType_e.dsSelectionSetType_Previous);
              String errorMessage = "You must select a dynamic block before executing this command";
              if (dsCommandMessage.PromptForSelection(true, "Select dynamic block", errorMessage))
              {
                  int count = dsSelectionManager.GetSelectedObjectCount(dsSelectionSetType_e.dsSelectionSetType_Previous);

                  DialogResult dialogResult = MessageBox.Show("Click Yes to change the properties of the selected dynamic block; Click No to reset and convert the selected dynamic block to a static block", "Dynamic block", MessageBoxButtons.YesNo, MessageBoxIcon.Question);

                  for (int index = 0; index < count; ++index)
                  {
                      dsObjectType_e entityType = dsObjectType_e.dsObjectUndefinedType;
                      object selObject = dsSelectionManager.GetSelectedObject(dsSelectionSetType_e.dsSelectionSetType_Previous, index, out entityType);
                      if (entityType != dsObjectType_e.dsBlockInstanceType)
                      {
                          continue;
                      }

                      BlockInstance dsBlockInstance = selObject as BlockInstance;
                      if (dsBlockInstance == null)
                          continue;

                      if ( dsBlockInstance.IsDynamicBlock )
                      {
                          if (dialogResult == DialogResult.No)
                          {
                              if (!dsBlockInstance.ResetBlock())
                              {
                                  dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsBlockInstance.ResetBlock() failed to reset." + "</ p ></b>");
                              }

                              if (!dsBlockInstance.ConvertToStaticBlock())
                              {
                                  dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsBlockInstance.ConvertToStaticBlock() failed to convert to static block." + "</ p ></b>");
                              }

                              continue;
                          }

                          object objs = dsBlockInstance.GetDynamicBlockProperties();
                          if (objs == null)
                              continue;

                          object[] dsDynamicBlocksProperties = (object[])objs;
                          for ( int i = 0; i < dsDynamicBlocksProperties.Length; ++i )
                          {
                              DynamicBlockInstanceProperty dsDynamicBlockInstanceProperty = dsDynamicBlocksProperties[i] as DynamicBlockInstanceProperty;
                              if (dsDynamicBlockInstanceProperty == null)
                                  continue;

                              if( String.IsNullOrEmpty(dsDynamicBlockInstanceProperty.PropertyName) )
                              {
                                  dsCommandMessage.PrintLine("Property name should not empty." );
                                  continue;
                              }

                              dsDynamicBlockReferencePropertyUnitsType_e unitType = dsDynamicBlockInstanceProperty.UnitsType;
                              dsCommandMessage.PrintLine("<b>< p style = " + "\"color:green;\"" + ">" + "Property name:  " + dsDynamicBlockInstanceProperty.PropertyName + "</ p ></b>");
                              if (unitType == dsDynamicBlockReferencePropertyUnitsType_e.dsDynamicBlockReferencePropertyUnitsType_UnknownUnits)
                              {
                                  object allowedVal = dsDynamicBlockInstanceProperty.GetStringAllowedValues();
                                  int indexArray = -1;
                                  if (allowedVal != null)
                                  {
                                      string[] strArray = (string[])allowedVal;
                                      string oldVal = dsDynamicBlockInstanceProperty.GetStringDynamicBlockProperty();
                                      indexArray = Array.IndexOf(strArray, oldVal);
                                      if (indexArray != strArray.Length - 1)
                                      {
                                          indexArray = indexArray + 1;
                                      }
                                      else
                                          indexArray = 0;

                                       dsDynamicBlockInstanceProperty.SetStringDynamicBlockProperty(strArray[indexArray]);
                                      if (dsDynamicBlockInstanceProperty.ReadOnly && String.Compare(strArray[indexArray], dsDynamicBlockInstanceProperty.GetStringDynamicBlockProperty()) == 0)
                                      {
                                          dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.SetStringDynamicBlockProperty() did not work because property is read only" + "</ p ></b>");
                                      }
                                      else if(String.Compare(strArray[indexArray], dsDynamicBlockInstanceProperty.GetStringDynamicBlockProperty()) != 0)
                                      {
                                          dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.GetStringDynamicBlockProperty() should return " + strArray[indexArray] + ", but it returns " + dsDynamicBlockInstanceProperty.GetStringDynamicBlockProperty() + "</ p ></b>");
                                      }
                                      continue;
                                  }

                                  allowedVal = dsDynamicBlockInstanceProperty.GetInteger16AllowedValues();
                                  if (allowedVal != null)
                                  {
                                      int[] intArray = (int[])allowedVal;
                                      int oldVal = dsDynamicBlockInstanceProperty.GetInteger16DynamicBlockProperty();
                                      indexArray = Array.IndexOf(intArray, oldVal);
                                      if (indexArray != intArray.Length - 1)
                                      {
                                          indexArray = indexArray + 1;
                                      }
                                      else
                                          indexArray = 0;

                                       dsDynamicBlockInstanceProperty.SetInteger16DynamicBlockProperty(intArray[indexArray]);
                                      if (dsDynamicBlockInstanceProperty.ReadOnly && intArray[indexArray] == dsDynamicBlockInstanceProperty.GetInteger16DynamicBlockProperty())
                                      {
                                          dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.SetInteger16DynamicBlockProperty() did not work because property is read only" + "</ p ></b>");
                                      }
                                      else if (intArray[indexArray] != dsDynamicBlockInstanceProperty.GetInteger16DynamicBlockProperty())
                                      {
                                          dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.GetInteger16DynamicBlockProperty() should return " + intArray[indexArray] + ", but it returns " + dsDynamicBlockInstanceProperty.GetInteger16DynamicBlockProperty() + "</ p ></b>");
                                      }
                                      continue;
                                  }

                                  allowedVal = dsDynamicBlockInstanceProperty.GetInteger32AllowedValues();
                                  if (allowedVal != null)
                                  {
                                      int[] intArray = (int[])allowedVal;
                                      int oldVal = dsDynamicBlockInstanceProperty.GetInteger32DynamicBlockProperty();
                                      indexArray = Array.IndexOf(intArray, oldVal);
                                      if (indexArray != intArray.Length - 1)
                                      {
                                          indexArray = indexArray + 1;
                                      }
                                      else
                                          indexArray = 0;

                                       dsDynamicBlockInstanceProperty.SetInteger32DynamicBlockProperty(intArray[indexArray]);
                                      if (dsDynamicBlockInstanceProperty.ReadOnly && intArray[indexArray] == dsDynamicBlockInstanceProperty.GetInteger32DynamicBlockProperty())
                                      {
                                          dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.SetInteger32DynamicBlockProperty() did not work because property is read only" + "</ p ></b>");
                                      }
                                      else if (intArray[indexArray] != dsDynamicBlockInstanceProperty.GetInteger32DynamicBlockProperty())
                                      {
                                          dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.GetInteger32DynamicBlockProperty() should return " + intArray[indexArray] + ", but it returns " + dsDynamicBlockInstanceProperty.GetInteger32DynamicBlockProperty() + "</ p ></b>");
                                      }
                                      continue;
                                  }
                              }
                              else if (unitType == dsDynamicBlockReferencePropertyUnitsType_e.dsDynamicBlockReferencePropertyUnitsType_Angular
                                  || unitType == dsDynamicBlockReferencePropertyUnitsType_e.dsDynamicBlockReferencePropertyUnitsType_Area
                                  || unitType == dsDynamicBlockReferencePropertyUnitsType_e.dsDynamicBlockReferencePropertyUnitsType_Distance)
                              {

                                  double valForAdd = 1.0;
                                  if ( unitType == dsDynamicBlockReferencePropertyUnitsType_e.dsDynamicBlockReferencePropertyUnitsType_Angular )
                                  {
                                      double angle = 15;// angle will be increased by 15 degrees
                                      valForAdd = (Math.PI / 180) * angle;
                                      if(dsDynamicBlockInstanceProperty.GetDoubleDynamicBlockProperty() == (Math.PI / 180) * 360 )
                                      {
                                          valForAdd = -valForAdd;
                                      }
                                  }

                                  double newValue = dsDynamicBlockInstanceProperty.GetDoubleDynamicBlockProperty() + valForAdd;
                                  dsDynamicBlockInstanceProperty.SetDoubleDynamicBlockProperty(newValue);
                                  if (dsDynamicBlockInstanceProperty.ReadOnly && dsDynamicBlockInstanceProperty.GetDoubleDynamicBlockProperty() == newValue)
                                  {
                                      dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.SetDoubleDynamicBlockProperty() did not work because property is read only" + "</ p ></b>");
                                  }
                                  else if (dsDynamicBlockInstanceProperty.GetDoubleDynamicBlockProperty() != newValue)
                                  {
                                      dsCommandMessage.PrintLine("<b>< p style = " + "\"color:red;\"" + ">" + "dsDynamicBlockInstanceProperty.GetDoubleDynamicBlockProperty() should return " + newValue + ", but it returns " + dsDynamicBlockInstanceProperty.GetDoubleDynamicBlockProperty() + "</ p ></b>");
                                  }

                              }
                          }
                      }
                      else
                      {
                          dsCommandMessage.PrintLine("Selection is not a dynamic block.");
                      }
                  }
              }
           }

           public void Dispose()
           {
              Dispose(true);
              GC.SuppressFinalize(this);
           }

           protected virtual void Dispose(bool disposing)
           {
              if (!isDisposed)
              {
                  if (disposing)
                  { }
                  try
                  {
                      if (IsUserCommandValid())
                          myCommand.ExecuteNotify -= new _ICommandEvents_ExecuteNotifyEventHandler(ExecuteCommand);
                      myCommand = null;
                      myAddin = null;
                      dsApp = null;
                  }
                  catch { }
              }
              isDisposed = true;
           }

           ~DSAddinCommand()
           {
              Dispose(false);
           }

      }
```

}

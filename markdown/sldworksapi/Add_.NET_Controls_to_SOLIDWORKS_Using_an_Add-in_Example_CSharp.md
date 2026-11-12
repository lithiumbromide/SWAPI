---
title: "Add .NET Controls to SOLIDWORKS Design using an Add-in Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm"
---

# Add .NET Controls to SOLIDWORKS Design using an Add-in Example (C#)

This example shows how to add .NET controls to FeatureManager, PropertyManager, Task Pane, and model view using an add-in.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 //  1. In Microsoft Visual Studio 2012 or later, create a new project using
 //     the SwCSharpAddin template.
 //  2. Name the project DotNetControlsDemo.
 //  3. Select Debug in the Solution Configurations drop-down list.
 //  4. Click Project > DotNetControlsDemo Properties.
 //     a. On the Application tab, ensure that the Target framework is
 //        .NET Framework 3.0 or later.
 //     b. On the Debug tab, select Start external program and type the
 //        pathname of your SOLIDWORKS Design executable.
 //  5. Save the project.
 //  6. In the Solution Explorer, add the following .NET Framework references:
 //     * PresentationCore
 //     * PresentationFramework
 //     * UIAutomationProvider
 //     * WindowsBase
 //     * WindowsFormsIntegration
 //     * System.Xaml
 //  7. Copy and paste:
 //     a. this into SwAddin.cs.
 //     b. this into UserPMPage.cs.
 //     c. this into PMPHandler.cs.
 //  8. Modify install_dir in SwAddin::WinFormInFeatureMgr to point to your
 //     SOLIDWORKS Design install directory.
 //  9. Add a Windows Presentation Foundation User Control to the project:
 //     a. In the Solution Explorer, right-click the project and click
 //        Add > User Control.
 //     b. Type WPFControl.xaml in Name.
 //     c. Click the User Control (WPF) template.
 //     d. Click Add.
 //     e. Copy and paste this into WPFControl.xaml.
 //     f. Expand WPFControl.xaml in the Solution Explorer and copy
 //        and paste  this into WPFControl.xaml.cs.
 // 10. Add a Windows Forms User Control to the project:
 //     a. In the Solution Explorer, right-click the project and click
 //        Add > User Control.
 //     b. Click Add.
 //     c. Copy and paste this into UserControl1.cs.
 //     d. Expand UserControl1.cs in the Solution Explorer and copy
 //        and paste  this into UserControl1.Designer.cs.
 // 11. Create a Windows Form:
 //     a. In the Solution Explorer, right-click the project and select
 //        Add > Windows Form.
 //     b. Click Add.
 //     c. Copy and paste this into  Form1.cs.
 //     d. Expand Form1.cs in the Solution Explorer and copy
 //        and paste  this into Form1.Designer.cs.
 // 12. Save, clean, and build the project.
 //
 // Postconditions:
 //  1. In SOLIDWORKS Design, click Tools > DotNetControlsDemo > WinFormInTaskPane.
 //  2. Displays a new tab in the Task Pane.
 //  3. Open a model document.
 //  4. Click Tools >  DotNetControlsDemo > UserControlInModelView.
 //  5. Displays a .NET User Control1 tab below the model view.
 //  6. Click Tools >  DotNetControlsDemo > WPFInModelView.
 //  7. Displays a .NET WPF Control tab below the model view.
 //  8. Click Tools >  DotNetControlsDemo > WinFormInFeatureMgr.
 //  9. Displays a new view in a split panel of the FeatureManager design tree.
 // 10. Click Tools >  DotNetControlsDemo > Show PMP.
 // 11. Click OK in each of the three message boxes.
 // 12. Displays a new tab with .NET controls in the PropertyManager.
 //---------------------------------------------------------------------------
//SwAddin.cs
```

```vb
using System;
 using System.Runtime.InteropServices;
 using System.Collections;
 using System.Reflection;
 using System.Diagnostics;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swpublished;
 using SolidWorks.Interop.swconst;
 using SolidWorksTools;
 using SolidWorksTools.File;
 using System.Windows.Forms;
 using System.Windows.Forms.Integration;

 namespace DotNetControlsDemo
 {
     /// <summary>
     /// Summary description for DotNetControlsDemo.
     /// </summary>
     [Guid("4ca45de8-6831-4a4c-83ac-d9d968803794"), ComVisible(true)]
     [SwAddin(
         Description = "DotNetControlsDemo description",
         Title = "DotNetControlsDemo",
         LoadAtStartup = true
         )]
     public class SwAddin : ISwAddin
     {
         #region Local Variables
         ISldWorks iSwApp;
         ICommandManager iCmdMgr;
         ICommandGroup cmdGroup;
         int addinID;
         Form1 TaskPanWinFormControl;
         UserControl1 TaskPanUserControl;
         Form1 FeatureMgrControl;
         UserControl1 ModelView1Control;
         WPFControl WpfModelView1Control;
         ElementHost ModelViewelhost;

         #region Event Handler Variables
         Hashtable openDocs;
         SolidWorks.Interop.sldworks.SldWorks SwEventPtr;
         #endregion

         #region Property Manager Variables
         UserPMPage ppage;
         #endregion

         // Public Properties
         public ISldWorks SwApp
         {
             get { return iSwApp; }
         }
         public ICommandManager CmdMgr
         {
             get { return iCmdMgr; }
         }

         public Hashtable OpenDocs
         {
             get { return openDocs; }
         }

         #endregion

         #region SOLIDWORKS Registration
         [ComRegisterFunctionAttribute]
         public static void RegisterFunction(Type t)
         {

             #region Get Custom Attribute: SwAddinAttribute
             SwAddinAttribute SWattr = null;
             Type type = typeof(SwAddin);
             foreach (System.Attribute attr in type.GetCustomAttributes(false))
             {
                 if (attr is SwAddinAttribute)
                 {
                     SWattr = attr as SwAddinAttribute;
                     break;
                 }
             }
             #endregion

             Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
             Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

             string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
             Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
             addinkey.SetValue(null, 0);

             addinkey.SetValue("Description", SWattr.Description);
             addinkey.SetValue("Title", SWattr.Title);

             keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
             addinkey = hkcu.CreateSubKey(keyname);
             addinkey.SetValue(null, Convert.ToInt32(SWattr.LoadAtStartup), Microsoft.Win32.RegistryValueKind.DWord);
         }

         [ComUnregisterFunctionAttribute]
         public static void UnregisterFunction(Type t)
         {
             Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
             Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

             string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
             hklm.DeleteSubKey(keyname);

             keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
             hkcu.DeleteSubKey(keyname);
         }

         #endregion

         #region ISwAddin Implementation
         public SwAddin()
         {
         }

         public bool ConnectToSW(object ThisSW, int cookie)
         {
             iSwApp = (ISldWorks)ThisSW;
             addinID = cookie;

             //Set up callbacks
             iSwApp.SetAddinCallbackInfo(0, this, addinID);

             #region Setup the Command Manager
             iCmdMgr = iSwApp.GetCommandManager(cookie);
             AddCommandMgr();
             #endregion

             #region Setup the Event Handlers
             SwEventPtr = (SolidWorks.Interop.sldworks.SldWorks)iSwApp;
             openDocs = new Hashtable();
             AttachEventHandlers();
             #endregion

             #region Setup Sample Property Manager
             AddPMP();
             #endregion

             return true;
         }

         public bool DisconnectFromSW()
         {
             RemoveCommandMgr();
             RemovePMP();
             DetachEventHandlers();

             iSwApp = null;
             //The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
             GC.Collect();
             return true;
         }
         #endregion

         #region UI Methods
         public void AddCommandMgr()
         {

             BitmapHandler iBmp = new BitmapHandler();

             Assembly thisAssembly;
             int cmdIndex0, cmdIndex1, cmdIndex2, cmdIndex3, cmdIndex4;
             string Title = "DotNetControlsDemo", ToolTip = "DotNetControlsDemo";

             int[] docTypes = new int[]{(int)swDocumentTypes_e.swDocASSEMBLY,
                                        (int)swDocumentTypes_e.swDocDRAWING,
                                        (int)swDocumentTypes_e.swDocPART};

             thisAssembly = System.Reflection.Assembly.GetAssembly(this.GetType());

             cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip,  "", -1);
             cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("DotNetControlsDemo.ToolbarLarge.bmp", thisAssembly);
             cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("DotNetControlsDemo.ToolbarSmall.bmp", thisAssembly);
             cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("DotNetControlsDemo.MainIconLarge.bmp", thisAssembly);
             cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("DotNetControlsDemo.MainIconSmall.bmp", thisAssembly);

             cmdIndex0 = cmdGroup.AddCommandItem("WinFromInTaskPane", -1, "Add Windows Form In Task Pane", "WinFormInTaskPane", 0, "WinFormInTaskPane", "EnableWinFormInTaskPane", 0);
             cmdIndex1 = cmdGroup.AddCommandItem("UserControlInModelView", -1, "Add User Control In Model View", "UserControlInModelView", 1, "UserControlInModelView", "EnableUserControlInModelView", 1);
             cmdIndex2 = cmdGroup.AddCommandItem("WPFInModelView", -1, "Add WPF In ModelView", "WPFInModelView", 2, "WPFInModelView", "EnableWPFInModelView", 2);
             cmdIndex3 = cmdGroup.AddCommandItem("WinFormInFeatureMgr", -1, "Add Windows Form In FeatureManager design tree", "WinFormInFeatureMgr", 3, "WinFormInFeatureMgr", "EnableWinFormInFeatureMgr", 3);
             cmdIndex4 = cmdGroup.AddCommandItem("Show PMP", -1,  "Display PropertyManager page with .NET Controls", "Show PMP", 4, "ShowPMP", "EnablePMP", 4);

             cmdGroup.HasToolbar = true;
             cmdGroup.HasMenu = true;
             cmdGroup.Activate();

             bool bResult;

             foreach (int type in docTypes)
             {
                 ICommandTab cmdTab;

                 cmdTab = iCmdMgr.GetCommandTab(type, Title);

                 if (cmdTab == null)
                 {
                     cmdTab = (ICommandTab)iCmdMgr.AddCommandTab(type, Title);

                     CommandTabBox cmdBox = cmdTab.AddCommandTabBox();

                     int[] cmdIDs = new int[6];
                     int[] TextType = new int[6];

                     cmdIDs[0] = cmdGroup.get_CommandID(cmdIndex0);
                     TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                     cmdIDs[1] = cmdGroup.get_CommandID(cmdIndex1);
                     TextType[1] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                     cmdIDs[2] = cmdGroup.get_CommandID(cmdIndex2);
                     TextType[2] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                     cmdIDs[3] = cmdGroup.get_CommandID(cmdIndex3);
                     TextType[3] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                     cmdIDs[4] = cmdGroup.get_CommandID(cmdIndex4);
                     TextType[4] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                     cmdIDs[5] = cmdGroup.ToolbarId;
                     TextType[5] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal | (int)swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout;

                     bResult = cmdBox.AddCommands(cmdIDs, TextType);

                     CommandTabBox cmdBox1 = cmdTab.AddCommandTabBox();
                     cmdIDs = new int[1];
                     TextType = new int[1];

                     cmdIDs[0] = cmdGroup.ToolbarId;
                     TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow | (int)swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout;

                     bResult = cmdBox1.AddCommands(cmdIDs, TextType);

                     cmdTab.AddSeparator(cmdBox1, cmdGroup.ToolbarId);

                 }

             }
             thisAssembly = null;
             iBmp.Dispose();
         }

         public void RemoveCommandMgr()
         {
             iCmdMgr.RemoveCommandGroup(1);
         }

         public Boolean AddPMP()
         {
             ppage = new UserPMPage(this);
             return true;
         }

         public Boolean RemovePMP()
         {
             ppage = null;
             return true;
         }

         #endregion

         #region UI Callbacks
         public void WinFormInTaskPane()
         {
               ITaskpaneView pTaskPanView;
               pTaskPanView = iSwApp.CreateTaskpaneView2("", ".NET Windows Form Control");
               TaskPanWinFormControl = new Form1();
               pTaskPanView.DisplayWindowFromHandlex64(TaskPanWinFormControl.Handle.ToInt64());
         }

         public int EnableWinFromInTaskPane()
         {
              return 1;

         }

         public void UserControlInModelView()
         {
             IModelDoc2 pDoc;
             pDoc = (IModelDoc2)iSwApp.ActiveDoc;
             IModelViewManager swModelViewMgr;
             swModelViewMgr = pDoc.ModelViewManager;
             ModelView1Control = new UserControl1();
             swModelViewMgr.DisplayWindowFromHandlex64(".NET User Control1", ModelView1Control.Handle.ToInt64(), false);
         }

         public int EnableUserControlInModelView()
         {
             if (iSwApp.ActiveDoc != null)
                 return 1;
             else
                 return 0;
         }

        public void  WPFInModelView()
        {
            IModelDoc2 pDoc;
            pDoc = (IModelDoc2)iSwApp.ActiveDoc;
            IModelViewManager swModelViewMgr;
            swModelViewMgr = pDoc.ModelViewManager;
            WpfModelView1Control = new WPFControl();

            ModelViewelhost = new ElementHost();
            ModelViewelhost.Child = WpfModelView1Control;
            swModelViewMgr.DisplayWindowFromHandlex64(".NET WPF Control", ModelViewelhost.Handle.ToInt64(), true);
        }

         public int EnableWPFInModelView()
         {
              if (iSwApp.ActiveDoc != null)
                 return 1;
             else
                 return 0;
         }

         public void WinFormInFeatureMgr()
         {
             IModelDoc2 pDoc;
             pDoc = (IModelDoc2)iSwApp.ActiveDoc;
             IModelViewManager swModelViewMgr;
             swModelViewMgr = pDoc.ModelViewManager;
             IFeatMgrView swFeatMgrTabTop;
             FeatureMgrControl = new Form1();
             swFeatMgrTabTop = swModelViewMgr.CreateFeatureMgrWindowFromHandlex64("public_documents\\samples\\tutorial\\api\\addin\\pm_extruded_block.bmp", FeatureMgrControl.Handle.ToInt64(), ".NET Windows Form Control", (int)swFeatMgrPane_e.swFeatMgrPaneTop);
             pDoc.FeatureManagerSplitterPosition = 0.5;
             swFeatMgrTabTop.ActivateView();
         }

        public int EnableWinFormInFeatureMgr()
        {
               if (iSwApp.ActiveDoc != null)
                 return 1;
             else
                 return 0;
        }

         public void ShowPMP()
         {
             if (ppage != null)
                 ppage.Show();
         }

         public int EnablePMP()
         {
             if (iSwApp.ActiveDoc != null)
                 return 1;
             else
                 return 0;
         }
         #endregion

         #region Event Methods
         public bool AttachEventHandlers()
         {
             AttachSwEvents();
             //Listen for events on all currently open docs
             AttachEventsToAllDocuments();
             return true;
         }

         private bool AttachSwEvents()
         {
             try
             {
                 SwEventPtr.ActiveDocChangeNotify +=  new   DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                 SwEventPtr.DocumentLoadNotify2 +=  new  DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                 SwEventPtr.FileNewNotify2 +=  new  DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                 SwEventPtr.ActiveModelDocChangeNotify +=  new   DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                 SwEventPtr.FileOpenPostNotify +=  new  DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                 return true;
             }
             catch (Exception e)
             {
                 Console.WriteLine(e.Message);
                 return false;
             }
         }

         private bool DetachSwEvents()
         {
             try
             {
                 SwEventPtr.ActiveDocChangeNotify -=  new   DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                 SwEventPtr.DocumentLoadNotify2 -=  new  DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                 SwEventPtr.FileNewNotify2 -=  new  DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                 SwEventPtr.ActiveModelDocChangeNotify -=  new   DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                 SwEventPtr.FileOpenPostNotify -=  new  DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                 return true;
             }
             catch (Exception e)
             {
                 Console.WriteLine(e.Message);
                 return false;
             }

         }

         public void AttachEventsToAllDocuments()
         {
             ModelDoc2 modDoc = (ModelDoc2)iSwApp.GetFirstDocument();
             while (modDoc != null)
             {
                 if (!openDocs.Contains(modDoc))
                 {
                     AttachModelDocEventHandler(modDoc);
                 }
                 modDoc = (ModelDoc2)modDoc.GetNext();
             }
         }

         public bool AttachModelDocEventHandler(ModelDoc2 modDoc)
         {
             if (modDoc == null)
                 return false;

             DocumentEventHandler docHandler = null;

             if (!openDocs.Contains(modDoc))
             {
                 switch (modDoc.GetType())
                 {
                     case (int)swDocumentTypes_e.swDocPART:
                         {
                             docHandler = new PartEventHandler(modDoc, this);
                             break;
                         }
                     case (int)swDocumentTypes_e.swDocASSEMBLY:
                         {
                             docHandler = new AssemblyEventHandler(modDoc, this);
                             break;
                         }
                     case (int)swDocumentTypes_e.swDocDRAWING:
                         {
                             docHandler = new DrawingEventHandler(modDoc, this);
                             break;
                         }
                     default:
                         {
                             return false; //Unsupported document type
                         }
                 }
                 docHandler.AttachEventHandlers();
                 openDocs.Add(modDoc, docHandler);
             }
             return true;
         }

         public bool DetachModelEventHandler(ModelDoc2 modDoc)
         {
             DocumentEventHandler docHandler;
             docHandler = (DocumentEventHandler)openDocs[modDoc];
             openDocs.Remove(modDoc);
             modDoc = null;
             docHandler = null;
             return true;
         }

         public bool DetachEventHandlers()
         {
             DetachSwEvents();

             //Close events on all currently open docs
             DocumentEventHandler docHandler;
             int numKeys = openDocs.Count;
             object[] keys = new Object[numKeys];

             //Remove all document event handlers
             openDocs.Keys.CopyTo(keys, 0);
             foreach (ModelDoc2 key in keys)
             {
                 docHandler = (DocumentEventHandler)openDocs[key];
                 docHandler.DetachEventHandlers();  //This also removes the pair from the hash
                 docHandler =  null;
             }
             return true;
         }
         #endregion

         #region Event Handlers
         //Events
         public int OnDocChange()
         {
             return 0;
         }

         public int OnDocLoad(string docTitle, string docPath)
         {
             return 0;
         }

         int FileOpenPostNotify(string FileName)
         {
             AttachEventsToAllDocuments();
             return 0;
         }

         public int OnFileNew(object newDoc, int docType, string templateName)
         {
             AttachEventsToAllDocuments();
             return 0;
         }

         public int OnModelChange()
         {
             return 0;
         }

         #endregion
     }

 }
```

```vb
Back to top
//UserPMPage.cs
```

```vb
using System;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swpublished;
 using SolidWorks.Interop.swconst;
 using System.Windows.Forms;

 using System.Windows.Forms.Integration;

 namespace DotNetControlsDemo
 {
     public class UserPMPage
     {
         //Local Objects
         IPropertyManagerPage2 swPropertyPage;
         PMPHandler handler;
         ISldWorks iSwApp;
         SwAddin userAddin;

         WPFControl MyWPFControl;
         ElementHost elhost;
         UserControl1 MyUserControl;
         Form1 MyWinFormControl;

         #region Property Manager Page Controls
         //Groups
         IPropertyManagerPageGroup group1;
         IPropertyManagerPageGroup group2;
         IPropertyManagerPageGroup group3;

         //Controls
         IPropertyManagerPageWindowFromHandle dotnet1;
         IPropertyManagerPageWindowFromHandle dotnet2;
         IPropertyManagerPageWindowFromHandle dotnet3;

         //Control IDs
         public const int group1ID = 0;
         public const int group2ID = 1;
         public const int group3ID = 2;

         public const int DotNet1ID = 3;
         public const int DotNet2ID = 4;
         public const int DotNet3ID = 5;

         #endregion

         public UserPMPage(SwAddin addin)
         {
             userAddin = addin;
             iSwApp = (ISldWorks)userAddin.SwApp;
             CreatePropertyManagerPage();
         }

         protected void CreatePropertyManagerPage()
         {
             int errors = -1;
             int options = (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_OkayButton |
                 (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_CancelButton;

             handler = new PMPHandler(userAddin);
             swPropertyPage = (IPropertyManagerPage2)iSwApp.CreatePropertyManagerPage(".Net PMP control", options, handler, ref errors);
             if (swPropertyPage != null && errors == (int)swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay)
             {
                 try
                 {
                     AddControls();
                 }
                 catch (Exception e)
                 {
                     iSwApp.SendMsgToUser2(e.Message, 0, 0);
                 }
             }
         }

         //Controls display on the page top to bottom in the order
         //in which they are added to the page
         protected void AddControls()
         {
             short controlType = -1;
             short align = -1;
             int options = -1;

             //Add the groups
             options = (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded |
                       (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible;

             group1 = (IPropertyManagerPageGroup)swPropertyPage.AddGroupBox(group1ID, "Windows Form controls", options);

             options = (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Checkbox |
                       (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible;

             group2 = (IPropertyManagerPageGroup)swPropertyPage.AddGroupBox(group2ID, "User controls", options);

             options =  (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Checkbox |
                         (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible;

             group3 = (IPropertyManagerPageGroup)swPropertyPage.AddGroupBox(group3ID, "WPF controls", options);

             controlType = (int)swPropertyManagerPageControlType_e.swControlType_WindowFromHandle;
             align = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge;
             options = (int)swAddControlOptions_e.swControlOptions_Enabled |
                       (int)swAddControlOptions_e.swControlOptions_Visible;

             dotnet1 = (IPropertyManagerPageWindowFromHandle )group1.AddControl2(DotNet1ID, controlType, ".Net Windows Form control", align, options, "This control is added without COM");
             dotnet1.Height = 150;

             controlType = (int)swPropertyManagerPageControlType_e.swControlType_WindowFromHandle;
             align = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge;
             options = (int)swAddControlOptions_e.swControlOptions_Enabled |
                       (int)swAddControlOptions_e.swControlOptions_Visible;

             dotnet2 = (IPropertyManagerPageWindowFromHandle )group2.AddControl2(DotNet2ID, controlType, ".Net user form control", align, options, "This control is added without COM");
             dotnet2.Height = 150;

             dotnet3 = (IPropertyManagerPageWindowFromHandle )group3.AddControl2(DotNet3ID, controlType, ".Net WPF control", align, options, "This control is added without COM");
             dotnet3.Height = 50;

         }

         public void Show()
         {

             //Windows Form control
             MyWinFormControl =  new  Form1();
             //If you are adding Windows form in the PropertyManager Page, set TopLevel to false
             MyWinFormControl.TopLevel = false;
             MyWinFormControl.Show();
              dotnet1.SetWindowHandlex64(MyWinFormControl.Handle.ToInt64());

             //User control
              MyUserControl =  new  UserControl1();
             dotnet2.SetWindowHandlex64(MyUserControl.Handle.ToInt64());

             //WPF control
             elhost =  new  ElementHost();
             MyWPFControl = new WPFControl();
             elhost.Child = MyWPFControl;
             dotnet3.SetWindowHandlex64(elhost.Handle.ToInt64());

             //Show PropertyManager page
             swPropertyPage.Show();

         }
     }
 }

Back to top
```

```vb
//PMPHandler.cs
```

```vb
using System;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swpublished;
 using System.Windows.Forms;

 namespace DotNetControlsDemo
 {

     public class PMPHandler : IPropertyManagerPage2Handler9
     {
         ISldWorks iSwApp;
         SwAddin userAddin;

         public PMPHandler(SwAddin addin)
         {
             userAddin = addin;
             iSwApp = (ISldWorks)userAddin.SwApp;
         }

         //Implement these methods from the interface
         public void AfterClose()
         {
             //This function must contain code, even if it does nothing, to prevent the
             //.NET runtime environment from doing garbage collection at the wrong time.
             int IndentSize;
             IndentSize = System.Diagnostics.Debug.IndentSize;
             System.Diagnostics.Debug.WriteLine(IndentSize);
         }

         public void OnCheckboxCheck(int id, bool status)
         {

         }

         public void OnClose(int reason)
         {
             //This function must contain code, even if it does nothing, to prevent the
             //.NET runtime environment from doing garbage collection at the wrong time.
             int IndentSize;
             IndentSize = System.Diagnostics.Debug.IndentSize;
             System.Diagnostics.Debug.WriteLine(IndentSize);
         }

         public void OnComboboxEditChanged(int id, string text)
         {

         }

         public int OnActiveXControlCreated(int id, bool status)
         {
             return -1;
         }

         public void OnButtonPress(int id)
         {

         }

         public void OnComboboxSelectionChanged(int id, int item)
         {

         }

         public void OnGroupCheck(int id, bool status)
         {

         }

         public void OnGroupExpand(int id, bool status)
         {

         }

         public bool OnHelp()
         {
             return true;
         }

         public void OnListboxSelectionChanged(int id, int item)
         {

         }

         public bool OnNextPage()
         {
             return true;
         }

         public void OnNumberboxChanged(int id, double val)
         {

         }

         public void OnOptionCheck(int id)
         {

         }

         public bool OnPreviousPage()
         {
             return true;
         }

         public void OnSelectionboxCalloutCreated(int id)
         {

         }

         public void OnSelectionboxCalloutDestroyed(int id)
         {

         }

         public void OnSelectionboxFocusChanged(int id)
         {

         }

         public void OnSelectionboxListChanged(int id, int item)
         {

         }

         public void OnTextboxChanged(int id, string text)
         {

         }

         public void AfterActivation()
         {

         }

         public bool OnKeystroke(int Wparam, int Message, int Lparam, int Id)
         {
             return true;
         }

         public void OnPopupMenuItem(int Id)
         {

         }

         public void OnPopupMenuItemUpdate(int Id, ref int retval)
         {

         }

         public bool OnPreview()
         {
             return true;
         }

         public void OnSliderPositionChanged(int Id, double Value)
         {

         }

         public void OnSliderTrackingCompleted(int Id, double Value)
         {

         }

         public bool OnSubmitSelection(int Id, object Selection, int SelType, ref string ItemText)
         {
             return true;
         }

         public bool OnTabClicked(int Id)
         {
             return true;
         }

         public void OnUndo()
         {

         }

         public void OnWhatsNew()
         {

         }

         public void OnRedo()
         {

         }

         public void OnGainedFocus(int Id)
         {

         }

         public void OnLostFocus(int Id)
         {

         }

         public int OnWindowFromHandleControlCreated(int id, bool status)
         {
             System.Windows.Forms.MessageBox.Show(".NET control created");
             return -1;
         }
         public void OnListboxRMBUp(int Id, int PosX, int PosY)
         {

         }

         public void OnNumberBoxTrackingCompleted(int Id, double Value)
         {

         }

     }
 }
```

```vb
Back to top

//Form1.cs
 using System;
 using System.Collections.Generic;
 using System.ComponentModel;
 using System.Data;
 using System.Drawing;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;

 namespace DotNetControlsDemo
 {
     public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
         }

         private void button1_Click(object sender, EventArgs e)
         {

         }

         private void textBox1_TextChanged(object sender, EventArgs e)
         {

         }

         private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
         {

         }

         private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
         {

         }
     }
 }

Back to top

//Form1.Designer.cs
```

```vb
 namespace DotNetControlsDemo
 {
     partial class Form1
     {
         /// <summary>
         /// Required designer variable.
         /// </summary>
         private System.ComponentModel.IContainer components = null;

         /// <summary>
         /// Clean up any resources being used.
         /// </summary>
         /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
         protected override void Dispose(bool disposing)
         {
             if (disposing && (components != null))
             {
                 components.Dispose();
             }
             base.Dispose(disposing);
         }

         #region Windows Form Designer generated code

         /// <summary>
         /// Required method for Designer support - do not modify
         /// the contents of this method with the code editor.
         /// </summary>
         private void InitializeComponent()
         {
             this.listBox1 = new System.Windows.Forms.ListBox();
             this.comboBox1 = new System.Windows.Forms.ComboBox();
             this.textBox1 = new System.Windows.Forms.TextBox();
             this.button1 = new System.Windows.Forms.Button();
             this.SuspendLayout();
             //
             // listBox1
             //
             this.listBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
             | System.Windows.Forms.AnchorStyles.Right)));
             this.listBox1.FormattingEnabled = true;
             this.listBox1.Items.AddRange(new object[] {
             "Help",
             "Whats New"});
             this.listBox1.Location = new System.Drawing.Point(25, 160);
             this.listBox1.Name = "listBox1";
             this.listBox1.Size = new System.Drawing.Size(304, 43);
             this.listBox1.TabIndex = 10;
             this.listBox1.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged);
             //
             // comboBox1
             //
             this.comboBox1.DisplayMember = "Monday";
             this.comboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
             this.comboBox1.FormattingEnabled = true;
             this.comboBox1.Items.AddRange(new object[] {
             "Monday ",
             "Tuesday",
             "Wednesday",
             "Thursday",
             "Friday",
             "Saturday",
             "Sunday"});
             this.comboBox1.Location = new System.Drawing.Point(25, 122);
             this.comboBox1.Name = "comboBox1";
             this.comboBox1.Size = new System.Drawing.Size(140, 21);
             this.comboBox1.TabIndex = 9;
             this.comboBox1.ValueMember = "Monday";
             this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
             //
             // textBox1
             //
             this.textBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
             | System.Windows.Forms.AnchorStyles.Left)
             | System.Windows.Forms.AnchorStyles.Right)));
             this.textBox1.Location = new System.Drawing.Point(25, 86);
             this.textBox1.Name = "textBox1";
             this.textBox1.Size = new System.Drawing.Size(321, 20);
             this.textBox1.TabIndex = 8;
             this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
             //
             // button1
             //
             this.button1.Location = new System.Drawing.Point(25, 12);
             this.button1.Name = "button1";
             this.button1.Size = new System.Drawing.Size(140, 57);
             this.button1.TabIndex = 7;
             this.button1.Text = "Say Hello";
             this.button1.UseVisualStyleBackColor = true;
             this.button1.Click += new System.EventHandler(this.button1_Click);
             //
             // Form1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.ClientSize = new System.Drawing.Size(382, 215);
             this.ControlBox = false;
             this.Controls.Add(this.listBox1);
             this.Controls.Add(this.comboBox1);
             this.Controls.Add(this.textBox1);
             this.Controls.Add(this.button1);
             this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
             this.MaximizeBox = false;
             this.MinimizeBox = false;
             this.Name = "Form1";
             this.ShowIcon = false;
             this.ShowInTaskbar = false;
             this.Text = "Form1";
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.ListBox listBox1;
         private System.Windows.Forms.ComboBox comboBox1;
         private System.Windows.Forms.TextBox textBox1;
         private System.Windows.Forms.Button button1;
     }
 }

Back to top

 //UserControl1.cs
```

```vb
 using System;
 using System.Drawing;
 using System.Data;
 using System.Linq;
 using System.Text;
 using System.Windows.Forms;

 namespace DotNetControlsDemo
 {
     public partial class UserControl1 : UserControl
     {
         public UserControl1()
         {
             InitializeComponent();
         }

         private void button1_Click(object sender, EventArgs e)
         {

         }

         private void textBox1_TextChanged(object sender, EventArgs e)
         {

         }

         private void radioButton1_CheckedChanged(object sender, EventArgs e)
         {

         }

         private void TabPage1_Click(object sender, EventArgs e)
         {

         }

         private void TabPage2_Click(object sender, EventArgs e)
         {

         }

         private void TabPage3_Click(object sender, EventArgs e)
         {

         }
     }
 }

Back to top

//UserControl1.Designer.cs
```

```vb
 namespace DotNetControlsDemo
 {
     partial class UserControl1
     {
         /// <summary>
         /// Required designer variable.
         /// </summary>
         private System.ComponentModel.IContainer components = null;

         /// <summary>
         /// Clean up any resources being used.
         /// </summary>
         /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
         protected override void Dispose(bool disposing)
         {
             if (disposing && (components != null))
             {
                 components.Dispose();
             }
             base.Dispose(disposing);
         }

         #region Component Designer generated code

         /// <summary>
         /// Required method for Designer support - do not modify
         /// the contents of this method with the code editor.
         /// </summary>
         private void InitializeComponent()
         {
             this.radioButton1 = new System.Windows.Forms.RadioButton();
             this.textBox1 = new System.Windows.Forms.TextBox();
             this.button1 = new System.Windows.Forms.Button();
             this.tabControl1 = new System.Windows.Forms.TabControl();
             this.TabPage1 = new System.Windows.Forms.TabPage();
             this.TabPage2 = new System.Windows.Forms.TabPage();
             this.TabPage3 = new System.Windows.Forms.TabPage();
             this.tabControl1.SuspendLayout();
             this.SuspendLayout();
             //
             // radioButton1
             //
             this.radioButton1.Anchor = System.Windows.Forms.AnchorStyles.Left;
             this.radioButton1.AutoSize = true;
             this.radioButton1.Location = new System.Drawing.Point(23, 113);
             this.radioButton1.Name = "radioButton1";
             this.radioButton1.Size = new System.Drawing.Size(85, 17);
             this.radioButton1.TabIndex = 5;
             this.radioButton1.TabStop = true;
             this.radioButton1.Text = "radioButton1";
             this.radioButton1.UseVisualStyleBackColor = true;
             this.radioButton1.CheckedChanged += new System.EventHandler(this.radioButton1_CheckedChanged);
             //
             // textBox1
             //
             this.textBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
             | System.Windows.Forms.AnchorStyles.Right)));
             this.textBox1.Location = new System.Drawing.Point(23, 87);
             this.textBox1.Name = "textBox1";
             this.textBox1.Size = new System.Drawing.Size(378, 20);
             this.textBox1.TabIndex = 4;
             this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
             //
             // button1
             //
             this.button1.Location = new System.Drawing.Point(23, 17);
             this.button1.Name = "button1";
             this.button1.Size = new System.Drawing.Size(119, 49);
             this.button1.TabIndex = 3;
             this.button1.Text = "Say Hello";
             this.button1.UseVisualStyleBackColor = true;
             this.button1.Click += new System.EventHandler(this.button1_Click);
             //
             // tabControl1
             //
             this.tabControl1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
             | System.Windows.Forms.AnchorStyles.Right)));
             this.tabControl1.Controls.Add(this.TabPage1);
             this.tabControl1.Controls.Add(this.TabPage2);
             this.tabControl1.Controls.Add(this.TabPage3);
             this.tabControl1.Location = new System.Drawing.Point(23, 148);
             this.tabControl1.Multiline = true;
             this.tabControl1.Name = "tabControl1";
             this.tabControl1.SelectedIndex = 0;
             this.tabControl1.Size = new System.Drawing.Size(386, 69);
             this.tabControl1.TabIndex = 6;
             //
             // TabPage1
             //
             this.TabPage1.Location = new System.Drawing.Point(4, 22);
             this.TabPage1.Name = "TabPage1";
             this.TabPage1.Padding = new System.Windows.Forms.Padding(3);
             this.TabPage1.Size = new System.Drawing.Size(378, 43);
             this.TabPage1.TabIndex = 0;
             this.TabPage1.Text = "TabPage1";
             this.TabPage1.UseVisualStyleBackColor = true;
             this.TabPage1.Click += new System.EventHandler(this.TabPage1_Click);
             //
             // TabPage2
             //
             this.TabPage2.Location = new System.Drawing.Point(4, 22);
             this.TabPage2.Name = "TabPage2";
             this.TabPage2.Padding = new System.Windows.Forms.Padding(3);
             this.TabPage2.Size = new System.Drawing.Size(378, 43);
             this.TabPage2.TabIndex = 1;
             this.TabPage2.Text = "TabPage2";
             this.TabPage2.UseVisualStyleBackColor = true;
             this.TabPage2.Click += new System.EventHandler(this.TabPage2_Click);
             //
             // TabPage3
             //
             this.TabPage3.Location = new System.Drawing.Point(4, 22);
             this.TabPage3.Name = "TabPage3";
             this.TabPage3.Padding = new System.Windows.Forms.Padding(3);
             this.TabPage3.Size = new System.Drawing.Size(378, 43);
             this.TabPage3.TabIndex = 2;
             this.TabPage3.Text = "TabPage3";
             this.TabPage3.UseVisualStyleBackColor = true;
             this.TabPage3.Click += new System.EventHandler(this.TabPage3_Click);
             //
             // UserControl1
             //
             this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
             this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
             this.Controls.Add(this.tabControl1);
             this.Controls.Add(this.radioButton1);
             this.Controls.Add(this.textBox1);
             this.Controls.Add(this.button1);
             this.Name = "UserControl1";
             this.Size = new System.Drawing.Size(427, 237);
             this.tabControl1.ResumeLayout(false);
             this.ResumeLayout(false);
             this.PerformLayout();

         }

         #endregion

         private System.Windows.Forms.RadioButton radioButton1;
         private System.Windows.Forms.TextBox textBox1;
         private System.Windows.Forms.Button button1;
         private System.Windows.Forms.TabControl tabControl1;
         private System.Windows.Forms.TabPage TabPage1;
         private System.Windows.Forms.TabPage TabPage2;
         private System.Windows.Forms.TabPage TabPage3;
     }
 }

Back to top
```

```vb
//WPFControl.xaml
```

```vb
<UserControl x:Class="DotNetControlsDemo.WPFControl"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Height="204" Width="314" Loaded="UserControl_Loaded">
     <Grid Height="44" Width="108">
         <ComboBox Text="WPF" Height="44" VerticalAlignment="Top">
             <ComboBoxItem Margin="2">
                 <Ellipse Width="20" Height="20" Stroke="Black" />
             </ComboBoxItem>
             <ComboBoxItem Margin="2">
                 <Path Stroke="Black" Data="M 0,0 L 20,0 L 10,20 Z" />
             </ComboBoxItem>
             <ComboBoxItem Margin="2">
                 <Rectangle Stroke="Black" Width="20" Height="20" />
             </ComboBoxItem>
         </ComboBox>
     </Grid>

 </UserControl>
```

```vb
Back to top

//WPFControl.xaml.cs
```

```vb
using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Windows;
 using System.Windows.Controls;
 using System.Windows.Data;
 using System.Windows.Documents;
 using System.Windows.Input;
 using System.Windows.Media;
 using System.Windows.Media.Imaging;
 using System.Windows.Navigation;
 using System.Windows.Shapes;

 namespace DotNetControlsDemo
 {
     /// <summary>
     /// Interaction logic for WPFControl.xaml
     /// </summary>
     public partial class WPFControl : UserControl
     {
         public WPFControl()
         {
             InitializeComponent();
         }

         private void UserControl_Loaded(object sender, RoutedEventArgs e)
         {

         }
     }
 }
```

```vb
Back to top
```

---
title: "Add .NET Controls to SOLIDWORKS Design using an Add-in Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm"
---

# Add .NET Controls to SOLIDWORKS Design using an Add-in Example (VB.NET)

This example shows how to add .NET controls to FeatureManager, PropertyManager, Task Pane, and model view using an add-in.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  '  1. In Microsoft Visual Studio 2012 or later, create a new project using
 '     the SwVBAddin template.
 '  2. Name the project VBDotNetControlsDemo.
 '  3. Select Debug in the Solution Configurations drop-down list.
 '  4. Click Project > VBDotNetControlsDemo Properties.
  '     a. On the Application tab, verify that Target framework is
 '        .NET Framework 3.0 or later.
 '     b. On the Debug tab, select Start external program and type the
 '        pathname of your SOLIDWORKS Design executable.
 '  5. Save the project.
  '  6. In the Solution Explorer, add the following .NET Framework references:
 '     * PresentationCore
 '     * PresentationFramework
 '     * UIAutomationProvider
 '     * WindowsBase
 '     * WindowsFormsIntegration
 '     * System.Xaml
 '  7. Copy and paste:
 '     a. this into SwAddin.vb.
 '     b. this into UserPMPage.vb.
 '     c. this into PMPHandler.vb.
 '  8. Modify install_dir in SwAddin::WinFormInFeatureMgr to point to your
 '     SOLIDWORKS Design install directory.
  '  9. Add a Windows Presentation Foundation User Control to the project:
  '     a. In the Solution Explorer, right-click the project and click
 '        Add > User Control.
 '     b. Type WPFControl.xaml in Name.
 '     c. Click the User Control (WPF) template.
 '     d. Click Add.
 '     e. Copy and paste this into WPFControl.xaml.
 '     f. Expand  WPFControl.xaml in the Solution Explorer and copy
 '         and paste this into WPFControl.xaml.vb.
 ' 10. Add a Windows Forms User Control to the project:
  '     a. In the Solution Explorer, right-click the project and click
 '        Add > User Control.
 '     b. Click Add.
 '     c. Copy and paste this into UserControl1.vb.
 '     d. Expand  UserControl1.vb in the Solution Explorer and copy
 '        and paste this into UserControl1.Designer.vb.
 ' 11. Create a Windows Form:
  '     a. In the Solution Explorer, right-click the project and select
 '        Add > Windows Form.
 '     b. Click Add.
 '     c. Copy and paste this into Form1.vb.
 '     d. Expand Form1.vb in the Solution Explorer and copy
 '        and paste this into Form1.Designer.vb.
 ' 12. Save, clean, and build the project.
 '
 ' Postconditions:
 '  1. In SOLIDWORKS Design, click Tools > VBDotNetControlsDemo > WinFormInTaskPane.
  '  2. Displays a new tab with .NET controls in the Task Pane.
 '  3. Open a model document.
 '  4. Click Tools > VBDotNetControlsDemo > UserControlInModelView.
 '  5. Displays a .NET User Control1 tab below the model view.
 '  6. Click Tools > VBDotNetControlsDemo > WPFInModelView.
 '  7. Displays a .NET WPF Control tab below the model view.
 '  8. Click Tools > VBDotNetControlsDemo > WinFormInFeatureMgr.
 '  9. Displays a new view in a split panel of the FeatureManager design tree.
 ' 10. Click Tools > VBDotNetControlsDemo > Show PMP.
 ' 11. Click OK in each of the three message boxes.
 ' 12. Displays a new tab with .NET controls in the PropertyManager.
  '---------------------------------------------------------------------------
 'SwAddin.vb
 Imports System
 Imports System.Collections
 Imports System.Reflection
 Imports System.Runtime.InteropServices

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports SolidWorksTools
 Imports SolidWorksTools.File
 Imports System.Windows.Forms
 Imports System.Windows.Forms.Integration

 Imports System.Collections.Generic
 Imports System.Diagnostics

 <Guid("1bce57ff-da20-460b-9c88-32f62e819510")> _
     <ComVisible(True)> _
     <SwAddin( _
         Description:="VBDotNetControlsDemo description", _
         Title:="VBDotNetControlsDemo ", _
         LoadAtStartup:=True _
         )> _
         Public Class SwAddin
     Implements SolidWorks.Interop.swpublished.SwAddin

 #Region "Local Variables"
     Dim WithEvents iSwApp As SldWorks
     Dim iCmdMgr As ICommandManager
     Dim cmdGroup As ICommandGroup
     Dim addinID As Integer
     Dim openDocs As Hashtable
     Dim SwEventPtr As SldWorks
     Dim ppage As UserPMPage
     Dim iBmp As BitmapHandler
     Dim TaskPanWinFormControl As Form1
     Dim TaskPanUserControl As UserControl1
     Dim FeatureMgrControl As Form1
     Dim ModelView1Control As UserControl1
     Dim WpfModelView1Control As WPFControl
     Dim ModelViewelhost As ElementHost

 #Region "Event Handler Variables"
     Dim m_openDocs As Hashtable
 #End Region

     ' Public Properties
     ReadOnly Property SwApp() As SldWorks
         Get
             Return iSwApp
         End Get
     End Property

     ReadOnly Property CmdMgr() As ICommandManager
         Get
             Return iCmdMgr
         End Get
     End Property

     ReadOnly Property OpenDocumentsTable() As Hashtable
         Get
             Return openDocs
         End Get
     End Property
 #End Region

 #Region "SolidWorks Registration"

     <ComRegisterFunction()> Public Shared Sub RegisterFunction(ByVal t As Type)

         ' Get Custom Attribute: SwAddinAttribute
         Dim attributes() As Object
         Dim SWattr As SwAddinAttribute = Nothing

         attributes = System.Attribute.GetCustomAttributes(GetType(SwAddin), GetType(SwAddinAttribute))

         If attributes.Length > 0 Then
             SWattr = DirectCast(attributes(0), SwAddinAttribute)
         End If
         Try
             Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
             Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

             Dim keyname As String = "SOFTWARE\SolidWorks\Addins\{" + t.GUID.ToString() + "}"
             Dim addinkey As Microsoft.Win32.RegistryKey = hklm.CreateSubKey(keyname)
             addinkey.SetValue(Nothing, 0)
             addinkey.SetValue("Description", SWattr.Description)
             addinkey.SetValue("Title", SWattr.Title)

             keyname = "Software\SolidWorks\AddInsStartup\{" + t.GUID.ToString() + "}"
             addinkey = hkcu.CreateSubKey(keyname)
             addinkey.SetValue(Nothing, SWattr.LoadAtStartup, Microsoft.Win32.RegistryValueKind.DWord)
         Catch nl As System.NullReferenceException
             Console.WriteLine("There was a problem registering this dll: SWattr is null.\n " & nl.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: SWattr is null.\n" & nl.Message)
         Catch e As System.Exception
             Console.WriteLine("There was a problem registering this dll: " & e.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: " & e.Message)
         End Try
     End Sub

     <ComUnregisterFunction()> Public Shared Sub UnregisterFunction(ByVal t As Type)
         Try
             Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
             Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

             Dim keyname As String = "SOFTWARE\SolidWorks\Addins\{" + t.GUID.ToString() + "}"
             hklm.DeleteSubKey(keyname)

             keyname = "Software\SolidWorks\AddInsStartup\{" + t.GUID.ToString() + "}"
             hkcu.DeleteSubKey(keyname)
         Catch nl As System.NullReferenceException
             Console.WriteLine("There was a problem unregistering this dll: SWattr is null.\n " & nl.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: SWattr is null.\n" & nl.Message)
         Catch e As System.Exception
             Console.WriteLine("There was a problem unregistering this dll: " & e.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: " & e.Message)
         End Try

     End Sub

 #End Region

 #Region "ISwAddin Implementation"

     Function ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Integer) As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.ConnectToSW
         iSwApp = ThisSW
         addinID = Cookie

         ' Set up callbacks
         iSwApp.SetAddinCallbackInfo(0, Me, addinID)

         ' Setup the Command Manager
         iCmdMgr = iSwApp.GetCommandManager(Cookie)
         AddCommandMgr()

         'Setup the Event Handlers
         SwEventPtr = iSwApp
         openDocs = New Hashtable
         AttachEventHandlers()

         'Setup Sample Property Manager
         AddPMP()

         ConnectToSW = True
     End Function

     Function DisconnectFromSW() As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.DisconnectFromSW

         RemoveCommandMgr()
         RemovePMP()
         DetachEventHandlers()

         System.Runtime.InteropServices.Marshal.ReleaseComObject(iCmdMgr)
         iCmdMgr = Nothing
         System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp)
         iSwApp = Nothing
         'The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
         GC.Collect()
         GC.WaitForPendingFinalizers()

         GC.Collect()
         GC.WaitForPendingFinalizers()

         DisconnectFromSW = True
     End Function
 #End Region

 #Region "UI Methods"
     Public Sub AddCommandMgr()

         Dim iBmp As New BitmapHandler()

         Dim thisAssembly As Assembly
         Dim cmdIndex0 As Integer, cmdIndex1 As Integer, cmdIndex2 As Integer, cmdIndex3 As Integer, cmdIndex4 As Integer
         Dim Title As String = "VBDotNetControlsDemo ", ToolTip As String = "VBDotNetControlsDemo "

         Dim docTypes As Integer() = New Integer() {swDocumentTypes_e.swDocASSEMBLY, swDocumentTypes_e.swDocDRAWING), swDocumentTypes_e.swDocPART

         thisAssembly = System.Reflection.Assembly.GetAssembly(Me.[GetType]())

         cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip, "", -1)
         cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("VBDotNetControlsDemo .ToolbarLarge.bmp", thisAssembly)
         cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("VBDotNetControlsDemo .ToolbarSmall.bmp", thisAssembly)
         cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("VBDotNetControlsDemo .MainIconLarge.bmp", thisAssembly)
         cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("VBDotNetControlsDemo .MainIconSmall.bmp", thisAssembly)

         cmdIndex0 = cmdGroup.AddCommandItem("WinFromInTaskPane", -1, "Add Windows Form In Task Pane", "WinFormInTaskPane", 0, "WinFormInTaskPane", _
             "EnableWinFormInTaskPane", 0)
         cmdIndex1 = cmdGroup.AddCommandItem("UserControlInModelView", -1, "Add User Control In Model View", "UserControlInModelView", 1, "UserControlInModelView", _
             "EnableUserControlInModelView", 1)
         cmdIndex2 = cmdGroup.AddCommandItem("WPFInModelView", -1, "Add WPF In ModelView", "WPFInModelView", 2, "WPFInModelView", _
             "EnableWPFInModelView", 2)
         cmdIndex3 = cmdGroup.AddCommandItem("WinFormInFeatureMgr", -1, "Add Windows Form In FeatureManager design tree", "WinFormInFeatureMgr", 3, "WinFormInFeatureMgr", _
             "EnableWinFormInFeatureMgr", 3)
         cmdIndex4 = cmdGroup.AddCommandItem("Show PMP", -1, "Display PropertyManager page with .NET Controls", "Show PMP", 4, "ShowPMP", _
             "EnablePMP", 4)

         cmdGroup.HasToolbar = True
         cmdGroup.HasMenu = True
         cmdGroup.Activate()

         Dim bResult As Boolean

         For Each type As Integer In docTypes
             Dim cmdTab As ICommandTab

             cmdTab = iCmdMgr.GetCommandTab(type, Title)

             If cmdTab Is Nothing Then
                 cmdTab = DirectCast(iCmdMgr.AddCommandTab(type, Title), ICommandTab)

                 Dim cmdBox As CommandTabBox = cmdTab.AddCommandTabBox()

                 Dim cmdIDs As Integer() = New Integer(5) {}
                 Dim TextType As Integer() = New Integer(5) {}

                 cmdIDs(0) = cmdGroup.CommandID(cmdIndex0)
                 TextType(0) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 cmdIDs(1) = cmdGroup.CommandID(cmdIndex1)
                 TextType(1) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 cmdIDs(2) = cmdGroup.CommandID(cmdIndex2)
                 TextType(2) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 cmdIDs(3) = cmdGroup.CommandID(cmdIndex3)
                 TextType(3) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 cmdIDs(4) = cmdGroup.CommandID(cmdIndex4)
                 TextType(4) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 cmdIDs(5) = cmdGroup.ToolbarId
                 TextType(5) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal Or swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout

                 bResult = cmdBox.AddCommands(cmdIDs, TextType)

                 Dim cmdBox1 As CommandTabBox = cmdTab.AddCommandTabBox()
                 cmdIDs = New Integer(0) {}
                 TextType = New Integer(0) {}

                 cmdIDs(0) = cmdGroup.ToolbarId
                 TextType(0) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow Or swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout

                 bResult = cmdBox1.AddCommands(cmdIDs, TextType)

                 cmdTab.AddSeparator(cmdBox1, cmdGroup.ToolbarId)

             End If
         Next
         thisAssembly = Nothing
         iBmp.Dispose()
     End Sub

     Public Sub RemoveCommandMgr()
         iCmdMgr.RemoveCommandGroup(1)
     End Sub

     Public Function AddPMP() As [Boolean]
         ppage = New UserPMPage(Me)
         Return True
     End Function

     Public Function RemovePMP() As [Boolean]
         ppage = Nothing
         Return True
     End Function

 #End Region

 #Region "UI Callbacks"
     Public Sub WinFormInTaskPane()
         Dim pTaskPanView As ITaskpaneView
         pTaskPanView = iSwApp.CreateTaskpaneView2("", ".NET Windows Form Control")
         TaskPanWinFormControl = New Form1()
         pTaskPanView.DisplayWindowFromHandlex64(TaskPanWinFormControl.Handle.ToInt64())
     End Sub

     Public Function EnableWinFromInTaskPane() As Integer
         Return 1

     End Function

     Public Sub UserControlInModelView()
         Dim pDoc As IModelDoc2
         pDoc = DirectCast(iSwApp.ActiveDoc, IModelDoc2)
         Dim swModelViewMgr As IModelViewManager
         swModelViewMgr = pDoc.ModelViewManager
         ModelView1Control = New UserControl1()
         swModelViewMgr.DisplayWindowFromHandlex64(".NET User Control1", ModelView1Control.Handle.ToInt64(), False)
     End Sub

     Public Function EnableUserControlInModelView() As Integer
         If iSwApp.ActiveDoc IsNot Nothing Then
             Return 1
         Else
             Return 0
         End If
     End Function

     Public Sub WPFInModelView()
         Dim pDoc As IModelDoc2
         pDoc = DirectCast(iSwApp.ActiveDoc, IModelDoc2)
         Dim swModelViewMgr As IModelViewManager
         swModelViewMgr = pDoc.ModelViewManager
         WpfModelView1Control = New WPFControl()

         ModelViewelhost = New ElementHost()
         ModelViewelhost.Child = WpfModelView1Control
         swModelViewMgr.DisplayWindowFromHandlex64(".NET WPF Control", ModelViewelhost.Handle.ToInt64(), True)
     End Sub

     Public Function EnableWPFInModelView() As Integer
         If iSwApp.ActiveDoc IsNot Nothing Then
             Return 1
         Else
             Return 0
         End If
     End Function

     Public Sub WinFormInFeatureMgr()
         Dim pDoc As IModelDoc2
         pDoc = DirectCast(iSwApp.ActiveDoc, IModelDoc2)
         Dim swModelViewMgr As IModelViewManager
         swModelViewMgr = pDoc.ModelViewManager
         Dim swFeatMgrTabTop As IFeatMgrView
         FeatureMgrControl = New Form1()
         swFeatMgrTabTop = swModelViewMgr.CreateFeatureMgrWindowFromHandlex64("public_documents\samples\tutorial\api\addin\pm_extruded_block.bmp", FeatureMgrControl.Handle.ToInt64(), ".NET Windows Form Control", swFeatMgrPane_e.swFeatMgrPaneTop)
         pDoc.FeatureManagerSplitterPosition = 0.5
         swFeatMgrTabTop.ActivateView()
     End Sub

     Public Function EnableWinFormInFeatureMgr() As Integer
         If iSwApp.ActiveDoc IsNot Nothing Then
             Return 1
         Else
             Return 0
         End If
     End Function

     Public Sub ShowPMP()
         If ppage IsNot Nothing Then
             ppage.Show()
         End If
     End Sub

     Public Function EnablePMP() As Integer
         If iSwApp.ActiveDoc IsNot Nothing Then
             Return 1
         Else
             Return 0
         End If
     End Function
 #End Region

 #Region "Event Methods"
     Sub AttachEventHandlers()
         AttachSWEvents()

         'Listen for events on all currently open docs
         AttachEventsToAllDocuments()
     End Sub

     Sub DetachEventHandlers()
         DetachSWEvents()

         'Close events on all currently open docs
         Dim docHandler As DocumentEventHandler
         Dim key As ModelDoc2
         Dim numKeys As Integer
         numKeys = openDocs.Count
         If numKeys > 0 Then
             Dim keys() As Object = New Object(numKeys - 1) {}

             'Remove all document event handlers
             openDocs.Keys.CopyTo(keys, 0)
             For Each key In keys
                 docHandler = openDocs.Item(key)
                 docHandler.DetachEventHandlers() 'This also removes the pair from the hash
                 docHandler = Nothing
                 key = Nothing
             Next
         End If
     End Sub

     Sub AttachSWEvents()
         Try
             AddHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
             AddHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
             AddHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
             AddHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
             AddHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
         Catch e As Exception
             Console.WriteLine(e.Message)
         End Try
     End Sub

     Sub DetachSWEvents()
         Try
             RemoveHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
             RemoveHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
             RemoveHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
             RemoveHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
             RemoveHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
         Catch e As Exception
             Console.WriteLine(e.Message)
         End Try
     End Sub

     Sub AttachEventsToAllDocuments()
         Dim modDoc As ModelDoc2
         modDoc = iSwApp.GetFirstDocument()
         While Not modDoc Is Nothing
             If Not openDocs.Contains(modDoc) Then
                 AttachModelDocEventHandler(modDoc)
             Else
                 Dim docHandler As DocumentEventHandler = openDocs(modDoc)
                 If Not docHandler Is Nothing Then
                     docHandler.ConnectModelViews()
                 End If
             End If
             modDoc = modDoc.GetNext()
         End While
     End Sub

     Function AttachModelDocEventHandler(ByVal modDoc As ModelDoc2) As Boolean
         If modDoc Is Nothing Then
             Return False
         End If
         Dim docHandler As DocumentEventHandler = Nothing

         If Not openDocs.Contains(modDoc) Then
             Select Case modDoc.GetType
                 Case swDocumentTypes_e.swDocPART
                     docHandler = New PartEventHandler()
                 Case swDocumentTypes_e.swDocASSEMBLY
                     docHandler = New AssemblyEventHandler()
                 Case swDocumentTypes_e.swDocDRAWING
                     docHandler = New DrawingEventHandler()
             End Select

             docHandler.Init(iSwApp, Me, modDoc)
             docHandler.AttachEventHandlers()
             openDocs.Add(modDoc, docHandler)
         End If
     End Function

     Sub DetachModelEventHandler(ByVal modDoc As ModelDoc2)
         Dim docHandler As DocumentEventHandler
         docHandler = openDocs.Item(modDoc)
         openDocs.Remove(modDoc)
         modDoc = Nothing
         docHandler = Nothing
     End Sub
 #End Region

 #Region "Event Handlers"
     Function SldWorks_ActiveDocChangeNotify() As Integer
         'TODO: Add your implementation here
     End Function

     Function SldWorks_DocumentLoadNotify2(ByVal docTitle As String, ByVal docPath As String) As Integer

     End Function

     Function SldWorks_FileNewNotify2(ByVal newDoc As Object, ByVal doctype As Integer, ByVal templateName As String) As Integer
         AttachEventsToAllDocuments()
     End Function

     Function SldWorks_ActiveModelDocChangeNotify() As Integer
         'TODO: Add your implementation here
     End Function

     Function SldWorks_FileOpenPostNotify(ByVal FileName As String) As Integer
         AttachEventsToAllDocuments()
     End Function
 #End Region

 End Class
 Back to top

 'UserPMPage.vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swpublished
 Imports SolidWorks.Interop.swconst
 Imports System.Windows.Forms

 Imports System.Windows.Forms.Integration

 Public Class UserPMPage
     'Local Objects
     Dim swPropertyPage As IPropertyManagerPage2
     Dim handler As PMPHandler
     Dim iSwApp As ISldWorks
     Dim userAddin As SwAddin

     Dim MyWPFControl As WPFControl
     Dim elhost As ElementHost
     Dim MyUserControl As UserControl1
     Dim MyWinFormControl As Form1

 #Region "Property Manager Page Controls"
     'Groups
     Dim group1 As IPropertyManagerPageGroup
     Dim group2 As IPropertyManagerPageGroup
     Dim group3 As IPropertyManagerPageGroup

     'Controls
     Dim dotnet1 As IPropertyManagerPageWindowFromHandle
     Dim dotnet2 As IPropertyManagerPageWindowFromHandle
     Dim dotnet3 As IPropertyManagerPageWindowFromHandle

     'Control IDs
     Public Const group1ID As Integer = 0
     Public Const group2ID As Integer = 1
     Public Const group3ID As Integer = 2

     Public Const DotNet1ID As Integer = 3
     Public Const DotNet2ID As Integer = 4
     Public Const DotNet3ID As Integer = 5

 #End Region

     Public Sub New(addin As SwAddin)
         userAddin = addin
         iSwApp = DirectCast(userAddin.SwApp, ISldWorks)
         CreatePropertyManagerPage()
     End Sub

     Protected Sub CreatePropertyManagerPage()
         Dim errors As Integer = -1
         Dim options As Integer = swPropertyManagerPageOptions_e.swPropertyManagerOptions_OkayButton Or swPropertyManagerPageOptions_e.swPropertyManagerOptions_CancelButton

         handler = New PMPHandler(userAddin)
         swPropertyPage = DirectCast(iSwApp.CreatePropertyManagerPage(".Net PMP control", options, handler, errors), IPropertyManagerPage2)
         If swPropertyPage IsNot Nothing AndAlso errors = swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay Then
             Try
                 AddControls()
             Catch e As Exception
                 iSwApp.SendMsgToUser2(e.Message, 0, 0)
             End Try
         End If
     End Sub

     'Controls display on the page top to bottom in the order
     'in which they are added to the page
     Protected Sub AddControls()
         Dim controlType As Short = -1
         Dim align As Short = -1
         Dim options As Integer = -1

         'Add the groups
         options = swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded Or swAddGroupBoxOptions_e.swGroupBoxOptions_Visible

         group1 = DirectCast(swPropertyPage.AddGroupBox(group1ID, "Windows Form controls", options), IPropertyManagerPageGroup)

         options = swAddGroupBoxOptions_e.swGroupBoxOptions_Checkbox Or swAddGroupBoxOptions_e.swGroupBoxOptions_Visible

         group2 = DirectCast(swPropertyPage.AddGroupBox(group2ID, "User controls", options), IPropertyManagerPageGroup)

         options = swAddGroupBoxOptions_e.swGroupBoxOptions_Checkbox Or swAddGroupBoxOptions_e.swGroupBoxOptions_Visible

         group3 = DirectCast(swPropertyPage.AddGroupBox(group3ID, "WPF controls", options), IPropertyManagerPageGroup)

         controlType = swPropertyManagerPageControlType_e.swControlType_WindowFromHandle
         align = swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge
         options = swAddControlOptions_e.swControlOptions_Enabled Or swAddControlOptions_e.swControlOptions_Visible

         dotnet1 = DirectCast(group1.AddControl2(DotNet1ID, controlType, ".Net Windows Form control", align, options, "This control is added without COM"), IPropertyManagerPageWindowFromHandle)
         dotnet1.Height = 150

         controlType = swPropertyManagerPageControlType_e.swControlType_WindowFromHandle
         align = swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge
         options = swAddControlOptions_e.swControlOptions_Enabled Or swAddControlOptions_e.swControlOptions_Visible

         dotnet2 = DirectCast(group2.AddControl2(DotNet2ID, controlType, ".Net user form control", align, options, "This control is added without COM"), IPropertyManagerPageWindowFromHandle)
         dotnet2.Height = 150

         dotnet3 = DirectCast(group3.AddControl2(DotNet3ID, controlType, ".Net WPF control", align, options, "This control is added without COM"), IPropertyManagerPageWindowFromHandle)
         dotnet3.Height = 50

     End Sub

     Public Sub Show()

         'Windows Form control
         MyWinFormControl = New Form1()
         'If you are adding Windows form in the PropertyManager Page, set TopLevel to false
         MyWinFormControl.TopLevel = False
         MyWinFormControl.Show()
         dotnet1.SetWindowHandlex64(MyWinFormControl.Handle.ToInt64())

         'User control
         MyUserControl = New UserControl1()
         dotnet2.SetWindowHandlex64(MyUserControl.Handle.ToInt64())

         'WPF control
         elhost = New ElementHost()
         MyWPFControl = New WPFControl()
         elhost.Child = MyWPFControl
         dotnet3.SetWindowHandlex64(elhost.Handle.ToInt64())

         'Show PropertyManager page
         swPropertyPage.Show()

     End Sub
 End Class

Back to top
 'PMPHandler.vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports System.Windows.Forms

 Public Class PMPHandler
     Implements PropertyManagerPage2Handler9

     Dim iSwApp As SldWorks
     Dim userAddin As SwAddin

     Public Sub New(addin As SwAddin)
         userAddin = addin
         iSwApp = DirectCast(userAddin.SwApp, ISldWorks)
     End Sub

     'Implement these methods from the interface
     Sub AfterClose() Implements PropertyManagerPage2Handler9.AfterClose
         ''This function must contain code, even if it does nothing, to prevent the
         ''.NET runtime environment from doing garbage collection at the wrong time.
         Dim IndentSize As Integer
         IndentSize = System.Diagnostics.Debug.IndentSize
         System.Diagnostics.Debug.WriteLine(IndentSize)

     End Sub

     Sub OnCheckboxCheck(ByVal id As Integer, ByVal status As Boolean) Implements PropertyManagerPage2Handler9.OnCheckboxCheck

     End Sub

     Sub OnClose(ByVal reason As Integer) Implements PropertyManagerPage2Handler9.OnClose
         ''This function must contain code, even if it does nothing, to prevent the
         ''.NET runtime environment from doing garbage collection at the wrong time.
         Dim IndentSize As Integer
         IndentSize = System.Diagnostics.Debug.IndentSize
         System.Diagnostics.Debug.WriteLine(IndentSize)
     End Sub

     Sub OnComboboxEditChanged(ByVal id As Integer, ByVal text As String) Implements PropertyManagerPage2Handler9.OnComboboxEditChanged

     End Sub

     Function OnActiveXControlCreated(ByVal id As Integer, ByVal status As Boolean) As Integer Implements PropertyManagerPage2Handler9.OnActiveXControlCreated
         OnActiveXControlCreated = -1
     End Function

     Sub OnButtonPress(ByVal id As Integer) Implements PropertyManagerPage2Handler9.OnButtonPress

     End Sub

     Sub OnComboboxSelectionChanged(ByVal id As Integer, ByVal item As Integer) Implements PropertyManagerPage2Handler9.OnComboboxSelectionChanged

     End Sub

     Sub OnGroupCheck(ByVal id As Integer, ByVal status As Boolean) Implements PropertyManagerPage2Handler9.OnGroupCheck

     End Sub

     Sub OnGroupExpand(ByVal id As Integer, ByVal status As Boolean) Implements PropertyManagerPage2Handler9.OnGroupExpand

     End Sub

     Function OnHelp() As Boolean Implements PropertyManagerPage2Handler9.OnHelp
         OnHelp = True
     End Function

     Sub OnListboxSelectionChanged(ByVal id As Integer, ByVal item As Integer) Implements PropertyManagerPage2Handler9.OnListboxSelectionChanged

     End Sub

     Function OnNextPage() As Boolean Implements PropertyManagerPage2Handler9.OnNextPage
         OnNextPage = True
     End Function

     Sub OnNumberboxChanged(ByVal id As Integer, ByVal val As Double) Implements PropertyManagerPage2Handler9.OnNumberboxChanged

     End Sub

     Sub OnOptionCheck(ByVal id As Integer) Implements PropertyManagerPage2Handler9.OnOptionCheck

     End Sub

     Function OnPreviousPage() As Boolean Implements PropertyManagerPage2Handler9.OnPreviousPage
         OnPreviousPage = True
     End Function

     Sub OnSelectionboxCalloutCreated(ByVal id As Integer) Implements PropertyManagerPage2Handler9.OnSelectionboxCalloutCreated

     End Sub

     Sub OnSelectionboxCalloutDestroyed(ByVal id As Integer) Implements PropertyManagerPage2Handler9.OnSelectionboxCalloutDestroyed

     End Sub

     Sub OnSelectionboxFocusChanged(ByVal Id As Integer) Implements PropertyManagerPage2Handler9.OnSelectionboxFocusChanged

     End Sub

     Sub OnSelectionboxListChanged(ByVal id As Integer, ByVal item As Integer) Implements PropertyManagerPage2Handler9.OnSelectionboxListChanged

     End Sub

     Sub OnTextboxChanged(ByVal id As Integer, ByVal text As String) Implements PropertyManagerPage2Handler9.OnTextboxChanged

     End Sub

     Public Sub AfterActivation() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.AfterActivation

     End Sub

     Public Function OnKeystroke(ByVal Wparam As Integer, ByVal Message As Integer, ByVal Lparam As Integer, ByVal Id As Integer) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnKeystroke
         OnKeystroke = True
     End Function

     Public Sub OnPopupMenuItem(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPopupMenuItem

     End Sub

     Public Sub OnPopupMenuItemUpdate(ByVal Id As Integer, ByRef retval As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPopupMenuItemUpdate

     End Sub

     Public Function OnPreview() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPreview
         OnPreview = True
     End Function

     Public Sub OnSliderPositionChanged(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderPositionChanged

     End Sub

     Public Sub OnSliderTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderTrackingCompleted

     End Sub

     Public Function OnSubmitSelection(ByVal Id As Integer, ByVal Selection As Object, ByVal SelType As Integer, ByRef ItemText As String) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSubmitSelection
         OnSubmitSelection = True
     End Function

     Public Function OnTabClicked(ByVal Id As Integer) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnTabClicked
         OnTabClicked = True
     End Function

     Public Sub OnUndo() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnUndo

     End Sub

     Public Sub OnWhatsNew() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnWhatsNew

     End Sub

     Function OnWindowFromHandleControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnWindowFromHandleControlCreated
         System.Windows.Forms.MessageBox.Show(".NET control created")
         Return -1
     End Function

     Sub OnGainedFocus(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGainedFocus

     End Sub

     Sub OnListboxRMBUp(ByVal Id As Integer, ByVal PosX As Integer, ByVal PosY As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnListboxRMBUp

     End Sub

     Sub OnLostFocus(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnLostFocus

     End Sub

     Sub OnRedo() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnRedo

     End Sub

     Sub OnNumberBoxTrackingCompleted(ByVal id As Integer, ByVal val As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNumberBoxTrackingCompleted

     End Sub
 End Class

Back to top
'WPFControl.xaml
 <UserControl x:Class="WPFControl"
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

Back to top
 'WPFControl.xaml.vb
 Imports System.Collections.Generic
 Imports System.Text
 Imports System.Windows
 Imports System.Windows.Controls
 Imports System.Windows.Data
 Imports System.Windows.Documents
 Imports System.Windows.Input
 Imports System.Windows.Media
 Imports System.Windows.Media.Imaging
 Imports System.Windows.Navigation
 Imports System.Windows.Shapes

 Public Class WPFControl
     Inherits UserControl
     Sub New()
         InitializeComponent()
     End Sub

     Sub UserControl_Loaded(sender As Object, e As RoutedEventArgs)

     End Sub
 End Class

Back to top
 'UserControl1.vb
 Imports System.Drawing
 Imports System.Data
 Imports System.Linq
 Imports System.Text
 Imports System.Windows.Forms

 Partial Public Class UserControl1
     Inherits UserControl

     Public Sub New()
         InitializeComponent()
     End Sub

     Private Sub textBox1_TextChanged_1(sender As Object, e As EventArgs) Handles textBox1.TextChanged

     End Sub

     Private Sub TabPage1_Click_1(sender As Object, e As EventArgs) Handles TabPage1.Click

     End Sub

     Private Sub TabPage2_Click_1(sender As Object, e As EventArgs) Handles TabPage2.Click

     End Sub

     Private Sub TabPage3_Click_1(sender As Object, e As EventArgs) Handles TabPage3.Click

     End Sub

     Private Sub radioButton1_CheckedChanged_1(sender As Object, e As EventArgs) Handles radioButton1.CheckedChanged

     End Sub

     Private Sub button1_Click_1(sender As Object, e As EventArgs) Handles button1.Click
           System.Windows.Forms.MessageBox.Show("Hello.")
     End Sub

 End Class

Back to top
 'UserControl1.Designer.vb
 Partial Class UserControl1
     ''' <summary>
     ''' Required designer variable.
     ''' </summary>
     Private components As System.ComponentModel.IContainer = Nothing

     ''' <summary>
     ''' Clean up any resources being used.
     ''' </summary>
     ''' <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
     Protected Overrides Sub Dispose(disposing As Boolean)
         If disposing AndAlso (components IsNot Nothing) Then
             components.Dispose()
         End If
         MyBase.Dispose(disposing)
     End Sub

 #Region "Component Designer generated code"

     ''' <summary>
     ''' Required method for Designer support - do not modify
     ''' the contents of this method with the code editor.
     ''' </summary>
     Private Sub InitializeComponent()
         Me.radioButton1 = New System.Windows.Forms.RadioButton()
         Me.textBox1 = New System.Windows.Forms.TextBox()
         Me.button1 = New System.Windows.Forms.Button()
         Me.tabControl1 = New System.Windows.Forms.TabControl()
         Me.TabPage1 = New System.Windows.Forms.TabPage()
         Me.TabPage2 = New System.Windows.Forms.TabPage()
         Me.TabPage3 = New System.Windows.Forms.TabPage()
         Me.tabControl1.SuspendLayout()
         Me.SuspendLayout()
         '
         ' radioButton1
         '
         Me.radioButton1.Anchor = System.Windows.Forms.AnchorStyles.Left
         Me.radioButton1.AutoSize = True
         Me.radioButton1.Location = New System.Drawing.Point(23, 113)
         Me.radioButton1.Name = "radioButton1"
         Me.radioButton1.Size = New System.Drawing.Size(85, 17)
         Me.radioButton1.TabIndex = 5
         Me.radioButton1.TabStop = True
         Me.radioButton1.Text = "radioButton1"
         Me.radioButton1.UseVisualStyleBackColor = True

         '
         ' textBox1
         '
         Me.textBox1.Anchor = (System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Left) Or System.Windows.Forms.AnchorStyles.Right
         Me.textBox1.Location = New System.Drawing.Point(23, 87)
         Me.textBox1.Name = "textBox1"
         Me.textBox1.Size = New System.Drawing.Size(378, 20)
         Me.textBox1.TabIndex = 4

         '
         ' button1
         '
         Me.button1.Location = New System.Drawing.Point(23, 17)
         Me.button1.Name = "button1"
         Me.button1.Size = New System.Drawing.Size(119, 49)
         Me.button1.TabIndex = 3
         Me.button1.Text = "Say Hello"
         Me.button1.UseVisualStyleBackColor = True

         '
         ' tabControl1
         '
         Me.tabControl1.Anchor = (System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Left) Or System.Windows.Forms.AnchorStyles.Right
         Me.tabControl1.Controls.Add(Me.TabPage1)
         Me.tabControl1.Controls.Add(Me.TabPage2)
         Me.tabControl1.Controls.Add(Me.TabPage3)
         Me.tabControl1.Location = New System.Drawing.Point(23, 148)
         Me.tabControl1.Multiline = True
         Me.tabControl1.Name = "tabControl1"
         Me.tabControl1.SelectedIndex = 0
         Me.tabControl1.Size = New System.Drawing.Size(386, 69)
         Me.tabControl1.TabIndex = 6
         '
         ' TabPage1
         '
         Me.TabPage1.Location = New System.Drawing.Point(4, 22)
         Me.TabPage1.Name = "TabPage1"
         Me.TabPage1.Padding = New System.Windows.Forms.Padding(3)
         Me.TabPage1.Size = New System.Drawing.Size(378, 43)
         Me.TabPage1.TabIndex = 0
         Me.TabPage1.Text = "TabPage1"
         Me.TabPage1.UseVisualStyleBackColor = True

         '
         ' TabPage2
         '
         Me.TabPage2.Location = New System.Drawing.Point(4, 22)
         Me.TabPage2.Name = "TabPage2"
         Me.TabPage2.Padding = New System.Windows.Forms.Padding(3)
         Me.TabPage2.Size = New System.Drawing.Size(378, 43)
         Me.TabPage2.TabIndex = 1
         Me.TabPage2.Text = "TabPage2"
         Me.TabPage2.UseVisualStyleBackColor = True

         '
         ' TabPage3
         '
         Me.TabPage3.Location = New System.Drawing.Point(4, 22)
         Me.TabPage3.Name = "TabPage3"
         Me.TabPage3.Padding = New System.Windows.Forms.Padding(3)
         Me.TabPage3.Size = New System.Drawing.Size(378, 43)
         Me.TabPage3.TabIndex = 2
         Me.TabPage3.Text = "TabPage3"
         Me.TabPage3.UseVisualStyleBackColor = True

         '
         ' UserControl1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0F, 13.0F)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.Controls.Add(Me.tabControl1)
         Me.Controls.Add(Me.radioButton1)
         Me.Controls.Add(Me.textBox1)
         Me.Controls.Add(Me.button1)
         Me.Name = "UserControl1"
         Me.Size = New System.Drawing.Size(427, 237)
         Me.tabControl1.ResumeLayout(False)
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Private WithEvents radioButton1 As System.Windows.Forms.RadioButton
     Private  WithEvents textBox1 As System.Windows.Forms.TextBox
     Private  WithEvents button1 As System.Windows.Forms.Button
     Private  WithEvents tabControl1 As System.Windows.Forms.TabControl
     Private  WithEvents TabPage1 As System.Windows.Forms.TabPage
     Private  WithEvents TabPage2 As System.Windows.Forms.TabPage
     Private WithEvents TabPage3 As System.Windows.Forms.TabPage
 End Class

Back to top
'Form1.vb
 Imports System.Collections.Generic
 Imports System.ComponentModel
 Imports System.Data
 Imports System.Drawing
 Imports System.Linq
 Imports System.Text
 Imports System.Windows.Forms

 Partial Public Class Form1
     Inherits Form

     Public Sub New()
         InitializeComponent()
     End Sub

     Private Sub button1_Click_1(sender As Object, e As EventArgs) Handles button1.Click
        System.Windows.Forms.MessageBox.Show("Hello.")

     End Sub

     Private Sub textBox1_TextChanged_1(sender As Object, e As EventArgs) Handles textBox1.TextChanged

     End Sub

     Private Sub comboBox1_SelectedIndexChanged_1(sender As Object, e As EventArgs) Handles comboBox1.SelectedIndexChanged

     End Sub

     Private Sub listBox1_SelectedIndexChanged_1(sender As Object, e As EventArgs) Handles listBox1.SelectedIndexChanged

     End Sub

 End Class

Back to top
 'Form1.Designer.vb
 Partial Class Form1
     ''' <summary>
     ''' Required designer variable.
     ''' </summary>
     Private components As System.ComponentModel.IContainer = Nothing

     ''' <summary>
     ''' Clean up any resources being used.
     ''' </summary>
     ''' <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
     Protected Overrides Sub Dispose(disposing As Boolean)
         If disposing AndAlso (components IsNot Nothing) Then
             components.Dispose()
         End If
         MyBase.Dispose(disposing)
     End Sub

 #Region "Windows Form Designer generated code"

     ''' <summary>
     ''' Required method for Designer support - do not modify
     ''' the contents of this method with the code editor.
     ''' </summary>
     Private Sub InitializeComponent()
         Me.listBox1 = New System.Windows.Forms.ListBox()
         Me.comboBox1 = New System.Windows.Forms.ComboBox()
         Me.textBox1 = New System.Windows.Forms.TextBox()
         Me.button1 = New System.Windows.Forms.Button()
         Me.SuspendLayout()
         '
         ' listBox1
         '
         Me.listBox1.Anchor = (System.Windows.Forms.AnchorStyles.Bottom Or System.Windows.Forms.AnchorStyles.Left) Or System.Windows.Forms.AnchorStyles.Right
         Me.listBox1.FormattingEnabled = True
         Me.listBox1.Items.AddRange(New Object() {"Help", "Whats New"})
         Me.listBox1.Location = New System.Drawing.Point(25, 160)
         Me.listBox1.Name = "listBox1"
         Me.listBox1.Size = New System.Drawing.Size(304, 43)
         Me.listBox1.TabIndex = 10

         '
         ' comboBox1
         '
         Me.comboBox1.DisplayMember = "Monday"
         Me.comboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
         Me.comboBox1.FormattingEnabled = True
         Me.comboBox1.Items.AddRange(New Object() {"Monday ", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", _
             "Sunday"})
         Me.comboBox1.Location = New System.Drawing.Point(25, 122)
         Me.comboBox1.Name = "comboBox1"
         Me.comboBox1.Size = New System.Drawing.Size(140, 21)
         Me.comboBox1.TabIndex = 9
         Me.comboBox1.ValueMember = "Monday"

         '
         ' textBox1
         '
         Me.textBox1.Anchor = ((System.Windows.Forms.AnchorStyles.Top Or System.Windows.Forms.AnchorStyles.Bottom) Or System.Windows.Forms.AnchorStyles.Left) Or System.Windows.Forms.AnchorStyles.Right
         Me.textBox1.Location = New System.Drawing.Point(25, 86)
         Me.textBox1.Name = "textBox1"
         Me.textBox1.Size = New System.Drawing.Size(321, 20)
         Me.textBox1.TabIndex = 8

         '
         ' button1
         '
         Me.button1.Location = New System.Drawing.Point(25, 12)
         Me.button1.Name = "button1"
         Me.button1.Size = New System.Drawing.Size(140, 57)
         Me.button1.TabIndex = 7
         Me.button1.Text = "Say Hello"
         Me.button1.UseVisualStyleBackColor = True

         '
         ' Form1
         '
         Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0F, 13.0F)
         Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
         Me.ClientSize = New System.Drawing.Size(382, 215)
         Me.ControlBox = False
         Me.Controls.Add(Me.listBox1)
         Me.Controls.Add(Me.comboBox1)
         Me.Controls.Add(Me.textBox1)
         Me.Controls.Add(Me.button1)
         Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None
         Me.MaximizeBox = False
         Me.MinimizeBox = False
         Me.Name = "Form1"
         Me.ShowIcon = False
         Me.ShowInTaskbar = False
         Me.Text = "Form1"
         Me.ResumeLayout(False)
         Me.PerformLayout()

     End Sub

 #End Region

     Private WithEvents listBox1 As System.Windows.Forms.ListBox
     Private WithEvents comboBox1 As System.Windows.Forms.ComboBox
     Private WithEvents textBox1 As System.Windows.Forms.TextBox
     Private WithEvents button1 As System.Windows.Forms.Button
 End Class

Back to top
```

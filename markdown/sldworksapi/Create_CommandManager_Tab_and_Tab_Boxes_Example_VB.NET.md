---
title: "Create CommandManager Tab and Tab Boxes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm"
---

# Create CommandManager Tab and Tab Boxes Example (VB.NET)

This example shows how to create an add-in that creates a CommandManager tab and tab boxes.

NOTES:

- This sample code is part of a project that was built using the VB.NET Add-In Wizard.
- To run this sample code, you need to create a complete VB.NET project.
- Your add-in must check to see if the tab already exists. If the tab already exists, then you should use that tab instead of creating a new tab. If your add-in does not check for an existing tab, then SOLIDWORKS Design will create a new tab each time it starts up.
- Users can add buttons to and remove buttons from your CommandManager tab. However, if your add-in removes the CommandManager tab upon exiting SOLIDWORKS Design, then any user customizations will be lost.

'------------------------------------------------------------------------------------------------------------------------------

#### ' SwAddin.vb

```vb
Imports System
Imports System.Windows.Forms
Imports System.Collections
Imports System.Reflection
Imports System.Runtime.InteropServices
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swpublished
Imports SolidWorksTools
Imports SolidWorksTools.File
<Guid("c5ede50f-7484-416b-9425-ca49f565e48e")> _
    <ComVisible(True)> _
    <SwAddin( _
        Description:="test description", _
        Title:="test", _
        LoadAtStartup:=True _
        )> _
        Public Class SwAddin
    Implements SolidWorks.Interop.swpublished.SwAddin
#Region "Local Variables"
    Dim WithEvents iSwApp As SldWorks
    Dim iCmdMgr As ICommandManager
    Dim addinID As Integer
    Dim openDocs As Hashtable
    Dim SwEventPtr As SldWorks
    Dim ppage As UserPMPage
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
#Region "SOLIDWORKS Registration"
    <ComRegisterFunction()> Public Shared Sub RegisterFunction(ByVal t As Type)
        ' Get Custom Attribute: SwAddinAttribute
        Dim attributes() As Object
        Dim SWattr As SwAddinAttribute = Nothing
        attributes = System.Attribute.GetCustomAttributes(GetType(SwAddin), GetType(SwAddinAttribute))
        If attributes.Length > 0 Then
            SWattr = DirectCast(attributes(0), SwAddinAttribute)
        End If
        Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
        Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser
        Dim keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString() + "}"
        Dim addinkey As Microsoft.Win32.RegistryKey = hklm.CreateSubKey(keyname)
        addinkey.SetValue(Nothing, 0)
        addinkey.SetValue("Description", SWattr.Description)
        addinkey.SetValue("Title", SWattr.Title)
        keyname = "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString() + "}"
        addinkey = hkcu.CreateSubKey(keyname)
        addinkey.SetValue(Nothing, SWattr.LoadAtStartup,Microsoft.Win32.RegistryValueKind.DWord)
    End Sub
    <ComUnregisterFunction()> Public Shared Sub UnregisterFunction(ByVal t As Type)
        Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
        Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser
        Dim keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString() + "}"
        hklm.DeleteSubKey(keyname)
        keyname = "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString() + "}"
        hkcu.DeleteSubKey(keyname)
    End Sub
#End Region
#Region "ISwAddin Implementation"
    Function ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Integer) As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.ConnectToSW
        iSwApp = ThisSW
        addinID = Cookie
        ' Setup callbacks
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
        iSwApp = Nothing
        'The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
        GC.Collect()
        DisconnectFromSW = True
    End Function
#End Region
#Region "UI Methods"
    Public Sub AddCommandMgr()
        Dim cmdGroup As ICommandGroup
        Dim iBmp As New BitmapHandler
        Dim thisAssembly As Assembly
        Dim cmdIndex0 As Integer, cmdIndex1 As Integer
        Dim Title As String = "VB Addin"
        Dim ToolTip As String = "VB Addin"
        Dim docTypes() As Integer = {swDocumentTypes_e.swDocASSEMBLY, _
                                       swDocumentTypes_e.swDocDRAWING, _
                                       swDocumentTypes_e.swDocPART}
        thisAssembly = System.Reflection.Assembly.GetAssembly(Me.GetType())
        cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip, "", -1)
        cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("test.ToolbarLarge.bmp", thisAssembly)
        cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("test.ToolbarSmall.bmp", thisAssembly)
        cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("test.MainIconLarge.bmp", thisAssembly)
        cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("test.MainIconSmall.bmp", thisAssembly)
        cmdIndex0 = cmdGroup.AddCommandItem2("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0, 1)
        cmdIndex1 = cmdGroup.AddCommandItem2("Show PMP", -1, "Display sample property manager", "Show PMP", 2, "ShowPMP", "PMPEnable", 2, 1)
        cmdGroup.HasToolbar = True
        cmdGroup.HasMenu = True
        cmdGroup.Activate()
        For Each docType As Integer In docTypes
            Dim cmdTab As ICommandTab = iCmdMgr.GetCommandTab(docType, Title)
            Dim bResult As Boolean
            If cmdTab Is Nothing Then
                cmdTab = iCmdMgr.AddCommandTab(docType, Title)
                Dim cmdBox As CommandTabBox = cmdTab.AddCommandTabBox
                Dim cmdIDs(3) As Integer
                Dim TextType(3) As Integer
                cmdIDs(0) = cmdGroup.CommandID(cmdIndex0)
                TextType(0) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal
                cmdIDs(1) = cmdGroup.CommandID(cmdIndex1)
                TextType(1) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal
                cmdIDs(2) = cmdGroup.ToolbarId
                TextType(2) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal
                bResult = cmdBox.AddCommands(cmdIDs, TextType)
                ' Call GetCommands to confirm
                Dim buttonNumber As Integer
                Dim idObject As Object = Nothing
                Dim textTypeObject As Object = Nothing
                buttonNumber = cmdBox.GetCommands(idObject, textTypeObject)
                Debug.Print("Added " + buttonNumber.ToString() + " commands.")
                Dim cmdBox1 As CommandTabBox = cmdTab.AddCommandTabBox()
                ReDim cmdIDs(1)
                ReDim TextType(1)
                cmdIDs(0) = cmdGroup.ToolbarId
                TextType(0) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow
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
    Function AddPMP() As Boolean
        ppage = New UserPMPage
        ppage.Init(iSwApp, Me)
    End Function
    Function RemovePMP() As Boolean
        ppage = Nothing
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
        AddHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
        AddHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
        AddHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
        AddHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
        AddHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
    End Sub
    Sub DetachSWEvents()
        RemoveHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
        RemoveHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
        RemoveHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
        RemoveHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
        RemoveHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
    End Sub
    Sub AttachEventsToAllDocuments()
        Dim modDoc As ModelDoc2
        modDoc = iSwApp.GetFirstDocument()
        While Not modDoc Is Nothing
            If Not openDocs.Contains(modDoc) Then
                AttachModelDocEventHandler(modDoc)
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
        Dim modDoc As ModelDoc2
        modDoc = iSwApp.GetFirstDocument()
        While Not modDoc Is Nothing
            If modDoc.GetTitle = docTitle Then
                If Not openDocs.Contains(modDoc) Then
                    AttachModelDocEventHandler(modDoc)
                End If
            End If
            modDoc = modDoc.GetNext()
        End While
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
#Region "UI Callbacks"
    Sub CreateCube()
        'make sure we have a part open
        Dim partTemplate As String
        Dim model As ModelDoc2
        Dim featMan As FeatureManager
        partTemplate = iSwApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
        model = iSwApp.NewDocument(partTemplate, swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0)
        model.InsertSketch2(True)
        model.SketchRectangle(0, 0, 0, 0.1, 0.1, 0.1, False)
        'Extrude the sketch
        featMan = model.FeatureManager
        featMan.FeatureExtrusion(True, _
                                  False, False, _
                                  swEndConditions_e.swEndCondBlind, swEndConditions_e.swEndCondBlind, _
                                  0.1, 0.0, _
                                  False, False, _
                                  False, False, _
                                  0.0, 0.0, _
                                  False, False, _
                                  False, False, _
                                  True, _
                                  False, False)
    End Sub
    Sub ShowPMP()
        ppage.Show()
    End Sub
    Function PMPEnable() As Integer
        If iSwApp.ActiveDoc Is Nothing Then
            PMPEnable = 0
        Else
            PMPEnable = 1
        End If
    End Function
#End Region
End Class
```

---
title: "Creating Add-ins (VB.NET)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/DotNetAddIns.htm"
---

# Creating Add-ins (VB.NET)

This topic shows how to create a debug add-in using VB.NET in Microsoft Visual Studio.

**NOTE:** Because SOLIDWORKS PDM Professional cannot force a reload of add-ins if they are written in VB.NET, all client machines must be restarted to ensure that the latest version of the add-in is used.

1. Start Microsoft Visual Studio.
2. Click **File > New > Project.**
3. In the dropdowns, select **Visual Basic, Windows, and Library.**
4. Select **Class Library** **(.NET Framework)**.
5. Enter **Project name**, **Solution** (Create new solution or Add to solution), and **Solution name** (if Create new Solution).
6. For Location, click **...** and navigate to the folder where to create your project.
7. Click **Create**.

  **Class1.vb** containing an empty class called Class1 is created.
8. Right-click the name of your project in the Solution Explorer to add the SOLIDWORKS PDM Professional type library and the Systems.Windows.Forms assembly:

  1. Select **Add Reference...**.
  2. Click **Browse...** in the left-hand panel, navigate to and select **EPDM.Interop.epdm.dll**, and click **OK**.
  3. Select **Add Reference...**.
  4. Click **Assemblies > Framework** in the left-hand panel, select **System.Windows.Forms**, and click **OK**.
  5. Click **Close**.
9. At the top of the **Class1.vb** code window, type on separate lines **Imports System.Windows.Forms,** Imports EPDM.Interop.epdm, and **Imports System.Runtime.InteropServices**.
10. Type before **Public Class Class1**:
  <Guid("")> _
  <ComVisible(True)> _
11. To populate the GUID attribute above, click **Tools > Create GUID** in the IDE, select GUID Format 6, click **Copy**, and click **Exit**. Replace <Guid("")> with the copied string.
12. Type below **Public Class Class1**:

  Implements IEdmAddIn5
13. Implement [IEdmAddIn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddin5~GetAddInInfo.html)[5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddin5~GetAddInInfo.html) by pasting the following code between **Implements IEdmAddIn5** and **End Class**:

Public Sub GetAddInInfo(ByRef poInfo As EdmAddInInfo, ByVal poVault As IEdmVault5, ByVal poCmdMgr As IEdmCmdMgr5) Implements IEdmAddIn5.GetAddInInfo

' Specify add-in information

poInfo.mbsAddInName = "VB.NET Add-in"

poInfo.mbsCompany = "My Company"

poInfo.mbsDescription = "Menu add-in that shows a message box."

poInfo.mlAddInVersion = 1

' Specify minimum version of SOLIDWORKS PDM Professional

poInfo.mlRequiredVersionMajor = 6

poInfo.mlRequiredVersionMinor = 4

' Register a menu command

poCmdMgr.AddCmd(1, "VB.NET Add-in", EdmMenuFlags.EdmMenu_Nothing)

End Sub

1. Implement [IEdmAddIn5::](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)[OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) by pasting the following code between **End Sub** and **End Class**:

  **NOTE**: [IEdmVault8::GetWin32Window](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault8~GetWin32Window.html) is used to convert the parent window handle to a window handle that .NET can use.

Public Sub OnCmd(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData()) Implements IEdmAddIn5.OnCmd

' Handle the menu command

If poCmd.meCmdType = EdmCmdType.EdmCmd_Menu Then

If poCmd.mlCmdID = 1 Then

Dim v8 as IEdmVault8

V8 = poCmd.mpoVault

System.Windows.Forms.MessageBox.Show(v8.GetWin32Window(poCmd.mlParentWnd), "VB.NET Add-in")

End If

End If

End Sub

1. Implement your own window handle wrapper by right-clicking the name of your project in the Solution Explorer and selecting **Add > New Item > Class**:

  1. Type **WindowHandle** in **Name**.
  2. Click **Add**.
  3. Replace the code in the code window with the following code.

Imports System.Windows.Forms

' Wrapper class to use SOLIDWORKS PDM Professional as a parent window to VB forms

Public Class WindowHandle

Implements IWin32Window

Private mHwnd As IntPtr

Public Sub New(ByVal hWnd As Integer)

mHwnd = New IntPtr(hWnd)

End Sub

Public ReadOnly Property Handle() As IntPtr Implements System.Windows.Forms.IWin32Window.Handle

Get

Return mHwnd

End Get

End Property

End Class

Your add-in uses the new wrapper in the menu command handler to show the message box by calling System.Windows.Forms.MessageBox.Show in Class1::OnCmd in Class1.vb.

1. Right-click the name of your project in the Solution Explorer and select **Properties**.

  1. On the **Application** tab, keep the suggested target framework or select **.NET Framework** **4.7.2** in the Target framework dropdown.
  2. On the **Application** tab, click **Assembly Information** and de-select **Make assembly COM-Visible**.
  3. On the **Compile** tab, select **AnyCPU** for the target CPU, de-select **Prefer 32-bit** and select **Register for COM interop**.
  4. On the **Debug** tab, select **Start external program** and type **C:\Windows\System32\notepad.exe** in the text field.
  5. Save the properties.

1. Right-click **E****pdm.Interop.epdm** in the Solution Explorer, select **Properties**, and set **Embed Interop Types** to **False** to handle methods that pass arrays of structures.
2. In Notepad, edit `project_path``\``project_name\``project_name\``project_name`.**vbproj**:

  1. Insert the following line below **<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">** and below **<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">**.

    <PlatformTarget>AnyCPU</PlatformTarget>
  2. Save the file and exit Notepad.
3. On the Visual Studio menu, click **Build > Build Solution** to build the add-in.
4. Install the add-in as a Debug Add-in using the SOLIDWORKS PDM Professional Administration tool:

  1. Start up the SOLIDWORKS PDM Professional Administration tool.
  2. Expand the vault where you want to install this add-in. Log in if prompted.
  3. Right-click **Add-ins** and select **Debug Add-ins**.
  4. Click **Add Add-in**, browse to `project_path``\``project_name\project_name`**\bin\Debug**, select `project_name`**.dll**, and click **Open**.

    Your add-in's name, path, and class ID should appear in **Add-ins installed for debugging on this machine**.
  5. Click **OK**.
5. In Microsoft Visual Studio, click **Debug > Start Debugging** or press **F5**.
6. Click **File > Open** in Notepad.
7. Click the name of the vault where you installed your add-in.
8. Right-click inside the vault in File Explorer and select **VB.NET Add-in**.

  A message box is displayed with the message **VB.NET Add-in**.
9. Click **OK** to close the message box.

### Complete Source Code

##### ' Class1.vb

```
Imports System.Windows.Forms
Imports System.Runtime.InteropServices
Imports EPDM.Interop.epdm
```

```
<Guid("")> _   ' See step 10 above to create the GUID
<ComVisible(True)> _
Public Class Class1
    Implements IEdmAddIn5

    Public Sub GetAddInInfo(ByRef poInfo As EdmAddInInfo, ByVal poVault As IEdmVault5, ByVal poCmdMgr As IEdmCmdMgr5) Implements IEdmAddIn5.GetAddInInfo
        ' Fill in the add-in's description
        poInfo.mbsAddInName = "VB.NET Add-in"
        poInfo.mbsCompany = "My Company"
        poInfo.mbsDescription = "Menu add-in that shows a message box."
        poInfo.mlAddInVersion = 1

        ' Minimum SOLIDWORKS PDM Professional version needed for VB.NET add-ins is 6.4
        poInfo.mlRequiredVersionMajor = 6
        poInfo.mlRequiredVersionMinor = 4

        ' Register a menu command
        poCmdMgr.AddCmd(1, "VB.NET Add-in", EdmMenuFlags.EdmMenu_Nothing)

    End Sub

    Public Sub OnCmd(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData()) Implements IEdmAddIn5.OnCmd

        ' Handle the menu command
        If poCmd.meCmdType = EdmCmdType.EdmCmd_Menu Then
            If poCmd.mlCmdID = 1 Then
                Dim v8 As IEdmVault8
                v8 = poCmd.mpoVault
                System.Windows.Forms.MessageBox.Show(v8.GetWin32Window(poCmd.mlParentWnd), "VB.NET Add-in")
            End If
        End If

    End Sub

End Class
```

##### 'WindowHandle.vb

```
Imports System.Windows.Forms

Public Class WindowHandle
    Implements IWin32Window
    Private mHwnd As IntPtr

    Public Sub New(ByVal hWnd As Integer)
        mHwnd = New IntPtr(hWnd)
    End Sub
    Public ReadOnly Property Handle() As IntPtr Implements System.Windows.Forms.IWin32Window.Handle
        Get
            Return mHwnd
        End Get
    End Property
End Class
```

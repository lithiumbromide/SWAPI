---
title: "Creating Add-ins (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/CSharpAddIns.htm"
---

# Creating Add-ins (C#)

This topic shows how to create a debug add-in using C# in Microsoft Visual Studio.

**NOTE:** Because SOLIDWORKS PDM Professional cannot force a reload of add-ins if they are written in .NET, all client machines must be restarted to ensure that the latest version of the add-in is used.

1. Start Microsoft Visual Studio.
2. Click **File > New > Project.**
3. **Language dropdown:** C#**, Platform dropdown:** Windows**, Project type dropdown:** Library
4. Select **Class Library** **(.NET Framework)**.
5. Click **Next**.
6. Enter **Project name**, **Location** (click **...** to browse), **Solution** (Create new solution or Add to solution), and **Solution name** (if Create new solution).
7. In the **Framework** dropdown at the bottom, keep the default version (recommended) or select .NET Framework 4.7.2 or later. See [Using .NET Framework for Add-in Applications](Using_NET_Framework_in_Addins.htm) for more information.
8. Click **Create**.

  **Class1.cs** containing empty class, Class1, is created.
9. Right-click the project name in the Solution Explorer and click **Add > Reference...**.

  1. Click **Browse** in the left-hand panel, click **Browse...** and navigate to and select **EPDM.Interop.epdm.dll**, and click **OK**.
  2. Right-click **E****pdm.Interop.epdm** in the Solution Explorer, select **Properties**, and set **Embed Interop Types** to **False** to handle methods that pass arrays of structures.
  3. Click **Assemblies > Framework** in the left-hand panel, select **System.Windows.Forms**, and click **OK**.
10. Right-click the project name in the Solution Explorer and click **Properties.**

  1. On the **Application** tab, click **Assembly Information****...**.
  2. De-select **Make assembly COM-Visible**. Click **OK**.
  3. On the **Build** tab, select **AnyCPU** for the Platform target, de-select **Prefer 32-bit,** and select **Register for COM interop** in the Output section.
  4. On the **Debug** tab, select **Start external program** and type **C:\Windows\System32\notepad.exe** in the text field.
  5. Save the properties.
11. In Notepad, edit `project_path``\``project_name\project_name\``project_name`.**csproj**:

  1. Insert the following line below **<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">** and below **<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">**.

    <PlatformTarget>AnyCPU</PlatformTarget>
  2. Save the file and exit Notepad.
12. Double-click **Class1.cs** in the Solution Explorer to open the code window.
13. At the top of the code window, type:

  using System.Windows.Forms;
  using System.Runtime.InteropServices;
  using EPDM.Interop.epdm;
14. Replace**:**
15. To populate the GUID attribute above, click **Tools > Create GUID** in the IDE, select GUID Format 5, click **Copy**, and click **Exit**. Populate [Guid(""), ...] with the copied string.
16. Implement [IEdmAddIn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddin5~GetAddInInfo.html)[5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddin5~GetAddInInfo.html) by adding the following to Class1:

  ```vb
       public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
      {
          //Specify information to display in the add-in's Properties dialog box
          poInfo.mbsAddInName = "C# Add-in";
          poInfo.mbsCompany = "My Company";
          poInfo.mbsDescription = "Menu add-in that shows a message box.";
          poInfo.mlAddInVersion = 1;

          //Specify the minimum required version of SolidWorks PDM Professional
          poInfo.mlRequiredVersionMajor = 6;
          poInfo.mlRequiredVersionMinor = 4;

          // Register a menu command
          poCmdMgr.AddCmd(1, "C# Add-in", (int)EdmMenuFlags.EdmMenu_Nothing);

      }
  ```
17. Implement [IEdmAddIn5::](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)[OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) by adding the following to Class1:
18. Implement your own window handle wrapper by right-clicking the project name in the Solution Explorer and clicking **Add > Class**:

  1. Type **WindowHandle.cs** in **Name**.
  2. Click **Add**.
  3. Replace the code in the code window with the following code.

```vb
 using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Windows.Forms;

 namespace Addin_CSharp
{
    //Wrapper class to use SOLIDWORKS PDM Professional as the parent window
    class WindowHandle : IWin32Window
    {
        private IntPtr mHwnd;

        public WindowHandle(int hWnd)
        {
            mHwnd = new IntPtr(hWnd);
        }
        public IntPtr Handle
        {
            get { return mHwnd; }
        }
    }
}
```

Your add-in uses the new wrapper in the menu command handler to show the message box by calling System.Windows.Forms.MessageBox.Show in Class1::OnCmd in **Class1.cs**.

On the Visual Studio menu, click **Build > Build Solution** to build the add-in.

Install the add-in for debugging through the SOLIDWORKS PDM Professional Administration tool:

1. Open the SOLIDWORKS PDM Professional Administration tool.
2. Expand the vault where you want to install this add-in and log in as Admin.
3. Right-click **Add-ins** and select **Debug Add-ins**.
4. Click **Add Add-in**, browse to `project_path``\``project_name\project_name`**\bin\Debug**, click `project_name`**.dll**, and click **Open**.

  Your add-in's name, path, and class ID should appear in the **Add-ins installed for debugging on this machine** list.
5. Click **OK**.

In Microsoft Visual Studio, click **Debug > Start Debugging** or press F5.

Open Notepad and click **File > Open**.

In the Open dialog, click the name of the vault where you installed this add-in.

Right-click inside the vault view and click **C# Add-in**.

Displays the message, **C# Add-in**.

Click **OK** to close the message box.

Click **Cancel**.

Close Notepad.

### Complete Source Code

##### //Class1.cs

```vb
using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using System.Windows.Forms;
 using System.Runtime.InteropServices;
 using EPDM.Interop.epdm;

[Guid(""), ComVisible(true)]    // See step 14 above to create the GUID
 public class Class1 : IEdmAddIn5
{

    public void GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)
    {

        poInfo.mbsAddInName = "C# Add-in";
        poInfo.mbsCompany = "My Company";
        poInfo.mbsDescription = "Menu add-in that shows a message box.";
        poInfo.mlAddInVersion = 1;

        poInfo.mlRequiredVersionMajor = 6;
        poInfo.mlRequiredVersionMinor = 4;

        poCmdMgr.AddCmd(1, "C# Add-in", (int)EdmMenuFlags.EdmMenu_Nothing);

    }

     public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
    {

        if (poCmd.meCmdType == EdmCmdType.EdmCmd_Menu)
        {
            if (poCmd.mlCmdID == 1)
            {
                System.Windows.Forms.MessageBox.Show("C# Add-in");
            }
        }
    }
}
```

##### //WindowHandle.cs

```vb
 using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Windows.Forms;

 namespace Addin_CSharp
{
    class WindowHandle : IWin32Window
    {
        private IntPtr mHwnd;

        public WindowHandle(int hWnd)
        {
            mHwnd = new IntPtr(hWnd);
        }
        public IntPtr Handle
        {
            get { return mHwnd; }
        }
    }
}
```

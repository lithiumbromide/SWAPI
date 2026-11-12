---
title: "Stand-alone Applications (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/StandAloneAppCSharp.htm"
---

# Stand-alone Applications (C#)

This topic describes how to create a C# stand-alone application that logs into a SOLIDWORKS PDM Professional file vault and lists the files in the root folder.

1. Start up Microsoft Visual Studio.
2. Click **File > New > Project** > **C#, Windows, Desktop > Windows Forms App (.NET Framework)**.

  1. Type **StandaloneApplicationCSharp** in **Project n****ame**. Enter Solution and Solution name.
  2. For **Location**, click **...** and navigate to the folder where to create the project.
  3. Click **Create**.
  4. Right-click the name of your project in the Solution Explorer and select **Add > Reference...** to add the SOLIDWORKS PDM Professional primary assembly interop to your project.

    1. Click **Browse...** to navigate to the top folder of your SOLIDWORKS PDM Professional installation.
    2. Locate and click **EPDM.Interop.epdm.dll**.
    3. Click **Add.**
    4. Click **OK**.
3. Change the version of the .NET Framework and the platform target.

  1. From the VS menu, click **Project >** **StandaloneApplicationCSharp** **Properties > Build** and set **Platform target** to **Any CPU** and de-select **Prefer 32-bit.**
  2. Click the **Application** tab and keep suggested **Target framework** or change it to **.NET Framework 4.7.2** (or later).
  3. Save the project.
4. Right-click **Form1.cs** in the Solution Explorer and click **View Designer**.
5. Click **View > Toolbox**.
6. Drag a button from the Toolbox onto the form.
7. Double-click the button to open **Form1.cs** and replace all of the code in the code window with the following code.

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System;
using System.Windows.Forms;
using EPDM.Interop.epdm;

namespace StandaloneApplicationCSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(System.Object sender, System.EventArgs e)
        {
            try
            {

                //Create a file vault interface and log into a vault
                IEdmVault5 vault = new EdmVault5();
                vault.LoginAuto("MyVaultName", this.Handle.ToInt32());

                //Get the vault's root folder interface
                string message = "";
                IEdmFile5 file = null;
                IEdmFolder5 folder = null;
                folder = vault.RootFolder;

                //Get position of first file in the root folder
                IEdmPos5 pos = null;
                pos = folder.GetFirstFilePosition();
                if (pos.IsNull)
                {
                    message = ("The root folder of your vault does not contain any files.");
                    MessageBox.Show(message);
                    return;
                }
                message = ("The root folder of your vault contains these files: " + "\n");
                while (!pos.IsNull)
                {
                    file = folder.GetNextFile(pos);
                    message = message + file.Name + "\n";
                }

                //Show the names of all files in the root folder
                MessageBox.Show(message);

            }

            catch (System.Runtime.InteropServices.COMException ex)
            {
                MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + "\n" + ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }
    }
}
```

1.

  ```vb
   Replace  MyVaultName in the code with the name of a SOLIDWORKS PDM Professional vault on your computer.
  ```
2.

  ```vb
   Click Debug > Start Debugging or press F5.
  ```

  1.

    ```vb
     Click Button1 on the form.
    A message box is displayed that either contains the names of the files in the root folder of the specified vault or informs you that the root folder of the specified vault does not contain any files.
    ```
  2.

    ```vb
     Close the form.
    ```
3.

  ```vb
   Click File > Save All.
  ```

### See Also

[Stand-alone Applications (VB.NET)](StandAloneApp.htm)

[Stand-alone Applications (C++)](StandAloneAppCpp.htm)

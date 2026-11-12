---
title: "Stand-alone Applications (VB.NET)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/StandAloneApp.htm"
---

# Stand-alone Applications (VB.NET)

This topic describes how to create a VB.NET stand-alone application that logs into a SOLIDWORKS PDM Professional file vault and lists the files in the root folder.

1. Start up Microsoft Visual Studio.
2. Click **File > New > Project** **>** **Visual Basic, Windows, Desktop > Windows Forms App (.NET Framework)**.

  1. Type **StandaloneApplicationVBNET** in Project n**ame**. Enter **Solution name**.
  2. For **Location**, click **...** and navigate to the folder where to create the project.
  3. Click **Create**.
  4. Right-click the name of your project in the Solution Explorer and select **Add > Reference...** to add the SOLIDWORKS PDM Professional primary assembly interop to your project.

    1. Click **Browse...** to navigate to the top folder of your SOLIDWORKS PDM Professional installation.
    2. Locate and click **EPDM.Interop.epdm.dll**.
    3. Click **Add.**
    4. Click **OK**.
3. Change the version of the .NET Framework and the platform target.

  1. From the VS menu, click **Project >** **StandaloneApplicationVBNET** **Properties > Compile**.
  2. Set **Target CPU** to **AnyCPU**.
  3. De-select **Prefer 32-bit**.
  4. Click the **Application** tab and Keep suggested **Target framework (all configurations)** or change it to **.NET Framework 4.7.2** (or later).
  5. Save the project.
4. Right-click **Form1.vb** in the Solution Explorer and click **View Designer**.
5. Click **View > Toolbox**.
6. Drag a button from the Toolbox onto the form.
7. Double-click the button to open **Form1.vb** and replace all of the code in the code window with the following code.

```
Imports EPDM.Interop.epdm

Public Class Form1

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        On Error GoTo ErrHandler

        'Create a file vault interface and log in to a vault
        Dim vault As IEdmVault5 = New EdmVault5
        vault.LoginAuto("MyVaultName", Me.Handle.ToInt32)

        'Get the vault's root folder interface
        Dim message As String
        Dim file As IEdmFile5
        Dim folder As IEdmFolder5
        folder = vault.RootFolder

        'Get position of first file in the root folder
        Dim pos As IEdmPos5
        pos = folder.GetFirstFilePosition
        If pos.IsNull Then
            message = "The root folder of your vault does not contain any files."
        Else
            message = "The root folder of your vault contains these files:" + vbLf
        End If

        'For all files in the root folder, append the name to the message
        While Not pos.IsNull
            file = folder.GetNextFile(pos)
            message = message + file.Name + vbLf
        End While

        'Show the names of all files in the root folder
        MsgBox(message)

        Exit Sub

ErrHandler:
        If vault Is Nothing Then
            MsgBox("Could not create vault interface.")
        Else
            Dim ErrName As String
            Dim ErrDesc As String
            vault.GetErrorString(Err.Number, ErrName, ErrDesc)
            MsgBox("Something went wrong." + vbLf + ErrName + vbLf + ErrDesc)
        End If

    End Sub

End Class
```

1.

  ```vb
   Replace  MyVaultName  in the code with the name of a SOLIDWORKS PDM Professional vault on your computer.
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

1.

  ```vb
   Click File > Save All.
  ```

### See Also

[Stand-alone Applications (C#)](StandAloneAppCSharp.htm)

[Stand-alone Applications (C++)](StandAloneAppCpp.htm)

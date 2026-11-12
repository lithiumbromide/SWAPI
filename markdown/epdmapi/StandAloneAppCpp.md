---
title: "Stand-alone Applications (C++)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/StandAloneAppCpp.htm"
---

# Stand-alone Applications (C++)

This topic describes how to create a C++ Windows MFC stand-alone application that logs into a SOLIDWORKS PDM Professional file vault and lists the files in the root folder.

1. Start up Microsoft Visual Studio.
2. Click **File > New > Project > C++, Windows, Desktop > MFC App**.

  1. Enter **Project** **Name** and **Solution name**.
  2. For **Location**, click **...** and browse to the folder where to create your project.
  3. Click **Create**.
  4. Select **Dialog based** in **Application type** dropdown.
  5. Click **Next, Next**, **Next**, and **Next**.
  6. Click **Finish**.

1.

  ```
  Replace MyVault in the code with the name of a SOLIDWORKS PDM Professional vault on your computer.
  ```
2.

  ```
  If creating this project on a 64-bit computer, change the platform to x64:
  ```

  1.

    ```
    Right-click the name of your project in the Solution Explorer and click Properties.
    ```
  2.

    ```
    Click the Configuration Manager button.
    ```
  3.

    ```
    Click the down-arrow button in the Platform column and select New.
    ```
  4.

    ```
    Select x64 in New platform and click OK.
    ```
  5.

    ```
    Click Close. If Active(x64) is not shown in Platform, then repeat Steps 2 - 5 until it is.
    ```
  6.

    ```
    Click OK.
    ```
3.

  ```
  Specify the project configuration properties:
  ```

  1.

    ```
    Right-click the name of your project in the Solution Explorer and click Properties.
    ```
  2.

    ```
    Click Configuration Properties > General.
    ```
  3.

    ```
    Set Use of MFC to Use MFC in a Shared DLL.
    ```
  4.

    ```
    Set Character Set to Use Unicode Character Set.
    ```
4.

  ```
  Click Build > Clean Solution.
  ```
5.

  ```
  Click Build > Rebuild Solution.
  ```
6.

  ```
  Click Debug > Start Debugging or press F5.
  ```

  1.

    ```
    Click Button1.

    A message box is displayed that either contains the names of the files in the root folder of the specified vault or informs you that the root folder of the specified vault does not contain any files.
    ```
  2.

    ```
    Close the form.
    ```
7.

  ```
  Click File > Save All.
  ```

### See Also

[Stand-alone Applications (VB.NET)](StandAloneApp.htm)

[Destroy Deleted Files in Vault Example (C++)](Destroy_Deleted_Files_in_Vault_Example_CSharp.htm)

[Destroy Deleted Files in Vault Example (VB.NET)](Destroy_Deleted_Files_in_Vault_Example_VBNET.htm)

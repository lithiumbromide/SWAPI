---
title: "Using .NET Framework in Add-in Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/Using_NET_Framework_in_Addins.htm"
---

# Using .NET Framework in Add-in Applications

Many versions of .NET Framework may be installed with your Windows operating system or Visual Studio. See [https://msdn.microsoft.com/en-us/library/bb822049(v=vs.110).aspx](https://msdn.microsoft.com/en-us/library/bb822049(v=vs.110).aspx).

SOLIDWORKS PDM Professional supports one or more versions of .NET Framework.

| SOLIDWORKS PDM Professional versions... | Support .NET Framework... |
| --- | --- |
| 2013 and later | 4 .0 and later |
| 2009 - 2012 | 3.5, 3.0, and 2.0 |
| 2008 and earlier | 2.0 |

If using .NET Framework 4.0 or later, prevent failures when calling methods that pass arrays of structures by:

1. Opening the project in Visual Studio.
2. Right-clicking **References > EPDM.Interop.epdm** in the Solution Explorer and selecting **Properties**.
3. Setting **Embed Interop Types** to **False** in Properties.
4. Right-clicking **References > EPDM.Interop.EPDMResultCode** in the Solution Explorer and selecting **Properties**.
5. Setting **Embed Interop Types** to **False** in Properties.
6. Initializing arrays of structures in your code to:

  - VB.NET: **Nothing**
  - C#: **null**

If your SOLIDWORKS PDM Professional 2012 or earlier version add-in application is compiled using Microsoft Visual Studio and a .NET Framework version other than version 2.0, then SOLIDWORKS PDM Professional may show the following message when you try to load the add-in:

“The Archive Server could not open the Windows Registry.”

- C# or VB.NET

  To solve this problem, try changing your add-in project’s target framework to .NET Framework 2.0:

1. Right-click the project in the **Solution Explorer**.
2. Select **Properties**.
3. Click **Compile > Advanced Compile Options**.
4. Select .NET Framework 2.0.
5. Click **OK**.

After changing your project’s target framework to .NET Framework 2.0, you might no longer be able to reference the SOLIDWORKS PDM Professional `nnnn` Type Library (**EdmInterface.dll**), because Visual Studio created the DLL using the latest version of .NET Framework, but you just changed the project to target an earlier version of .NET Framework (2.0). If you encounter this problem, you can generate a compatible SOLIDWORKS PDM Professional primary interop assembly by using the Microsoft's Type Library Importer (**TlbImp.exe)** that is included in an earlier version of the Microsoft .NET Framework SDK.

1. Download and install a version of .NET Framework SDK that is compatible with your add-in project's version.
2. Open a Windows Command Prompt.
3. Navigate to **C:\Program Files\Microsoft SDKs\Windows\v**`x.x`**\Bin** in which the earlier .NET Framework version of **TlbImp.exe** is installed.
4. Type **TlbImp.exe** `install_dir`**\EdmInterface.dll /sysarray /out:Interop.EdmLib.dll /namespace:EdmLib.**
5. Modify all add-in examples in this help file to use the new interop ssembly.

- C++

  This problem can occur at runtime if the add-in failed to register its DLL during the build process. To solve this problem, ensure that your add-in registers the DLL:

  1. Open your C++ add-in project.
  2. Right-click the project in the **Solution Explorer**.
  3. Select **Properties**.
  4. Click **Linker > Input**.
  5. Configure **Module Definition File** to point to the add-in's `project_name`**.def**.
  6. Save the project.
  7. Click **Build > Clean Solution**.
  8. Click **Build > Build Solution**.

##### See Also

[Using .NET Framework in Stand-alone Applications](Using_NET_Framework_in_Applications.htm)

---
title: "PDM Professional API Troubleshooting Guide"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/Troubleshooting_Guide.htm"
---

# PDM Professional API Troubleshooting Guide

The examples provided with the PDM APIs are thorough and extensive. You should use them carefully when you develop your own PDM applications and add-ins. This topic discusses several important steps in the PDM API examples that are often overlooked by PDM developers. It also answers some questions that have been frequently asked of API Support.

[Why am I getting "The parameter is incorrect. (Exception from HRESULT: 0x80070057 (E_INVALIDARG)" when my PDM API application
calls a method that passes an array of structures?](#Answer1)

[Why does adding my add-in to the Admin tool fail with the message "Please select at least one DLL implementing the IEdmAddin5
interface."?](#Answer2)

[When I add an add-in to the Admin tool, why does it throw "An older version of the add-in is already loaded in memory..."?](#Answer3)

[Why aren't I hitting breakpoints when I debug my PDM API application?](#Answer4)

[Why are my add-in's commands not working?](#Answer5)

[How do you debug a task add-in?](#Answer6)

[Why doesn't my PDM add-in appear in the Debug Add-ins window after I've selected to debug the add-in in the Admin tool?](#Answer7)

[How do I specify the lParentWnd parameter in methods?](#Answer8)

[Why am I seeing **Failed to extract add-in** and **Error loading add-ins** messages while my add-in is running?](#Answer9)

[My add-in works when compiled for .NET Framework 2.0, 3.0, and 3.5. But with .NET Framework 4.0, I get a runtime error,
"Call to method 'OnCmd' in add-in failed. Error code = 0x080131522 (Unknown error 0x080131522)."](#Answer10)

======================================================================================

Why am I getting "The parameter is incorrect. (Exception from HRESULT: 0x80070057 (E_INVALIDARG)" when my PDM API application
calls a method that passes an array of structures?

If you are using .NET 4.0, you must right-click EPDM.Interop.epdm in References, click Properties, and set Embed Interop Types
to False.

The reason is that all of the structures defined in the PDM Pro API (nothing but COM API’s) are not embedded by the .Net
Framework if this property is set to true. This is a Microsoft issue with COM, and there is no solution for it at the moment.

*KEEP IN MIND THAT YOU SHOULD ONLY SET THIS PROPERTY TO FALSE FOR EPDM.Interop.epdm.dll. FOR ALL OTHER EXTERNAL REFERENCES IN
YOUR PROJECT THIS PROPERTY SHOULD BE SET TO TRUE.

[Back](#top)

Why does adding my .NET or C++ add-in to the Admin tool fail with the message "Please select at least one DLL implementing the IEdmAddin5
interface."?

The Admin tool did not find the ISwAddin interface for some reason, usually because multiple classes were made COM-visible in
your add-in, and the Admin tool randomly chose the wrong class with which to start the add-in. To correct this problem:

1. In project properties deselect **Application > Assembly Information> Make Assembly COM-visible**.
2. Make only the class that implements IEdmAddin5 COM-Visible as follows:

'VB.NET
Imports EPDM.Interop.epdm
Imports System.Runtime.InteropServices

<Guid("07a33492-234f-4e8a-8c4f-6b66d8cf16c2")> _
<ComVisible(True)> _
Public Class SWEPDMAddin
Implements IEdmAddIn5
Public Sub GetAddInInfo
Public Sub OnCmd
…

The Guid above is created in Visual Studio's **Tools > Create GUID**. Copy and paste the GUID to one class that implements the
IEDMAddin5 interface.

3. If you are on Windows 8 or above, make sure that .Net CLR 2.0 is enabled on your machine, because your add-in is using .Net Framework 3.5. Also, ensure that the UAC is off on this machine.
4. In project properties select **Build > Register for COM interop**.
5. Re-compile the add-in.
6. Open the task manager and kill **edmserver.exe**, **viewserver.exe** and **explorer.exe**.
7. Restart the Admin tool as administrator.
8. Add the add-in dlls in the Admin tool.

If this happens with your C++ add-in, try re-compiling the add-in DLL under Administrator privileges in Visual Studio so the add-in is registered. Also, make sure to open the Admin Tool with Administrator privileges, or you won't be able to successfully add the add-in.

[Back](#top)

When I add an add-in to the Admin tool, why does it throw "An older version of the add-in is already loaded in memory..."?

There is already an add-in with the same version in the vault.
To add the add-in you must create your own GUID using Visual Studio’s **Tools > Create GUID**. Copy the new GUID to the class
implementing the IEdmAddin5 interface, setting the COMVisible attribute to true. This uniquely identifies each add-in and
also prevents the loading of duplicate add-ins in your vault.

//C#
using System.Runtime.InteropServices;

namespace test
{
[Guid("E9B24B05-A4CA-401B-A644-AB59175D758E"),ComVisible(true)]
public class Class1 : IEdmAddIn5
...
}

[Back](#top)

Why aren't I hitting breakpoints when I debug my PDM API application?

If your project targets a .NET Framework older than 4.0, you must add an application configuration file to the debug
application in order for breakpoints to work. If you are using Notepad for debugging, then add the notepad config file to the
notepad exe’s location i.e. **C:\Windows\Notepad.exe**. Add notepad.exe.config for .Net CLR 2 or CLR 4, depending on your .NET
framework.

<!-- sample notepad.exe.config -->
<?xml version ="1.0"?>
<configuration>
<startup>
<supportedRuntime version="v2.0.[version on your machine]" />
</startup>
</configuration>

To determine the correct [version on your machine] look in the “C:\Windows\Microsoft.NET\Framework” directory for the most recent
“v2.0.xxxxx” folder.

[Back](#top)

Why are my add-in's commands not working?

Are you passing arguments to OnCmd() by value or by reference? PDM Pro add-ins require that you implement IEdmAddIn5::OnCmd, passing arguments using ByRef:

C#:

**public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData) {}**

VB.NET:

**Public Sub OnCmd(ByRef poCmd As EdmCmd, ByRef ppoData As EdmCmdData()) Implements IEdmAddIn5.OnCmd**

[Back](#top)

How do you debug a task add-in?

The task add-in needs to be fully installed in the vault before you can install it as a task or debug it. Therefore in order to debug a task
add-in, you must attach the add-in’s running process to the debugger.

Since add-ins are loaded and unloaded at unpredictable times, you can pop up a message box to force the add-in to pause
while you attach the debugger to the add-in's process.

[Back](#top)

Why doesn't my PDM add-in appear in the Debug Add-ins window after I've configured the Admin tool to debug the add-in?

1. In the project's properties, select **Application > Register for COM interop**.
2. Compile the add-in.
3. Kill **edmserver.exe**, **viewserver.exe**, and **explorer.exe** from the task manager.
4. Restart the Admin tool as an administrator.
5. Add the add-in for debugging in the Admin tool.
6. Debug the add-in.

```vb
Back
```

How do I specify the lParentWnd parameter in method calls?

The lParentWnd parameter ensures that your application’s dialog remains visible. When your application displays a dialog box, you need to make sure that it is not possible to switch between the dialog box and the Explorer window behind it (or whatever application it is launched from). Failure to ensure this may cause your application's dialog box to be hidden behind an inactive Explorer window or application, leaving the impression that your program has hung.

For methods called in Windows Forms, you can specify lParentWnd as follows:

VB.NET:

**Me.Handle.ToInt32()**

C#:

**this.Handle.ToInt32()**

For non-windows-forms applications, you can specify lParentWnd with 0 (zero).

[Back](#top)

Why am I seeing **Failed to extract add-in** and **Error loading add-ins** messages when my add-in is running?

1. In Visual Studio, select **Compile** or **Build tab > Register for COM interop**.
2. If you are on Windows 10, verify that the UAC is OFF.
3. The host application needs an elevation (i.e. it must be run with administrator privileges).
4. Start the Admin Tool as Administrator and then add the add-in.

[Back](#top)

My add-in works when compiled for .NET Framework 2.0, 3.0, and 3.5. But with .NET Framework 4.0, I get a runtime error,
"Call to method 'OnCmd' in add-in failed. Error code = 0x080131522 (Unknown error 0x080131522)."

As of PDM Pro 2013 we distribute the primary interop assembly, **EPDM.Interop.epdm.dll**.
Add this interop assembly to your add-in's references when compiling for .NET Framework 4.0 and later.

[Back](#top)

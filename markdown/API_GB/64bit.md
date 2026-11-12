---
title: "Writing 64-bit Add-ins"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/64bit.htm"
---

# Writing 64-bit Add-ins

This topic shows how to create add-ins for the 64-bit version of SOLIDWORKS PDM Professional.

**64-bit .NET Add-ins**

You must use Microsoft Visual Studio 2005, or later, to create managed (.NET) DLL add-ins. The build target must be set to **Any CPU** for the DLL to load in both 32-bit and 64-bit hosts. Managed DLL add-ins are added to the vault using the [Administration tool](AdminDlg.htm).

**Native DLL Add-ins**

A native 32-bit DLL cannot be loaded into a 64-bit EXE, and a 64-bit native DLL cannot be loaded into a 32-bit EXE. Because SOLIDWORKS PDM Professional gets loaded into both 32- and 64-bit processes, you must build two versions of your add-in, 32-bit and 64-bit.

Native DLL add-ins that are added to the vault on a 64-bit machine also work on a 32-bit machine:

1. Right-click the **Add-ins** node in the Administration tool.
2. Select `New` **Add-in**.
3. Navigate to and open the 64-bit add-in DLL.
4. In the Properties dialog, select **Files** in the left pane.
5. Click `Add Files`.
6. Navigate to and open the 32-bit add-in DLL.
7. Click **OK**.

SOLIDWORKS PDM Professional creates a single add-in package that contains both 32-bit and 64-bit versions of the add-in. The 32-bit version is loaded in 32-bit processes, and the 64-bit version is loaded in 64-bit processes.

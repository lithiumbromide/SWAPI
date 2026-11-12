---
title: "Using .NET Framework in Stand-alone Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "API_GB/Using_NET_Framework_in_Applications.htm"
---

# Using .NET Framework in Stand-alone Applications

If your Visual Studio project uses the [primary interop assembly](GettingStarted-epdmapi.html) provided with SOLIDWORKS PDM Professional:

- Reference **EPDM.Interop.epdm.dll** and **EPDM.Interop.EPDMResultCode.dll** by:

  1. Right-clicking the project name in the Solution Explorer.
  2. Selecting **Add Reference.**
  3. Selecting **Framework** in the left-side panel.
  4. Clicking **Browse** and navigating to the top folder of your SOLIDWORKS PDM Professional installation.
  5. Locating and selecting **EPDM.Interop.epdm.dll**.
  6. Clicking **Open**.
  7. Clicking **Add**.
  8. Repeat step 4.
  9. Locating and selecting **EPDM.Interop.EPDMResultCode.dll**.
  10. Repeat steps 6 and 7.
  11. Click **Close**.
- Include the following statements in your code:

  - VB.NET:

    **Imports EPDM.Interop.epdm
    Imports EPDM.Interop.EPDM.Interop.EPDMResultCode**
  - C#:
    **using EPDM.Interop.epdm
    using EPDM.Interop.EPDMResultCode**

- Change the version of .NET Framework, select the platform target **Any CPU**, and for .NET Frameworks 4.5 de-select **Prefer 32-bit**:

  - VB.NET:

    - In **Project >** `your_project_name` **Properties... > Application**, set **Target framework** to **.NET Framework 4.0 or later** (or keep your Visual Studio's default setting)
    - In **Project >** `your_project_name` **Properties... > Compile > Compile Options**:

      - Set **Target CPU** to **AnyCPU**
      - If the .NET Framework version is 4.5 or later, de-select **Prefer 32-bit**
  - C#:

    - In **Project >** `your_project_name` **Properties... > Application**, set **Target framework** to **.NET Framework 4.0 or later** (or keep your Visual Studio's default setting)
    - In **Project >** `your_project_name` **Properties... > Build**:

      - Set **General > Platform target** to **Any CPU**
      - If the .NET Framework version is 4.5 or later, de-select **Prefer 32-bit**
- Prevent failures when calling methods that pass arrays of structures by:

  1. Opening the project in Visual Studio.
  2. Right-clicking **References > EPDM.Interop.epdm** in the Solution Explorer and selecting **Properties**.
  3. Setting **Embed Interop Types** to **False** in Properties.
  4. Right-clicking **References > EPDM.Interop.EPDMResultCode** in the Solution Explorer and selecting **Properties**.
  5. Setting **Embed Interop Types** to **False** in Properties.
  6. Initializing arrays of structures in your code to:

    - VB.NET: **Nothing**
    - C#: **null**

##### See Also

[Using .NET Framework in Add-in Applications](Using_NET_Framework_in_Addins.htm)

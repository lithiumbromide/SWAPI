---
title: "Using .NET Framework in Stand-alone Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/Using_NET_Framework_in_Applications.htm"
---

# Using .NET Framework in Stand-alone Applications

If your Visual Studio project uses the [primary interop assembly](GettingStarted-epdmapi.html) provided with SOLIDWORKS PDM Professional, add the following dependencies to your project:

- **EPDM.Interop.epdm.dll** and **EPDM.Interop.EPDMResultCode.dll**:

  1. Right-click the project name in the Solution Explorer.
  2. Select **Add > Project Reference.**
  3. Click **Browse tab > Browse...** and navigate to the top folder of your SOLIDWORKS PDM Professional installation.
  4. Locate and select **EPDM.Interop.epdm.dll**.
  5. Click **Add** and **OK.**
  6. Repeat step 3.
  7. Locate and select **EPDM.Interop.EPDMResultCode.dll**.
  8. Repeat step 5.
- Include the following statements at the top of your code:

  - VB.NET:

    **Imports EPDM.Interop.epdm
    Imports EPDM.Interop.EPDM.Interop.EPDMResultCode**
  - C#:

    **using EPDM.Interop.epdm;
    using EPDM.Interop.EPDMResultCode;**

- Change the version of .NET Framework, select the platform target **Any CPU**, and for .NET Frameworks 4.5 or later de-select **Prefer 32-bit**:

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
  2. Right-clicking **Dependencies > Assemblies > EPDM.Interop.epdm** in the Solution Explorer and selecting **Properties**.
  3. Setting **Embed Interop Types** to **No**.
  4. Right-clicking **Dependencies > Assemblies > EPDM.Interop.EPDMResultCode** in the Solution Explorer and selecting **Properties**.
  5. Setting **Embed Interop Types** to **No**.
  6. Initializing arrays of structures in your code to:

    - VB.NET: **Nothing**
    - C#: **null**

##### See Also

[Using .NET Framework in Add-in Applications](Using_NET_Framework_in_Addins.htm)

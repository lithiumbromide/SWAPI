---
title: "GetCurrentLicenseType Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCurrentLicenseType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentLicenseType.html"
---

# GetCurrentLicenseType Method (ISldWorks)

Gets the type of license for the current SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentLicenseType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.GetCurrentLicenseType()
```

### C#

```csharp
System.int GetCurrentLicenseType()
```

### C++/CLI

```cpp
System.int GetCurrentLicenseType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of SOLIDWORKS Design license as defined in [swLicenseType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLicenseType_e.html)

## VBA Syntax

See [SldWorks::GetCurrentLicenseType](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCurrentLicenseType.html).

## Examples

[Get License Types of SOLIDWORKS (C#)](Get_License_Types_of_SOLIDWORKS_Example_CSharp.htm)
[Get License Types of SOLIDWORKS (VB.NET)](Get_License_Types_of_SOLIDWORKS_Example_VBNET.htm)
[Get License Types of SOLIDWORKS (VBA)](Get_License_Types_of_SOLIDWORKS_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IModelDocExtension::GetLicenseType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLicenseType.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0

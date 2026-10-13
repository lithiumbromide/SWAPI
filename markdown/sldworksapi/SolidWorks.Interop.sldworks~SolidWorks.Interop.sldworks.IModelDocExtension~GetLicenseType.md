---
title: "GetLicenseType Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetLicenseType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLicenseType.html"
---

# GetLicenseType Method (IModelDocExtension)

Gets the type of SOLIDWORKS license used when the model was created.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLicenseType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetLicenseType()
```

### C#

```csharp
System.int GetLicenseType()
```

### C++/CLI

```cpp
System.int GetLicenseType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of SOLIDWORKS license as defined in [swLicenseType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLicenseType_e.html)

## VBA Syntax

See [ModelDocExtension::GetLicenseType](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetLicenseType.html).

## Examples

[Get License Type of SOLIDWORKS (C#)](Get_License_Types_of_SOLIDWORKS_Example_CSharp.htm)
[Get License Type of SOLIDWORKS (VB.NET)](Get_License_Types_of_SOLIDWORKS_Example_VBNET.htm)
[Get License Type of SOLIDWORKS (VBA)](Get_License_Types_of_SOLIDWORKS_Example_VB.htm)

## Remarks

This method always returns 0 (swLicenseType_e.swLicenseType_Full) for files saved under any commercial SOLIDWORKS license.

To get the license type of this SOLIDWORKS installation, use [ISldWorks::GetCurrentLicenseType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentLicenseType.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

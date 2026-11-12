---
title: "GetActivePropertyManagerPage Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetActivePropertyManagerPage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetActivePropertyManagerPage.html"
---

# GetActivePropertyManagerPage Method (IModelDocExtension)

Gets the name of the active PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActivePropertyManagerPage() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.String

value = instance.GetActivePropertyManagerPage()
```

### C#

```csharp
System.string GetActivePropertyManagerPage()
```

### C++/CLI

```cpp
System.String^ GetActivePropertyManagerPage();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the active PropertyManager page

## VBA Syntax

See [ModelDocExtension::GetActivePropertyManagerPage](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetActivePropertyManagerPage.html).

## Examples

[Get Active PropertyManager Page Name (C#)](Get_Active_PropertyManager_Page_Name_Example_CSharp.htm)
[Get Active PropertyManager Page Name (VB.NET)](Get_Active_PropertyManager_Page_Name_Example_VBNET.htm)
[Get Active PropertyManager Page Name (VBA)](Get_Active_PropertyManager_Page_Name_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0

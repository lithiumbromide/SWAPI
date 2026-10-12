---
title: "ISetUserValueIn3 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "ISetUserValueIn3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.html"
---

# ISetUserValueIn3 Method (IDimension)

Sets the value of this dimension in the units of the specified document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetUserValueIn3( _
   ByVal Doc As ModelDoc2, _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Doc As ModelDoc2
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim value As System.Integer

value = instance.ISetUserValueIn3(Doc, NewValue, WhichConfigurations)
```

### C#

```csharp
System.int ISetUserValueIn3(
   ModelDoc2 Doc,
   System.double NewValue,
   System.int WhichConfigurations
)
```

### C++/CLI

```cpp
System.int ISetUserValueIn3(
   ModelDoc2^ Doc,
   System.double NewValue,
   System.int WhichConfigurations
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Doc`: [Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) whose units you want to use
- `NewValue`: Value for this dimension in the units of the document specified by Doc
- `WhichConfigurations`: Configurations to set the value as defined in [swSetValueInConfiguration_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html)

### Return Value

Success indicator as defined in [swSetValueReturnStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueReturnStatus_e.html)

## VBA Syntax

See [Dimension::ISetUserValueIn3](ms-its:sldworksapivb6.chm::/sldworks~Dimension~ISetUserValueIn3.html).

## Remarks

The WhichConfigs argument is equivalent to the **Change Parameter** dialog in the SOLIDWORKS Design user interface, which gives the user the option of having the value set in all configurations or the current configuration. If there is one configuration in the part, SOLIDWORKS ignores this argument.

This method allows you to change the value of a read-only dimension. You can use [IDimension::ReadOnly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~ReadOnly.html) to determine if a dimension is read-only.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.html)
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.html)
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.html)
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.html)
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.html)
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.html)
[IDimension::SetSystemValue2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue2.html)
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.html)
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.html)
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

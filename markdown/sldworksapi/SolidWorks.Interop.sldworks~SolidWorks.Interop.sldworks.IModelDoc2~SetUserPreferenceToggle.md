---
title: "SetUserPreferenceToggle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetUserPreferenceToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html"
---

# SetUserPreferenceToggle Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUserPreferenceToggle( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal OnFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim OnFlag As System.Boolean
Dim value As System.Boolean

value = instance.SetUserPreferenceToggle(UserPreferenceValue, OnFlag)
```

### C#

```csharp
System.bool SetUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

### C++/CLI

```cpp
System.bool SetUserPreferenceToggle(
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreferenceValue`: Value to toggle as defined in [swUserPreferenceToggle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html)
- `OnFlag`: True to toggle the value on, false to toggle the value off

### Return Value

True if the toggle is successful, false if not

## VBA Syntax

See [ModelDoc2::SetUserPreferenceToggle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetUserPreferenceToggle.html).

## Examples

[Hide or Show All Types (VBA)](Hide_or_Show_All_Types_Example_VB.htm)
[Ignore Feature Colors (VBA)](Ignore_Feature_Colors_Example_VB.htm)

## Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

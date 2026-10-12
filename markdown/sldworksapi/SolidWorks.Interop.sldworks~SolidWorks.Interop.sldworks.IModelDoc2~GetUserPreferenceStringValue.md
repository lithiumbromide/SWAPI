---
title: "GetUserPreferenceStringValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetUserPreferenceStringValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceStringValue.html"
---

# GetUserPreferenceStringValue Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceString](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceString.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UserPreference As System.Integer
Dim value As System.String

value = instance.GetUserPreferenceStringValue(UserPreference)
```

### C#

```csharp
System.string GetUserPreferenceStringValue(
   System.int UserPreference
)
```

### C++/CLI

```cpp
System.String^ GetUserPreferenceStringValue(
   System.int UserPreference
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserPreference`: Value as defined in [swUserPreferenceStringValue_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceStringValue_e.html)

### Return Value

String value of UserPreference

## VBA Syntax

See [ModelDoc2::GetUserPreferenceStringValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetUserPreferenceStringValue.html).

## Examples

[Get Transform of Coordinate System (VB.NET)](Get_Transform_of_Coordinate_System_Example_VB.NET.htm)
[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)
[Save Rollbacked Part as Parasolid File (VBA)](Save_Roll_Backed_Part_as_Parasolid_File_Example_VB.htm)

## Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS Design software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

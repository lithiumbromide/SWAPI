---
title: "SetLibraryMaterial2 Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "SetLibraryMaterial2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetLibraryMaterial2.html"
---

# SetLibraryMaterial2 Method (ICWBeamBody)

Sets the material library and material name for the beam.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLibraryMaterial2( _
   ByVal SLibWithPathName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim SLibWithPathName As System.String
Dim SMaterialName As System.String
Dim value As System.Boolean

value = instance.SetLibraryMaterial2(SLibWithPathName, SMaterialName)
```

### C#

```csharp
System.bool SetLibraryMaterial2(
   System.string SLibWithPathName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.bool SetLibraryMaterial2(
   System.String^ SLibWithPathName,
   System.String^ SMaterialName
)
```

### Parameters

- `SLibWithPathName`: Path to the material library
- `SMaterialName`: Material name in the library

### Return Value

-1 or true if material library and library name are set, 0 or false if not

## Examples

[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)

## Remarks

This method returns a boolean value that can be cast to an integer.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
